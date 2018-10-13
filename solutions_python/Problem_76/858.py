#!/usr/bin/env python

# Getting file descriptors

f = open('input-3.in', 'r')     # Replace with appropriate file name
s = open('outputfile', 'w')


# Defining functions

def dec2bin(x):
    x = int(x)
    if x == 1:
        return str(1)
    elif x == 0:
        return str(0)
    else:
        return str(dec2bin(x/2))+str(x%2)

def add_bin(x,y):
    if len(x) == 0:
        return ''
    elif (x[0] == '1' and y[0] == '1') or (x[0] == '0' and y[0] == '0'):
        return '0' + add_bin(x[1:],y[1:])
    elif (x[0] == '1' and y[0] == '0') or (x[0] == '0' and y[0] == '1'):
        return '1' + add_bin(x[1:],y[1:])

def patrick_add(x,y):
    a = dec2bin(x)[::-1]
    b = dec2bin(y)[::-1]
    if len(a)<len(b):
        a = a + (len(b)-len(a))*'0'
    elif len(b)<len(a):
        b = b + (len(a)-len(b))*'0'
    
    c = add_bin(a,b)
    
    return int(c[::-1],2)

def patrick_sum(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return patrick_add(lst[0],patrick_sum(lst[1:]))

def find_osplit(pile):
    sean_pile = pile
    pat_pile = [0]
    while 1:
        pat_pile.append(sean_pile.pop())
        if len(sean_pile) == 0:
            return 'NO'
        if patrick_sum(sean_pile) == patrick_sum(pat_pile):
            if sum(pat_pile) != 0:
                break       
    return sum(sean_pile)
    
def process(line):
    line = line.rstrip()
    bag = line.split()
    bag = map(int,bag)
    bag.sort()
    return find_osplit(bag[::-1])



# Getting input and processing

LineNum = 0

for line in f:
    if LineNum == 0:
        NumCases = int(line)
        LineNum += 1
    elif LineNum % 2 == 0:
        s.write("Case #%d: %s\n"%(LineNum/2,process(line)))
        LineNum += 1
    else:
        LineNum += 1

# Closing files

f.close()
s.close()