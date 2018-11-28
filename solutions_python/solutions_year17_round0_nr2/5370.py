#!/usr/bin/env python
import sys
def analyse_data(dataInput):
    while check_if_tidy(dataInput) == False:
        dataInput = str(int(dataInput)-1)
    return dataInput

def check_if_tidy(dataInput):
    size = len(dataInput)-1
    if size == 0:
        return True

    for pos, ch in enumerate(dataInput):
        if pos<size:
            if ch <= dataInput[pos+1]:
                continue
            else:
                return False
        else:
            return True

    return False


def main():
    t = int(input())  # read a line with a single integer
    for i in range(1, t + 1):
        line = raw_input()
        dataOutput = analyse_data(line)
        #print "Analysing %s" % line
        print("Case #{}: {}".format(i, dataOutput))
        

if __name__ == "__main__":
    main()