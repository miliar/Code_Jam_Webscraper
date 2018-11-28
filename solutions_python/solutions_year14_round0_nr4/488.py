import sys
import string
trans = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq')

fname = 'D'

output_format = 'single'
scale_op = input('Data Scale? 0 - sample,  1 - small,  2 - large: ')
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
    num_blocks = fp.readline().rstrip()
    blocks = fp.readline().rstrip().split()
    n_blocks = [float(x) for x in blocks]
    k_blocks = map(float, fp.readline().rstrip().split())
    n_blocks2 = n_blocks[:]
    k_blocks2 = sorted(k_blocks[:])
    o_wins = 0

    while (n_blocks):
        min_n = min(n_blocks)
        min_k = min(k_blocks)
        if min_n < min_k:
            n_blocks.remove(min_n)
            k_blocks.remove(max(k_blocks))
        else:
            n_blocks.remove(min_n)
            k_blocks.remove(min_k)
            o_wins +=1

    wins = 0
    n_blocks = n_blocks2
    k_blocks = k_blocks2
    #print k_blocks
    while (n_blocks):
        pick = n_blocks.pop()
        won = 0
        for i in k_blocks:
            if i > pick:
                won = 1
                k_blocks.remove(i)
                break
        if not won:
            wins += 1
            k_blocks.pop(0)






    return str(o_wins) +" "+ str(wins)

    print n_blocks
    print k_blocks
    return 0


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
