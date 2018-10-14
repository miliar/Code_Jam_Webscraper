#!/bin/python

def readint(): return int(raw_input())

def readints(): return [ int(x) for x in raw_input().split() ]

def padding(table,t):
    return [line+["."]*(t-len(line)) for line in table]

def rightskew(table,t):
    return [ ["."]*i + line + ["."]*(t-i) for i,line in enumerate(table) ]

def leftskew(table,t):
    return [ ["."]*(t-i) + line + ["."]*i for i,line in enumerate(table) ]

def solve(table,t,k):
    ret = []
    ret += judgetable( zip(*leftskew(padding(table,t),t)) ,k)
    ret += judgetable( zip(*rightskew(padding(table,t),t)) ,k)
    ret += judgetable(zip(*padding(table,k)),k)
    ret += judgetable(table,k)
    return set(ret)

def makeanswer(answer):
    if "R" in answer and "B" in answer:
        return "Both"
    elif "R" in answer:
        return "Red"
    elif "B" in answer:
        return "Blue"
    return "Neither"

def drop(table):
    return [ [ i for i in reversed(row) if i != "." ] for row in table ]

def judgetable(table,k):
    return sum([ judge(row,k) for row in table ],[])

def judge(line,k):
    lined = []
    prev = "."
    count = 0
    for x in line:
        if prev == x:
            count += 1
        else:
            if count >= k:
                lined.append(prev)
            count = 1
        prev = x
    if count >= k:
        lined.append(prev)
    return lined

def printtable(table):
    for x in table:
        print x

if __name__ == "__main__":
    nt = readint()
    for i in range(nt):
        t,k = tuple(readints())
        table = [ raw_input() for _ in range(t) ]
        print "Case #%d: %s" % ( i+1, makeanswer(solve(drop(table),t,k)))
