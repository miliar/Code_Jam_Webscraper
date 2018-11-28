#-*- coding:utf-8 -*-
#!/usr/bin/env/python
def readInt(): return int(raw_input())
def readArray(num_):
    result = []
    for i in xrange(num_):
        result.append(raw_input())
    return result
def readLineArray(func_): return map(func_,raw_input().split())

def gcd(x_,y_):
    while y_:
        x_,y_ = y_,x_ % y_
    return x_
def gcdListDiff(x_):
    result = 0
    size = len(x_)
    x_.sort(reverse=True)
    for i in xrange(size-1):
        for j in xrange(i+1,size):
            result = gcd(result,x_[i]-x_[j])
    return result
def process(times_):
    divisor = gcdListDiff(times_)
    remainder = times_[0]%divisor
    result = 0
    if (remainder!=0) and (divisor !=1):
        result = divisor - remainder
    return result
def main():    
    C = readInt()
    for i in xrange(C):
        times = readLineArray(int)[1:]
        print "Case #%d: %d" %(i+1,process(times))

if __name__ == '__main__':
    main()
