#!/usr/bin/env python
import sys
f=sys.stdin
def base10toN(num,n):
    """Change a  to a base-n number.
    Up to base-36 is supported without special notation."""
    num_rep={10:'a',
         11:'b',
         12:'c',
         13:'d',
         14:'e',
         15:'f',
         16:'g',
         17:'h',
         18:'i',
         19:'j',
         20:'k',
         21:'l',
         22:'m',
         23:'n',
         24:'o',
         25:'p',
         26:'q',
         27:'r',
         28:'s',
         29:'t',
         30:'u',
         31:'v',
         32:'w',
         33:'x',
         34:'y',
         35:'z'}
    new_num_string=''
    current=num
    while current!=0:
        remainder=current%n
        if 36>remainder>9:
            remainder_string=num_rep[remainder]
        elif remainder>=36:
            remainder_string='('+str(remainder)+')'
        else:
            remainder_string=str(remainder)
        new_num_string=remainder_string+new_num_string
        current=current/n
    return new_num_string

def memorise(f):
    mem = {}
    def inner(*args):
        if args not in mem:
            mem[args] = f(*args)
        return mem[args]
    return inner

@memorise
def ishappy(n,b):
    seen=set()
    n=base10toN(n,b) 
    while True:
        if n == '1': return True
        if n in seen: return False
        seen.add(n)
        n=base10toN(sum(int(x)*int(x) for x in n),b)

      


def test(bases):
    n=2
    while True:
        happy=True
        for b in bases:
            if not ishappy(n,b):
                happy=False
                break
        if happy: break
        n+=1
    return n

if __name__=='__main__':
    T=int(f.next())
    for i in range(1,T+1):
        bases=map(int,f.next().split())
        print "Case #%s: %s"%(i,test(bases))

