import sys
import string
import math

fname = 'C'

output_format = 'single'
scale_op = input('Data Scale? 0 - practice,  1 - small,  2 - large: ')
scale = ''
if scale_op == 0: scale = 'small-practice'
elif scale_op == 1: scale = 'small'
elif scale_op == 2: scale = 'large'
else: sys.exit(0)

input_file = open(fname + '-' + scale + '.in', 'r')
output_file = open(fname + '-' + scale + '.out', 'w')


def notPal(num):
    num = str(num)
    #print "WHatnotpal?"+num+"---"+str(len(num))
    while len(num) >1:
        if num[0] != num[len(num)-1]:
            return 1
        num = num[1:len(num)-2]
    return 0

def equal_float(a, b):
    #return abs(a - b) <= sys.float_info.epsilon
    #print abs(a - b)
    return abs(a - b) <= 0.01 #see edit below for more info

def process(fp):
    num = 0
    A, none, B = fp.readline().rstrip().partition(" ")
    A = int(A)
    B = int(B)

    a = int(math.ceil(math.sqrt(A)))
    b =int(math.floor(math.sqrt(B)))
    for i in range(a,b+1):
        #print i
        if notPal(i):
            continue
        #print "Past 1"
        if not (equal_float(int(math.pow(i, 2)),math.pow(i, 2))):
            continue
        #print "Past 2"
        if notPal(int(math.pow(i, 2))):
            continue
        #print "Past 3"
        num = num+1
    return num

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
