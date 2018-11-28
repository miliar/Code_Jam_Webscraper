#!/bin/python
import re;

def IsPR(s) :
    length = len(s);
    if (length == 1) :
        return True;
    if (length % 2 == 0):
        return False;
    front = s[0:length/2];
    end = s[length/2 + 1: length][::-1];
    return front == end;
        
def NextPR(k):
    s = str(k);
    length = len(s);
    if (length != 2 and length % 2 == 0):
        return int('1' + '0' * (length - 1) + '1');
    elif (length == 1):
        return k;
    elif (length == 2):
        half = int(s[0]);
        ret = str(half) * 2;
        if int(ret) < k:
            half += 1;
            ret = str(half) * 2;
        return int(ret);
    else :
        half = int(s[0:length/2]);
        mid = int(s[length/2]);
        
        ret = str(half) + str(mid) + str(half)[::-1];
        if int(ret) < k:
            if mid == 9:
                mid = 0;
                half += 1;
            else :
                mid += 1;
            ret = str(half) + str(mid) + str(half)[::-1];
        return int(ret);
        
def Calc(a, b):
    init = int(a**(0.5));
    term = int(b**(0.5));
    i = NextPR(init);
    total = 0;
    while i <= term:
        n = i**2;
        if IsPR(str(n)) and n >= a and n <= b:
            total += 1;
            # print n;
        i = NextPR(i+1);
        n = NextPR(n+1);
        if (i**2 < n) :
            i == int(n**(0.5));
    return total;
        
numTest = int(input());

for t in range(0,numTest):
    test = raw_input();
    testg = re.match("([0-9]*) ([0-9]*)",test);
    A = int(testg.group(1));
    B = int(testg.group(2));
    nCase = Calc(A, B);
    print "Case #%d: %d" % (t + 1, nCase);
    