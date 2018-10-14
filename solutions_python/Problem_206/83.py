import argparse

parser =  argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout

def solver(D, Ki, Si):
    tmax = (D-Ki[0])/Si[0]
    for i in range(len(Ki)):
        t = (D - Ki[i]) / Si[i]
        tmax = max(t, tmax)
    return D/tmax

with open(fin,'r') as input, open(fout,'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0,T):
        s = input.readline().rstrip('\n')
        l = s.split(' ')
        D = float(l[0])
        N = int(l[1])
        Ki = []
        Si = []
        for j in range(int(N)):
            s = input.readline().rstrip('\n')
            l = s.split(' ')
            Ki.append(float(l[0]))
            Si.append(float(l[1]))
        answer = 'Case #{}: {}\n'.format(i+1,solver(D, Ki, Si))
        print(answer)
        output.write(answer)