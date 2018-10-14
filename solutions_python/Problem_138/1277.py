import copy

infile = 'D-large.in'
outfile = 'Dlarge-out.txt'

f = open(infile, 'r')
out = open(outfile, 'w')
T = int(f.readline())

for m in range(T):

    N = int(f.readline())
    A = sorted(map(float, f.readline().split()))
    B = sorted(map(float, f.readline().split()))
    AA = copy.deepcopy(A)
    BB = copy.deepcopy(B)

    A.reverse()

    a = 0
    for i,j in enumerate(A):
        if(B[-1]>j):
            B.pop()
        else:
            a+=1
            B = B[1:]
    print a

    A = AA
    B = BB

    x = 0
    for i,j in enumerate(A):
        if(B[0]<j):
            B = B[1:]
            x+=1
        else:
            B.pop()
    print x

    out.write('Case #'+str(m+1)+': ')

    out.write(str(x)+' '+str(a))

    out.write('\n')

out.close()
