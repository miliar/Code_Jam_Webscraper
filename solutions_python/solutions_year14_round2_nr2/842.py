#!/usr/bin/python
import sys

def compute(a, b, k):
    win_count = 0
    for i in range(a):
        for j in range(b):
            #print ' i ',i,' j ',j ,' i&j ',i&j
            val = i&j
            #print 'val', val, 'k', k
            if int(val) < int(k):
                win_count+=1
    return win_count

def main():
    if len(sys.argv) > 1:
        print 'Input file name : ',str(sys.argv[1])
        _input_file = sys.argv[1]
    else:
        _input_file = 'input.txt'

    fi = open(_input_file,'Ur')
    no_testcases = int(fi.readline().rstrip('\n'))

    result = ''
    for t in range(no_testcases):
        # read data for testcase
        # int(fi.readline())
        a, b, k = map(int, fi.readline().split(' '))
        print a,b,k

        res = compute(a, b, k)
        print 'result ', res

        #compute the result

        # store the result
        result += "Case #"+str(t+1)+": "+ str(res) + "\n"


    fh = open('output.txt','w')
    fh.write(result)
    fh.close()
    return

main()