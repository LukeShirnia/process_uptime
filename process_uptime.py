#!/usr/bin/env python
#
# Process uptime/start date calculation
# author: LukeShirnia
# https://github.com/LukeShirnia/process_uptime
#
import os
import sys
import time
from datetime import datetime


def readfile(filename):
    """ Return the whole contents of the given file
    """
    f = open(filename)
    ret = f.read().strip()
    f.close()
    return ret


def seconds2human(seconds, precision=6):
    """ Convert time in seconds to human-readable representation
    """
    intervals = [
        ("year", 31556952),  # 365.2425 days
        (
            "month",
            2629746,
        ),  # (365.2425 days / 12) - just using 30 days leaves ~5 days remainder
        ("week", 604800),
        ("day", 86400),
        ("hour", 3600),
        ("minute", 60),
        ("second", 1),
    ]
    result = []
    for unit, unit_length in intervals:
        unit_count, seconds = divmod(seconds, unit_length)
        if unit_count or result:
            if unit_count != 1:
                unit += "s"
            result.append("%s %s" % (unit_count, unit))
    return ", ".join(result[:precision])


def timedelta_total_seconds(timedelta):
    """ Returns a timedelta object in seconds

    timedelta.total_seconds() does not exist on python <= 2.6
    """
    return (
        timedelta.microseconds + 0.0 +
        (timedelta.seconds + timedelta.days * 24 * 3600) * 10 ** 6) / 10 ** 6


def get_process_uptime(PID):
    """ Returns timedelta object of a process' uptime
    """
    # CLK_TCK is normally 100 (Linux Kernel > 2.7),
    # but we don't make assumptions and obtain the exact value
    CLK_TCK = os.sysconf(os.sysconf_names["SC_CLK_TCK"])
    # Start time of process (in clock ticks) since system boot
    PROCESS_CLOCK_TICKS = readfile("/proc/{0}/stat".format(PID)).split()[21]
    # System uptime
    SYSTEM_UPTIME = readfile("/proc/uptime").split()[0]
    # Get the process uptime (since system boot) in JIFFS
    PROCESS_JIFFS = int(PROCESS_CLOCK_TICKS) / CLK_TCK
    # .timestamp() was introduced in python > 3.3 so we convert manually instead
    now = time.mktime(datetime.now().timetuple()) + datetime.now().microsecond / 1e6
    # Obtain timestamp of the process start time
    RAW_START_TIME = now - (int(float(SYSTEM_UPTIME) - PROCESS_JIFFS))
    # Convert start time to datetime object
    PROCESS_START_TIME = datetime.fromtimestamp(RAW_START_TIME)

    return datetime.now() - PROCESS_START_TIME


for item in sys.argv[1:]:
    try:
        print("")
        print("PID: {0}".format(item))
        UPTIME = get_process_uptime(item)
        print("Uptime: {0}".format(seconds2human(timedelta_total_seconds(UPTIME))))
        print("Start Date: {0}".format((datetime.now() - UPTIME).strftime("%c")))
    except Exception as ex:
        print("Error with pid {0}".format(ex))

print("")
