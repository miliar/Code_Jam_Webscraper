def omino(X, R, C):
    if X >= 7:
        return 'RICHARD'
    elif X > max(R, C):
        return 'RICHARD'
    elif (X+1)/2 > min(R, C):
        return 'RICHARD'
    elif (R*C)%X != 0:
        return 'RICHARD'
    elif ((2*X >= (R*C)) and X>3):
        return 'RICHARD'
    else:
        return 'GABRIEL'


fin = open('D-small-attempt2.in','r')
fout = open('output.txt','w')

T = int(fin.readline())
print T

for i in range(T):
    temp = fin.readline().split(' ')
    ans = omino(int(temp[0]), int(temp[1]), int(temp[2]))
    fout.write("Case #%d: %s\n"%(i+1, ans))

fin.close()
fout.close()