import math
import itertools

def check_palindrome(strng):
    if (len(strng) == 1):
        return True
    if (len(strng) == 2):
        return strng[0] == strng[1]
    if (strng[0] == strng[-1]):
        return check_palindrome(strng[1:-1])
    return False


def check_square(num):
    sqr = num * num
    return check_palindrome(str(sqr)), sqr


def perf_palindrome_kd(k, A, B, cnt):
    digits = [str(n) for n in range(10)]
    if (k % 2 == 0):
        d = itertools.combinations(digits, k/2)
    else:
        d = itertools.combinations(digits, (k+1)/2)
    while True:
        try:
            num_str = d.next()
            if (num_str[0] == '0'):
                continue
            if (k % 2 == 0):
                num = int(''.join(num_str + num_str[::-1]))
            else:
                num = int(''.join(num_str + num_str[:-1][::-1]))
            sts, val = check_square(num)
            if (sts):
                if (A <= val <= B):
                    cnt = cnt + 1
        except StopIteration:
            return cnt

def palindrome(A, B):
    a = math.sqrt(A)
    b = math.sqrt(B)
    na = len(str(int(a)))
    nb = len(str(int(b)))
    cnt = 0
    for k in range(na, nb + 1):
        cnt = perf_palindrome_kd(k, A, B, cnt)
    return cnt


fid_ip = open('C-small-attempt2.in', 'r')
fid_op = open('output.in', 'w')

num_cases = int(fid_ip.readline())

for case in range(num_cases):
    [A, B] = [int(x) for x in fid_ip.readline().split()]
    fid_op.write('Case #' + str(case+1) + ': ' + str(palindrome(A, B))+"\n")

