#https://code.google.com/codejam/contest/dashboard?c=3264486#s=p0
import os
import math
import cProfile

flipd={"+":"-", "-":"+"}

# not used - transformed to map , kept for legacy
def flip(str):
    return flipd[str]

# not used - transformed to map , kept for legacy
def flipstr(str):      # for char in srt, flip + to - and - to +
    newstring=""
    for s in str:
        newstring+=flip(s)
    return newstring

# not used - transformed to map , kept for legacy
def flipstr2(str):      # for char in srt, flip + to - and - to +
    newstring=""
    for s in str:
        if s=="-":
            newstring+="+"
        else:
            newstring+="-"
    return newstring

def loop(items):
    S=items[0]
    K=int(items[1])   
    flips=0                         # return # flips

    for s in range(len(S)):         # itr through inp str
        if S[s]=="-":               # if it finds a -, flip 
            length=len(S[s:])       # chars left to iterate through
            if length>=K:           # enough pancakes to flip
                beg=S[:s]
                newL=map(lambda x: flipd[x],S[s:s+K])    # flip starting with -, K chars
                new=''.join(newL)
                #new2=map(flip,S[s:s+K])
                #new3=flipstr(S[s:s+K])  
                end=S[s+K:]
                S=beg+new+end
                flips+=1
            else:
                return "IMPOSSIBLE" # end of string, not enough pancakes to flip
    return flips
               
def start():
    file="A-large"                     
    with open(file+'.out', 'wt') as outfile:
        with open(file+".in") as infile:
            T=int(next(infile))
            for t in range(1, T+1):
                items=next(infile).split()
                out = loop(items)
                casestr="Case #%s: %s\n" % (t,out)
                #casestr="Case #%s: %s %s\n" % (case,out[0],out[1])
                print(casestr)
                outfile.write(casestr)
                
start()
#print(loop(["---+-++----", 3]))
#cProfile.run("loop([1000000,1000000])")