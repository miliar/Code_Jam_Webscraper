#!/usr/bin/python3.4
import time
from sys import stdin

def main():
    next(stdin)
    case_number = 1
    for line in stdin:
        line = int(line.rstrip('\n'))
        if line > 0:
            answer = last_tidy_number(line)
            print('Case #'+str(case_number)+': '+str(answer))
            case_number += 1

def last_tidy_number(number):
    string_number = str(number)
    length = len(string_number)

    if length == 1:
        return number

    for j in range(0, length-1):
        if int(string_number[j]) > int(string_number[j+1]):
            number = int(string_number[:j+1])-1
            number = str(number)+'9'*len(string_number[j+1:])
            return number.lstrip('0')
    return number
            


if __name__ == '__main__':
    #start = time.time()
    main()
    #print("Script took %.4f ms to run" %((time.time() - start)*1000)) # measure run time