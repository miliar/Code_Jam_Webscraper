import os
import sys

def runcase(line):
    numbers = line.split(' ')
    n = int(numbers[0])
    pd = int(numbers[1])
    pg = int(numbers[2])

    if pg == 100 and pd < 100:
        return "Broken"
    
    if pg == 0 and pd > 0:
        return "Broken"

    for d in range(1, n+1):
        if (d * pd) % 100 != 0:
            continue

        return "Possible"

    return "Broken"        
    
def run():
    count = int(sys.stdin.readline().strip())
    for i in range(0,count):
        print('Case #%d: %s' % (i+1,runcase(sys.stdin.readline().strip())))

run()
