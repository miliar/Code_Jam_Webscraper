  # input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.

import sys
from math import pi



f_dir = sys.argv[1]
fo_dir = sys.argv[2]

f = open(f_dir,'r')
fo = open(fo_dir,'w')

def solve(N,K,ps):
    ans = []
    ps.sort(key=lambda x:x[0],reverse = True)
    look = ps[:len(ps)-K+1]
    for i,x in enumerate(look):
        # print("picked: ",x)
        ans.append(cal(x[0],x[1],K,ps[i+1:]))
    # print(max(ans))
    return max(ans)

def cal(R,H,K,ps):
    ps.sort(key=lambda x:x[1]*x[0],reverse = True)
    # print("And also: ",ps[:K-1])
    # print(ps,K)
    rh = sum(x[0]*x[1] for x in ps[:K-1]) if K!=1 else 0
    return pi*(2*(rh+R*H)+R*R)


t = int(f.readline())  # read a line with a single integer
test = []
count = 0
while count!=t:
  # n, m = [int(s) for s in f.readline().split(" ")]  # read a list of integers, 2 in this case
  # print("Case #{}: {} {}".format(i, n + m, n * m))
  # check out .format's specification for more formatting options
    # print(f.readline())
    s = f.readline().split()
    # print(s)
    N,K = int(s[0]),int(s[1])
    pancakes = []
    for i in range(N):
        pancakes.append([int(x) for x in f.readline()[:-1].split()])
    # print (N,K,pancakes)
    ans = solve(N,K,pancakes)
    fo.write("Case #"+str(count+1)+": %.9f\n"%ans)
    count+=1

f.close()

# for A in test:
#     # for row in A:
#     #     print(row)
#     parse=[]
#     for i in range(len(A)):
#         for j in range(len(A[i])):
#             if A[i][j]!='?' and A[i][j] not in parse:
#                 parse.append(A[i][j])
#                 greedy((i,j),A,A[i][j])


# for i in range(1,len(test)+1):
#     fo.write("Case #"+str(i)+':\n')
#     for row in test[i-1]:
#         fo.write(''.join(row)+'\n')

fo.close()