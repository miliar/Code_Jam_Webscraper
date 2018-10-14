import sys
import numpy as np

def make_ints(l):
    return [int(i) for i in l.split(' ')]

def merge(s1, s2):
    m = min(len(s1), len(s2))
    return "".join(x+y for (x,y) in zip(s1,s2))+s1[m:]+s2[m:]

def solve_simple(R,B,Y):
    if min([R,B,Y]) < 0:
        return "IMPOSSIBLE"
    a,b,c = sorted([(R,"R"),(B,"B"),(Y,"Y")])
    if c[0] > a[0]+b[0]:
        return "IMPOSSIBLE"
    x = merge(c[1]*c[0], b[1]*b[0])
    x = merge(a[1]*a[0], x[::-1])
    return x

def find_first_and_replace(s, what, s2):
    i = s.find(what)
    s = s[:i+1] + s2 + s[i+1:]
    return s

def solve_case(N,R,O,Y,G,B,V):
    if B>R+Y+O:
        return "IMPOSSIBLE"
    if R>B+Y+G:
        return "IMPOSSIBLE"
    if Y>B+R+V:
        return "IMPOSSIBLE"
    ans = solve_simple(R-G,B-O,Y-V)
    if ans=="IMPOSSIBLE":
        return "IMPOSSIBLE"
    if O:
        ans = find_first_and_replace(ans, "B", ("OB"*O))
    if G:
        ans = find_first_and_replace(ans, "R", ("GR"*G))
    if V:
        ans = find_first_and_replace(ans, "Y", ("VY"*V))
    return ans

def check_ans(ans,**kwargs):
    from collections import Counter
    if ans=="IMPOSSIBLE":
        return
    cnt = Counter(ans)
    for key in kwargs:
        if kwargs[key]!=cnt.get(key,0):
            #print "Failed"
            return
    good_colors = {"B":"RYO","R":"BYG","Y":"BRV"}
    for i,j in zip(ans, ans[1:]+ans[0]):
        if (not (i in good_colors and j in good_colors[i])) and (not(j in good_colors and i in good_colors[j])):
            #print "Failed"
            return -1
    #print "Correct"

def main():
    infile = sys.argv[1]
    inp = file(infile,"rb").read()
    lines = inp.splitlines()
    T = int(lines[0])
    lines = lines[1:]
    for case_num, line in enumerate(lines):
        N,R,O,Y,G,B,V = make_ints(line)
        ans = solve_case(N,R,O,Y,G,B,V)
        bla = check_ans(ans,R=R,O=O,Y=Y,G=G,B=B,V=V)
        if bla==-1:
            ans = "IMPOSSIBLE"
        print "Case #%d: %s"%(case_num+1,ans)

if __name__ == "__main__":
    main()