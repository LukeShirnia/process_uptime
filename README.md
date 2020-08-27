# process_uptime
Obtain the uptime and start date of a Linux process in pure python  
python 2.6+ compatible 

## Example ##
### Single PID ###
```
$ python process_uptime.py 15918

PID: 15918
Uptime: 3 hours, 14 minutes
Start Date: Thu Aug 27 07:42:29 2020

```
### Multiple PIDs ###
```
$ python process_uptime.py 1217 17201 17202

PID: 1217
Uptime: 4 hours, 43 minutes
Start Date: Thu Jul 16 06:44:10 2020

PID: 17201
Uptime: 31 minutes, 46 seconds
Start Date: Wed Aug 26 10:55:25 2020

PID: 17202
Uptime: 31 minutes, 46 seconds
Start Date: Wed Aug 26 10:55:25 2020

```
