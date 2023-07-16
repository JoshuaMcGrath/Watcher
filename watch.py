import argparse
import os
import time
import subprocess


def watch():
    print(os.getpid())
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--fileName',
        help='The root path to the file name in which you want to monitor'
        )
    parser.add_argument(
        '--folder',
        help='The root path to the project folder in which you want to monitor'
    )
    parsedArgs = parser.parse_args()
    if parsedArgs.fileName and parsedArgs.folder:
        watch_specific_file(folder=parsedArgs.folder, file=parsedArgs.fileName)
    elif parsedArgs.folder and not parsedArgs.fileName:
        watch_folder(folder=parsedArgs.folder)


def watch_specific_file(folder, file):
    listOfFilesModified = {}
    try:
        for root, dirs, files in os.walk(folder):
            folder_file = os.path.join(root, file)
            while True:
                if file not in files:
                    print("file or directory not found")
                    exit()
                modTime = os.path.getmtime(folder_file)
                if folder_file not in listOfFilesModified:
                    listOfFilesModified[folder_file] = modTime
                if modTime > listOfFilesModified.get(folder_file):
                    run_unit_tests(folder=folder)
                    listOfFilesModified.update(
                        {folder_file: modTime}
                    )
                time.sleep(3)
    except Exception as e:
        print(e)


def watch_folder(folder):
    listOfFilesModified = {}
    try:
        while True:
            for root, dirs, files in os.walk(folder):
                if not files:
                    print("No files in folder!")
                    exit()
                if not listOfFilesModified:
                    listOfFilesModified = dict.fromkeys(files)
                    continue
                for file in files:
                    modTime = os.path.getmtime(os.path.join(root, file))
                    if not listOfFilesModified.get(file):
                        listOfFilesModified.update(
                            {file: modTime}
                        )
                    if modTime > listOfFilesModified.get(file):
                        run_unit_tests(folder=folder)
                        listOfFilesModified.update(
                            {file: modTime}
                        )
            time.sleep(3)
    except Exception as e:
        print(e)


def run_unit_tests(folder):
    subprocess.call([
                    "python",
                    "-m",
                    "unittest",
                    "discover",
                    "-s",
                    str(folder),
                    "-p",
                    "*test*.py"
                    ])


watch()
