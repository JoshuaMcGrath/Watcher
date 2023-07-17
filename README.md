# Watcher
Watch for any changes within your project and test to make sure nothing is broken!


## How to run
Navigate to folder in which youve saved the watch.py script. Run in a free terminal within your IDE or terminal Environment 

```
python3 watch.py --folder {root_folder_location_of_app}
```

You can also monitor just a file instead of your whole app

```
python3 watch.py --folder {root_folder_location_of_app} --file {location_of_file_from_project_root}
```

It'll print out the process ID as the first thing it does and you check how much memory it uses using this command here 
```
ps u -p {put-process-id-here} | awk '{sum=sum+$6}; END {print sum/1024}'
```
