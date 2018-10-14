#!/usr/bin/python
import sys
import re


k="""
(0.2 furry
  (0.81 fast
    (0.3)
    (0.2)
  )
  (0.1 fishy
    (0.3 freshwater
      (0.01)
      (0.01)
    )
    (0.1)
  )
)
"""

rw = re.compile('\(\s*(\d+(\.\d*)?)\s*\)', re.DOTALL|re.MULTILINE)

def parse(s):
    tree = {}
    t = s.strip()[1:-1].strip()
    a = re.compile("(\d+(\.\d*)?)\s+([a-z]+)(.*)", re.DOTALL|re.MULTILINE)
    t2 = a.match(t).groups()
    return t2[0], t2[2], t2[3].strip()

def twoparts(s):
    s.strip()
    t = 0
    for i in xrange(0, len(s)):
        if s[i] == '(':
            t+=1
        elif s[i] == ')':
            t-=1
        if t == 0:
            return s[:i+1].strip(), s[i+1:].strip()

def store(s):
    tree = {}

    if rw.match(s):
        tree["weight"] = float(rw.match(s).groups()[0])
        tree["name"] = "Sdafkausdfasodfhasiu"
        tree["left"] = 1
        tree["right"]=1
        return tree
    
    t = parse(s)
    weight = float(t[0])
    name = t[1]
    rest = t[2]

    both = twoparts(rest)
    # print "both", both

    if rw.match(both[0]):
        left = float(rw.match(both[0]).groups()[0])
    else:
        left = store(both[0]) 

    if rw.match(both[1]):
        right = float(rw.match(both[1]).groups()[0])
    else:
        right = store(both[1]) 

    
    tree["name"] = name
    tree["weight"] = weight
    tree["left"] = left
    tree["right"] = right
    return tree

def run(s,d):
    a = s.split()
    name = a[0]
    count = int(a[1])
    ps = a[2:]
    # print name, count, ps
    return __run(ps, d, 1)

def __run(names, d, value):
    value *= d["weight"]
    if d["name"] in names:
        t = d["left"]
    else:
        t = d["right"]
    try:
        t.keys()
        # print "__run", names, t, value
        return __run(names, t, value)
    except AttributeError:
        # print value, t
        return value * t


def ReadInts():
    return map(int, sys.stdin.readline().strip().split())

num_cases = ReadInts()[0]
for i in xrange(1, 1+num_cases):
    num_lines = ReadInts()[0]
    d_s = ""
    for _ in xrange(num_lines):
        d_s += sys.stdin.readline()

    print "Case #%d:" % i

# print d_s
    d=store(d_s)
    # print d

        
    num_lines = ReadInts()[0]
    for _ in xrange(num_lines):
        test_s = sys.stdin.readline()
        print "%.7f" % run(test_s, d)
    
