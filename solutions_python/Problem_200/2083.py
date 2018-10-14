import sys
import numpy
import itertools
# print sys.maxsize
def num(N):
    if len(N)==1:
        return int(N)
    elif N=='10':
        return 9
    else:
        N=int(N)
        flag=1
        hld = list(str(N))
        while(flag==1):
        # for i in reversed(range(int(N) + 1)):
        #     N=int(N)

            # N=int(N)-1

            for j in range(len(hld) - 1):
                if hld[j]<=hld[j+1]:
                    if j+2==len(hld):
                        flag=0
                    else:
                        flag=1
                    # continue
                else:
                    hld[j]=str(int(hld[j])-1)
                    for jj in range(j+1,len(hld)):
                        hld[jj]='9'
                        # break
                    # flag=0
                    break

            # if flag==1:
        return int(''.join(hld))
                # break



f1 = open('B-large.in', 'r')
# print f1
T=f1.readline().strip()
print T
# M=f1.readline()
for t,line in enumerate(f1):
    N= line.strip()
    X=num(N)
    sys.stdout = open('tidy1.txt', 'a')
    print 'Case #%d: %d' % (t + 1,X)
    # print X

