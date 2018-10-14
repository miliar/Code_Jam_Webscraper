#!/usr/bin/env python

import sys

count = 0
cases = 0
current_case = 1
row = 0
possible = []
both = []
status = ""
for line in sys.stdin:
    if not count:
        cases = int(line)
    elif count % 5 == 1:
        row = int(line)
    if (count - 1) % 5 == row:
        if not possible:
            possible = line.split()
        else:
            for item in line.split():
                if item in possible:
                    both.append(item)
            if len(both) == 0:
                status = "Volunteer cheated!"
            elif len(both) == 1:
                status = str(both[0])
            else:
                status = "Bad magician!"
            print("Case #" + str(current_case) + ": " + status)
            possible = []
            both = []
            current_case += 1
            status = ""
    count += 1
