def solve(N):
    if len(N) == 1:
        return N
    else:
        flag = 0
        num_max = 0
        num_min = int(N[0])    
        for idx,c in enumerate(N):
            if num_max < int(c):
                num_max = int(c)
            elif num_max > int(c) and num_max > num_min:
                flag = 1
                ans = N[0] + str(int(N[idx-1])-1) + '9'*(len(N)-idx)
            elif num_max > int(c) and num_max == num_min:
                flag = 1
                if num_min == 1:
                    ans = '9'*(len(N)-1)
                else:
                    ans = str(int(N[0])-1) + '9'*(len(N)-1)
    if flag == 0:
        return N
    return ans

f = open("./B-small-attempt1.in",'r')
w = open("./B-small-attempt1.out",'w')
# f = open("./A-large.in",'r')
# w = open("./A-large.out",'w')
numcases = int(f.readline())
for casenum in range(1,numcases+1):
    N = f.readline().strip()
#     print('Case #' + repr(casenum) + ': ' + solve(N))
    w.write('Case #' + repr(casenum) + ': ' + solve(N) + '\n')

f.close()
w.close()