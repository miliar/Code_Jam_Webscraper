import sys

f = open('B-small.in')
f_out = open('B-small.out', 'w')

T = int(f.readline())
for k in range(T):
    line = f.readline().split()
    N = int(line[0])
    V = float(line[1])
    X = float(line[2])
    R = list()
    C = list()
    for i in range(N):
        line = f.readline().split()
        R.append(float(line[0]))
        C.append(float(line[1]))
    if N==1:
        if C[0]!=X:
            f_out.write('Case #{0}: IMPOSSIBLE\n'.format(k+1))
        else:
            f_out.write('Case #{0}: {1}\n'.format(k+1, V/R[0]))
    else: #N==2 in small test cases
        if C[0]>C[1]:
            C.reverse()
            R.reverse()
        if C[0]==C[1]==X:
            f_out.write('Case #{0}: {1}\n'.format(k+1, V/(sum(R))))
        elif C[0]==X:
            f_out.write('Case #{0}: {1}\n'.format(k+1, V/R[0]))
        elif C[1]==X:
            f_out.write('Case #{0}: {1}\n'.format(k+1, V/R[1]))
        elif C[0]<X and C[1]>X:
            V0 = V*(C[1]-X)/(C[1]-C[0])
            V1 = V-V0
            f_out.write('Case #{0}: {1}\n'.format(k+1, max(V0/R[0], V1/R[1])))
        else:
            f_out.write('Case #{0}: IMPOSSIBLE\n'.format(k+1))

f.close()
f_out.close()
