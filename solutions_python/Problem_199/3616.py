def solve(S,K):
    Snew = S
    count = 0
    flag = 0
    res = 0
    for i in range(len(S)):
        if Snew[i] == '-' and (i+K)<=len(S):
            for j in range(K):
                if Snew[i+j] == '-':
                    Snew[i+j] = '+'
                else:
                    Snew[i+j] = '-'
            res += 1
        elif Snew[i] == '-':
            return 'IMPOSSIBLE'
    return str(res)

# In[45]:

# f = open("./A-small-attempt3.in",'r')
# w = open("./A-small-attempt3.out",'w')
f = open("./A-large.in",'r')
w = open("./A-large.out",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    S,K = f.readline().strip().split(" ")
    K = int(K)
    S = list(S)
#     print('Case #' + repr(casenum) + ': ' + solve(S,K))
    w.write('Case #' + repr(casenum) + ': ' + solve(S,K) + '\n')

f.close()
w.close()