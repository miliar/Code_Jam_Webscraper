import sys
import string

fname = 'B'

output_format = 'single'
scale_op = input('Data Scale? 0 - practice,  1 - small,  2 - large: ')
scale = ''
if scale_op == 0: scale = 'small-practice'
elif scale_op == 1: scale = 'small'
elif scale_op == 2: scale = 'large'
else: sys.exit(0)

input_file = open(fname + '-' + scale + '.in', 'r')
output_file = open(fname + '-' + scale + '.out', 'w')


def check(line):
    #sys.stdout.write("Checking "+line+"\n")
    if "." in line: return 0
    if "X" in line and "O" in line: return 0
    if "X" in line: return "X won"
    return "O won"

def process(fp):
    N, none, M = fp.readline().rstrip().partition(" ")
    N = int(N)
    M = int(M)
    check = [[0 for i in range(M)] for j in range(N)]
    real = [[0 for i in range(M)] for j in range(N)]
    maxcol = [0 for i in range(M)]
    for i in range(0, N):
        real[i] = fp.readline().rstrip().split()
        high = max(real[i])
        for j in range(0,M):
            if real[i][j] > maxcol[j]:
                maxcol[j] = real[i][j]
            if real[i][j]==high:
                check[i][j]=1


    for i in range(0, N):
        for j in range(0,M):
            if real[i][j] == maxcol[j]:
                check[i][j]=1
            if check[i][j]==0:
                return "NO"


    return "YES"


    answer = "Game has not completed" #ongoing
    l = fp.readline().rstrip()+fp.readline().rstrip()+fp.readline().rstrip()+fp.readline().rstrip()
    fp.readline().rstrip()
    if not "." in l: answer = "Draw" #draw
    ans = check(l[0:4])
    if ans:
        return (ans)
    ans = check(l[4:8])

    if ans:
        return (ans)
    ans = check(l[8:12])
    if ans:
        return (ans)
    ans = check(l[12:16])
    if ans:
        return (ans)


    return (answer)
    

def format_output(fp, i, result):
    if output_format == 'single':
        fp.write('Case #%d: %s\n' % (i, result))
    elif output_format == 'multiple':
        fp.write('Case #%d:\n' % (i,))
        for r in result:
            fp.write('%s\n' % r)
    else:
        print 'No output format.'
    print('Case #%d: %s' % (i, result))

T = int(input_file.readline().rstrip('\n'))
for i in range(1, T+1):
    result = process(input_file)
    format_output(output_file, i, result)

input_file.close()
output_file.close()

print('Done.')
