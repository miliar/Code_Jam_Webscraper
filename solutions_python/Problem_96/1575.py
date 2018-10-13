import sys,math
temp=sys.stdin
def solve(t):
    n,s,p,tr=t[0],t[1],t[2],t[3:]
    os,ss=0,0
    for i in tr:
        r=i%3
        d=int(math.ceil(i/3))
        if d>=p:
            os+=1
        elif p-d==1 and r!=1 and p-2>=0:
            ss+=1
    return os+min(ss,s)

testcase = open('b-large.in','r')
sys.stdin = testcase
solution = open('b-large.out','w')
t = int(input())
for i in range(t):
    T=[int(j) for j in input().split()]
    print('Case #' + str(i+1) + ': ' + str(solve(T)),file=solution)
solution.close()
testcase.close()
sys.stdin=temp
