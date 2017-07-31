#!/usr/bin/env python
logfile = open("honeynet_Feb.log", "r")
for line in logfile:
    line_split = line.split()
    print line_split
    list = line_split[5], line_split[6], line_split[12]
    print list
