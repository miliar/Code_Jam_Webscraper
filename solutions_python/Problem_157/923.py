import copy


d = {('i','j'): 'k',
     ('j','i'): '-k',
     ('j','k'): 'i',
     ('k','j'): '-i',
     ('k','i'): 'j',
     ('i','k'): '-j'}


def mul_q(q1, q2):
    sign = 1
    if q1[0] == '-':
        sign *= -1
        q1 = q1[1:]
    if q2[0] == '-':
        sign *= -1
        q2 = q2[1:]

    if q1 == '1':
        ans = q2
    elif q2 == '1':
        ans = q1
    elif q1 == q2:
        ans = '-1'
    else:
         ans = d[(q1, q2)]

    if sign == -1:
        if ans[0] == '-':
            return ans[1:]
        else:
            return '-' + ans
    else:
        return ans

def prod_string(s):
    qs = list(s)
    acc = '1'
    for q in s:
        acc = mul_q(acc, q)
    return acc

def exp_q(q, pow):
    pow = pow % 4
    if pow == 0:
        return '1'
    acc = '1'
    for i in range(pow):
        acc = mul_q(acc, q)
    return acc

def solve_case(case):
    pow, s = case
    if exp_q(prod_string(s), pow) != '-1':
        return 'NO'
    pow_i = min(pow, 4)
    ans_i = starts_i(s * pow_i)
    if ans_i:
        remaining_chars = ans_i[1]
    else:
        return 'NO'

    pow_j = min(pow - pow_i, 4)
    ans_j = starts_j(remaining_chars + s * pow_j)
    if ans_j:
        return 'YES'
    else:
        return 'NO'

def starts_i(s):
    qs = list(s)
    acc = '1'
    chars_used = 0
    for q in s:
        acc  = mul_q(acc, q)
        chars_used += 1
        if acc == 'i':
            return (True, ''.join(qs[chars_used:]))
    return False

def starts_j(s):
    qs = list(s)
    acc = '1'
    chars_used = 0
    for q in s:
        acc  = mul_q(acc, q)
        chars_used += 1
        if acc == 'j':
            return (True, ''.join(qs[chars_used:]))
    return False

    
    
        

        


f = open('c.in', 'r')
lines = f.readlines()

cases = [(int(lines[2*i - 1].split()[1]), lines[2*i].strip()) for i in xrange(1, 1 + len(lines)/2)]
print(len(cases))
print(cases)

g = open('c.out','w')
for i in xrange(len(cases)):
    g.write('Case #' + str(i + 1) + ': ' + str(solve_case(cases[i])) + '\n')
g.close()


