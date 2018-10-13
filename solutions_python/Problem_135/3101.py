f=open('A-small-attempt0.in','r')
output = open('out.txt', 'w') # Output File
for i in range(1,int(f.readline())+1):
    a=int(f.readline())-1
    A = [[None for x in range(4)] for y in range(4)]
    A[0] = [int(x) for x in f.readline().split()]
    A[1] = [int(x) for x in f.readline().split()]
    A[2] = [int(x) for x in f.readline().split()]
    A[3] = [int(x) for x in f.readline().split()]
    c={A[a][p] for p in range(0,4)}
    b=int(f.readline())-1
    B = [[None for x in range(4)] for y in range(4)]
    B[0] = [int(x) for x in f.readline().split()]
    B[1] = [int(x) for x in f.readline().split()]
    B[2] = [int(x) for x in f.readline().split()]
    B[3] = [int(x) for x in f.readline().split()]
    d={B[b][p] for p in range(0,4)}
    output.write('Case #'+str(i)+': ')
    if len(d & c)==0: output.write('Volunteer cheated!')
    if len(d & c)==1: output.write(str((d&c).pop()))
    if len(d & c) >1: output.write('Bad magician!')
    output.write('\n')
f.close()
output.close()
        
