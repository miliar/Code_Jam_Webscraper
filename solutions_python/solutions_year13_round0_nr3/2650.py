import sys
import math

def palindrome(number):
    if len(number) == 1:
        return True
    start = 0
    end = len(number)-1
    while(start < end):
        if number[start] != number[end]:
            return False
        start += 1
        end -= 1
    return True

if __name__=='__main__':
    fileName = sys.argv[1]
    with open(fileName+'.output','w') as fw:
        with open(fileName,'r') as fh:
            cases = int(fh.readline())
            for t in xrange(cases):
                start,end = fh.readline().rstrip().split()
                n = int(start)
                end = int(end)
                count = 0
                while(n<=end):
                    nsqrt = math.sqrt(n) 
                    if nsqrt == int(nsqrt):
                        if palindrome(str(n)) and palindrome(str(int(nsqrt))):
                            count +=1
                    n+=1
                fw.write('Case #{0}: {1}\n'.format(t+1,count))

