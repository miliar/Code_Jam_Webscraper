#! /usr/bin/python
import sys

def next_number(number):
    strnum = list(str(number))
    for i in range(len(strnum) - 1):
        if strnum[-1-i] <= strnum[-2-i]:
            continue
        else:
            c = strnum[-2-i]
            strtail = strnum[-1-i:]
            restmin = min([letter for letter in strtail if letter > c])
            restmin_index = strnum.index(restmin, -1-i)
            strnum[-2-i] = strnum[restmin_index]
            strnum[restmin_index] = c
            strtail = strnum[-1-i:]
            strtail.sort()
            next_str = strnum[0:-1-i] + strtail
            return int(''.join(next_str))
        
    length = len(strnum)
    zeros = strnum.count('0')
    strnum.sort()
    strnum = list(str(int(''.join(strnum))))
    for c in range(zeros + 1):
        strnum.insert(1, '0')
    return int(''.join(strnum))

if __name__ == "__main__":
    input_file = sys.argv[1]
    ifile = open(input_file)
    case_count = int(ifile.readline().strip())
    for i in range(case_count):
        number = int(ifile.readline().strip())
        result = next_number(number)
        print "Case #%d: %d" % (i+1, result)