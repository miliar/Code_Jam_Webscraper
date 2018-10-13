f=open('C-small-2-attempt0.in')
out=open('output.txt','w')
T=int(f.readline())
for i in range(T):
    out.write('Case #'+str(i+1)+': ')
    temp=f.readline().split()
    N=[[0,0]]
    N.append([int(temp[0]),1])
    N.sort(reverse=True)
    K=int(temp[1])
    #if K>(N[0][0]/2):
    #    out.write('0 0\n')
    #    continue
    while K>0:
        if N[0][1]>=K:
            if N[0][0] % 2 == 0:
                m1 = int(N[0][0] / 2)
                m2 = m1 - 1
                if m1 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m1 == N[j][0]:
                            N[j][1] = N[j][1] + K
                            find = 1
                    if find == 0:
                        N.append([m1, K])
                if m2 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m2 == N[j][0]:
                            N[j][1] = N[j][1] + K
                            find = 1
                    if find == 0:
                        N.append([m2, K])
            else:
                m1 = int((N[0][0] - 1) / 2)
                m2 = m1
                if m1 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m1 == N[j][0]:
                            N[j][1] = N[j][1] + K*2
                            find = 1
                    if find == 0:
                        N.append([m1, K*2])
            K = 0
            N[0][1] = N[0][1] - K
            if N[0][1] == 0:
                del N[0]
            N.sort(reverse=True)
        else:
            if N[0][0] % 2 == 0:
                m1 = int(N[0][0] / 2)
                m2 = m1 - 1
                if m1 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m1 == N[j][0]:
                            N[j][1] = N[j][1] + N[0][1]
                            find = 1
                    if find == 0:
                        N.append([m1, N[0][1]])
                if m2 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m2 == N[j][0]:
                            N[j][1] = N[j][1] + N[0][1]
                            find = 1
                    if find == 0:
                        N.append([m2, N[0][1]])
            else:
                m1 = int((N[0][0] - 1) / 2)
                m2 = m1
                if m1 != 0:
                    find = 0
                    for j in range(len(N)):
                        if m1 == N[j][0]:
                            N[j][1] = N[j][1] + N[0][1]*2
                            find = 1
                    if find == 0:
                        N.append([m1, N[0][1]*2])
            K = K - N[0][1]
            N[0][1] = N[0][1] - N[0][1]
            if N[0][1] == 0:
                del N[0]
            N.sort(reverse=True)
    out.write(str(m1)+' '+str(m2)+'\n')
f.close()
out.close()
