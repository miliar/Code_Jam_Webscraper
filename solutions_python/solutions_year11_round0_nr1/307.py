
def solve(N):
    B = [1,0,0]
    O = [1,0,0]
    for (color, pos) in N:
        if color == 'O':
            update(O, B, pos)
        else:
            update(B, O, pos)
    return B[1] + O[1]

def update(robot, tRobot, pos):
    rPos = robot[0]
    time = abs(pos-rPos)    
    if time<=tRobot[2]:
        time = 1
    else:
        time = time-tRobot[2]+1;
    tRobot[2]=0    
    robot[0] = pos
    robot[1] = robot[1] + time
    robot[2] = robot[2] + time
    

input_file = 'A-large.in'
output_file = 'result.dat'
fin=open(input_file , 'r')
fout=open(output_file, 'w')

T=int(fin.readline())
for t in range(1, T+1):
    N = [x for x in fin.readline().split()]
    N = list(zip(N[1::2], [int(n) for n in N[2::2]]))
    ans = 'Case #%d: %d\n'%(t, solve(N))
    print(ans)
    fout.write(ans)
fin.close()
fout.close()