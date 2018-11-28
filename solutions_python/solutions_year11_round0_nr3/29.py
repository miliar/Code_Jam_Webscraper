#!/usr/bin/env python

def xsum(list):
    result = 0 
    for i in list:
        result = result^i
    return result


if __name__ == '__main__':
    f = open('input')
    a = int( f.readline() )
    for i in range(a):
        f.readline()
        list = map(int,f.readline().split())
        if xsum(list) != 0:
            result="NO"
        else:
            result = sum(list) - min(list)
        print "Case #"+str(i+1)+":", result
