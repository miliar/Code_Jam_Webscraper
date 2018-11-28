import sys
import string
trans = string.maketrans('abcdefghijklmnopqrstuvwxyz', 'yhesocvxduiglbkrztnwjpfmaq')

fname = 'B'

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
    (C, F, X) = fp.readline().rstrip().split()
    C = float(C)
    F = float(F)
    X = float(X)
    #print 'C - farm cost is', C
    #print 'F - farm bonus is', F
    #print 'X - win number is', X

    num_farms = 1
    Old = X/2
    New = C/2 + X/(2+F)
    base = C/2
    while New < Old:
        Old = New
        num_farms += 1
        base += C/(2+(num_farms-1)*F)
        New = base +  X/(2+num_farms*F)
        #print 'NBXX+', num_farms, base, Old, New
    return round(Old,7)

    left = C/2 + X/(2+F)
    base = C/2
    print 'FRL', right, left
    while left < right:
        num_farms += 1
        base += C/(2+(num_farms-1)*F)
        right = base + X/(2+(num_farms*F))
        left = base + C/(2+(num_farms-1)*F) + X/(2+num_farms*F)
        print 'NBRL', num_farms, base, right, left




    return right


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
