#!/usr/bin/python

f=open('pancake_small.in', 'r')
output=open('pancake_small.out', 'w')
#f=open('pancake2.in', 'r')
#output=open('pancake2.out', 'w')
#f=open('pancake3.in', 'r')
#output=open('pancake3.out', 'w')

cases=int(f.readline())

def of_list(l): return ''.join(l)

def complete(s):
    return not ('-' in s)

def any_complete(l):
    return True in [complete(s) for s in l]

def flip(c):
    if c == '+': return '-'
    elif c == '-': return '+'
    else: raise ValueError

def flip_some(x, k, i):
    l=list(x)
    ret=[]
    for j in range(len(l)):
        if j >= i and j < i+k:
            ret.append(flip(l[j]))
        else:
            ret.append(l[j])
    return of_list(ret)

def list_to_str_for_testing(l):
    return [of_list(x) for x in l]

def pancake(original, k, case):
    used=set([original])
    current=set([original])
    n=len(list(original))
    # print ""
    # print "starting with: %s" % of_list(original)
    for i in range(5 * n):
        #  if i < 10 and case == 6:
        #      print i
        #      print "current: %s" % str(list_to_str_for_testing(current))
        #      print "used: %s" % str(list_to_str_for_testing(used))
        #      print "current: %i" % len(current)
        #      print "used: %i" % len(used)
        if any_complete(current): return i
        next_curr=set([])
        for x in current:
            for j in range(n - k + 1):
                y=flip_some(x,k,j)
                if not y in used:
                    next_curr.add(y)
        used=used.union(next_curr)
        current=next_curr
        if len(current) == 0: return "IMPOSSIBLE"
    return "IMPOSSIBLE"
        
for case in range(cases):
    s=f.readline().replace("\n","").split(' ')
    original=s[0]
    k=int(s[1])
    value=pancake(original, k, case)
    # print value
    output.write ("Case #%i: %s\n" % (case+1, str(value)))
