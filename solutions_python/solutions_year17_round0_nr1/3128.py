import argparse

parser =  argparse.ArgumentParser(description='Google Code Jam 2017')
parser.add_argument('fin')
parser.add_argument('fout')

args = parser.parse_args()

fin = args.fin
fout = args.fout

def solver(p, K):
    ret = 0
    for i in range(len(p)):
        if p[i] == '-':
            if len(p) - i < K:
                return 'IMPOSSIBLE'
            else:
                ret += 1
                for j in range(i, i+K):
                    if p[j] == '-':
                        p[j] = '+'
                    else:
                        p[j] = '-'
    return ret

with open(fin,'r') as input, open(fout,'w') as output:
    T = int(input.readline().rstrip('\n'))
    for i in range(0,T):
        s = input.readline().rstrip('\n')
        l = s.split(' ')
        p = list(l[0])
        K = l[1]
        K = int(K)
        answer = 'Case #{}: {}\n'.format(i+1,solver(p, K))
        print(answer)
        output.write(answer)