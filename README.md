# process_uptime
Obtain the uptime and start date of a Linux process in pure python

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
$ python process_uptime.py 15918 15926 15928

PID: 15918
Uptime: 3 hours, 15 minutes
Start Date: Thu Aug 27 07:42:29 2020

PID: 15926
Uptime: 3 hours, 15 minutes
Start Date: Thu Aug 27 07:42:29 2020

PID: 15928
Uptime: 3 hours, 15 minutes
Start Date: Thu Aug 27 07:42:29 2020

```
