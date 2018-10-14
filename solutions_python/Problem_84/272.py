import os
import sys

def rl():
    return sys.stdin.readline().strip()

def runcase():
    nums = rl()
    height = int(nums.split(' ')[0])
    pic = []
    for i in range(0, height):
        pic.append(list(rl()))

    for row in range(0, len(pic)):
        for col in range(0, len(pic[0])):
            if pic[row][col] == '#':
                if row == len(pic) - 1:
                    return "Impossible"

                if col == len(pic[0]) - 1:
                    return "Impossible"
                    
                if pic[row + 1][col] != '#' or \
                   pic[row][col + 1] != '#' or \
                   pic[row + 1][col + 1] != '#':
                    return "Impossible"

                pic[row][col] = "/"
                pic[row][col + 1] = "\\"
                pic[row + 1][col] = "\\"
                pic[row + 1][col + 1] = "/"

    return '\n'.join([''.join(x) for x in pic])
    
    
def run():
    count = int(sys.stdin.readline().strip())
    for i in range(0,count):
        print('Case #%d:\n%s' % (i+1,runcase()))

run()
