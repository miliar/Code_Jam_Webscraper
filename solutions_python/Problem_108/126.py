import sys
import itertools
from compiler.ast import Break

fname = 'A'

output_format = 'single'
scale_op = input('Data Scale? 0 - sample,  1 - small,  2 - large: ')
scale = ''
if scale_op == 0: scale = 'sample'
elif scale_op == 1: scale = 'small'
elif scale_op == 2: scale = 'large'
else: sys.exit(0)

input_file = open(fname + '-' + scale + '.in', 'r')
output_file = open(fname + '-' + scale + '.out', 'w')

def process(fp):
    N = int(fp.readline().rstrip())
    line_list = []
    for i in range(0, N):
        line_list.append([int(x) for x in fp.readline().rstrip().split(' ')])
    D = int(fp.readline().rstrip())
    line_list.append([D, 10^10])
    frontier_set = set([(0, line_list[0][0])])
    past_set = set()
    while len(frontier_set) != 0:
        state = frontier_set.pop()
        past_set.add(state)
        k = state[0]
        swing = state[1]
        for candidate in itertools.count(k + 1):
            if line_list[candidate][0] - line_list[k][0] > swing:
                break
            else:
                if candidate == N:
                    return 'YES'
                token = (candidate, min(line_list[candidate][0] - line_list[k][0], line_list[candidate][1]))
                if token not in past_set and token not in frontier_set:
                    frontier_set.add(token)
    
    return 'NO'
                

    

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
