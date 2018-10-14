def add(a, b):
    # in binary

    result = []

    while len(a) != len(b):
        if len(a) > len(b):
            b = '0' + b
        elif len(a) < len(b):
            a = '0' + a

    for i in range(len(a)):
        if a[i] == b[i]:
            result.append(0)
        else:
            result.append(1)

    s = ''.join([str(x) for x in result])
    return s
    #return ''.join(result)


r =  add('1100', '0101')


def bintodec(a):
    return int(a, 2)

def dectobin(a):
    s = bin(int(a))
    s = s[2:]
    return s


def get_min(lis):
    min = lis[0]
    for i in lis:
        if i < min:
            min = i
    return min



def compar(a, b):
    while len(a) != len(b):
        if len(a) > len(b):
            b = '0' + b
        elif len(a) < len(b):
            a = '0' + a

    if a == b:
        return True
    return False


filename = 'C-large.in'
inp = open(filename)
is_first = True
is_num = True
cases = []
output = open('output', 'w')
for line in inp:
    if is_first:
        is_first = False
    else:
        sp = line.split()
        if len(sp) != 1:
            cases.append(line)

little_br = []
big_br = []
case_num = 0
for case in cases:
    case_num += 1
    little_br = []
    big_br = []
    sp = case.split()
    sp_int = [int(i) for i in sp]
    min = get_min(sp_int)
    sp_int.remove(min)
    little_br.append(min)
    big_brother = sp_int

    sum_bb = '0'
    for integer in big_brother:
        #import pdb; pdb.set_trace()
        sum_bb = add(sum_bb, dectobin(integer))

    if compar(sum_bb, dectobin(little_br[0])):
        sum = 0
        for i in big_brother:
            sum += int(i)
        output.write('Case #' + str(case_num) + ': ' + str(sum)+'\n')
    else:
        output.write('Case #' + str(case_num) + ': ' + 'NO'+'\n')

