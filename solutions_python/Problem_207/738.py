import sys
sys.stdin = open("input2.in","r")
sys.stdout = open("output2.out","w")
def from_last_first_non_zero(line,c):
    i=5
    while i>=0:
        if line[i][0] !=0 and line[i][1][len(line[i][1])-1]!=c:
            ret = [line[i][1][len(line[i][1])-1],0]
            line[i][0]-=1
            return ret;
        i-=1
    return ['x',-1]
def first_non_zero(line,c):    
    i=0
    while i<=5:
        if line[i][0] !=0 and line[i][1][len(line[i][1])-1]!=c:
            ret = [line[i][1][len(line[i][1])-1],0]
            line[i][0]-=1
            return ret;
        i+=1
    return ['x',-1]

test = int(raw_input())
for t in range(test):
    
    N,R,O,Y,G,B,V = map(int,raw_input().split())
    line = [] 
    line += [[R,'R']]
    line += [[O,'O']]
    line += [[Y,'Y']]
    line += [[G,'G']]
    line += [[B,'B']]
    line += [[V,'V']]
    line.sort()
    line[0][1] = 'Z' + line[0][1]
    line[1][1] = 'ZZ' + line[1][1]
    line[2][1] = 'ZZZ' + line[2][1]
    line[3][1] = 'ZZZZ' + line[3][1] 
    line[4][1] = 'ZZZZZ' + line[4][1] 
    line[5][1] = 'ZZZZZZ' + line[5][1] 
    
    pat = 'X'
    res= [0,0]
    while res[1]!=-1:
    
        line.sort()
        res = from_last_first_non_zero(line,pat[len(pat)-1]);
        if res[1] == -1:
            ''''''
        else:
            pat += res[0]
            #print res
        
        res = first_non_zero(line,pat[len(pat)-1])
        if res[1] == -1:
            ''''''
        else:
            pat += res[0]
            #print res
        #print "t"
    flag=1
    pat = pat[1:]
    for i in range(len(pat)-1):
        if pat[i]==pat[i+1]:
            print "Case #"+str(t+1)+": IMPOSSIBLE"
            flag=0
            break
            
    if flag==1:
        if pat[0] != pat[len(pat)-1]:
            print "Case #"+str(t+1)+": "+pat
        else:
            print "Case #"+str(t+1)+": IMPOSSIBLE"

