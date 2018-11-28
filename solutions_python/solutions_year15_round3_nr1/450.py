import sys
sys.stdin = open("in.txt","r")
#sys.stdout = open("out.txt","w")
tests = int(raw_input())
for t in range(1,tests+1):
    r,c,w = map(int,raw_input().split())
    first = c/w
    if c - (c/w-1)*w <=w:
        ans = r*(first+w-1)
    else: ans = r*(first+w)
    print "Case #"+str(t)+':',ans
    
#sys.stdout.close()
