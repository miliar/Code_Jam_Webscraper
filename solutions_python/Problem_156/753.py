import sys
import string
import fractions
import itertools

fname = 'B2015'

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

def eat_score(option):
    special = option['s']
    plates = option['p']
    return max(plates) + special


def get_options(plates, score):
    options = []
    p = max(plates)
    np = plates[:]
    if p == 9:
        np.remove(9)
        np.append(3)
        np.append(3)
        options.append({'s': score + 2, 'p': np})
        #print 'pre1', options
        options += get_options(np, score + 2)
        #print 'post1', options
        np2 = np[:]
        np2.remove(3)
        np2.remove(3)
        np2.append(4)
        np2.append(5)
        options.append({'s': score + 1, 'p': np2})
        #print 'pre2', options
        options += get_options(np2, score + 1)
        #print 'post2', options
    if p == 8:
        np.remove(8)
        np.append(4)
        np.append(4)
        options.append({'s': score + 1, 'p': np})
        options += get_options(np, score + 1)
    if p == 7:
        np.remove(7)
        np.append(4)
        np.append(3)
        options.append({'s': score + 1, 'p': np})
        options += get_options(np, score + 1)
    if p == 6:
        np.remove(6)
        np.append(3)
        np.append(3)
        options.append({'s': score + 1, 'p': np})
        options += get_options(np, score + 1)
    if p == 5:
        np.remove(5)
        np.append(3)
        np.append(2)
        options.append({'s': score + 1, 'p': np})
        options += get_options(np, score + 1)
    if p == 4:
        np.remove(4)
        np.append(2)
        np.append(2)
        options.append({'s': score + 1, 'p': np})
        options += get_options(np, score + 1)

    return options



def process(fp):
    diners = int(fp.readline())
    plates = [int(n) for n in fp.readline().split()]
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
