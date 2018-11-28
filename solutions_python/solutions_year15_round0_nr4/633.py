import sys
import string
import fractions
import itertools

fname = 'D2015'

output_format = 'single'
scale_op = input('Data Scale? 0 - sample,  1 - small,  2 - large: ')
scale = ''
if scale_op == 0: scale = 'small-practice'
elif scale_op == 1: scale = 'small'
elif scale_op == 2: scale = 'large'
else: sys.exit(0)

input_file = open(fname + '-' + scale + '.in', 'r')
output_file = open(fname + '-' + scale + '.out', 'w')

pool = {}

def process(fp):
    line = [int(n) for n in fp.readline().split()]
    size = line[0]
    R = line[1]
    C = line[2]
    print size, R, C
    if size == 1:
        return 'GABRIEL'
    if (R * C) % size != 0:
        return 'RICHARD'
    if size == 2:
        return 'GABRIEL'
    if R == 1 or C == 1:
        return 'RICHARD'
    if size == 3:
        return 'GABRIEL'
    if R == 2 or C == 2:
        return 'RICHARD'
    return 'GABRIEL'

    return '???'
    options = []
    options.append({'s': 0, 'p': plates})
    options += get_options(plates, 0)

    min_score = 10000
    for option in options:
        if eat_score(option) < min_score:
            min_score = eat_score(option)
    return min_score

    (max, audience) = fp.readline().split()
    standing = int(audience[0])
    audience = audience[1:]
#    print "Max {0} Audience {1}".format(max, audience)
    while len(audience):
        shyness += 1
        next_shy = int(audience[0])
        audience = audience[1:]
        if next_shy == 0:
            continue
        while standing < shyness:
            adds += 1
            standing += 1
        standing += next_shy
    return adds

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
    pool = {}
    result = process(input_file)
    format_output(output_file, i, result)

input_file.close()
output_file.close()

print('Done.')
