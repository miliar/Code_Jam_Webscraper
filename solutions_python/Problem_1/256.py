#! /usr/bin/python
import sys

cases = int(sys.stdin.readline()[:-1])
actual_case = 0

while actual_case < cases:
    actual_case += 1
    engines = int(sys.stdin.readline()[:-1])
    machines = {}
    switch = 0
    
    for i in range(engines):
        name = sys.stdin.readline()[:-1]
        machines[name] = 0
    
    number = int(sys.stdin.readline()[:-1])
    used = 0
    for i in range(number):
        name = sys.stdin.readline()[:-1]
        if machines[name] == 0:
            used += 1
            if used == engines:
                switch += 1
                for member in machines:
                    machines[member] = 0
                used = 1
            machines[name] = 1

    print "Case #%d: %d" %(actual_case,switch)
