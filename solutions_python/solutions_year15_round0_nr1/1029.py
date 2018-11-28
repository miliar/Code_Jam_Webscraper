import sys
import string
import fractions
import itertools

fname = 'A'

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

def check(my_list):
    if not my_list in pool:
        pool[my_list] = check2(my_list)
    return pool[my_list]

def check2(my_list):
    prev = ""
    hit = {}
    for j in my_list:
        for char in j:
            if prev != char:
                if char in hit:
                    return False
                prev = char
                hit[char] = True
                continue
            elif char == prev:
                continue
    return True

def process(fp):
    shyness = 0
    adds = 0
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
