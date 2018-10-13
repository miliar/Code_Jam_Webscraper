import io
import sys
from collections import *
from itertools import *


# Scaffolding

def run(fin=sys.stdin, fout=sys.stdout):
    fin = io.StringIO(fin) if isinstance(fin, str) else fin
    N = int(fin.readline())
    for i in range(1, N + 1):
        t = fin.readline().rstrip('\n')
        fout.write("Case #{}: {}\n".format(i, solve(t)))

def run_sample(s, n=None, fout=sys.stdout):
    s = s.strip()
    if n is not None:
        s = "1\n" + s.split('\n')[n]
    run(s, fout)

def check_sample(sample_in, expected_out):
    expected_out = expected_out.strip("\n")
    actual_out = io.StringIO()
    run_sample(sample_in, fout=actual_out)
    for line_in, line_out in zip(expected_out.split("\n"), actual_out.getvalue().strip("\n").split("\n")):
        if line_in != line_out:
            print("Expected:", line_in)
            print("Actual  :", line_out)
            break
    print("ok")

def is_tidy(seq):
    return all(i <= j for i, j in zip(seq, seq[1:]))

assert is_tidy([1, 2, 3])
assert not is_tidy([1, 3, 2])

def str_to_digits(s):
    return [ord(c) - 48 for c in str(s)]

def digits_to_str(seq):
    return ''.join(chr(c + 48) for c in seq)

assert str_to_digits('123') == [1, 2, 3]
assert digits_to_str([1, 2, 3]) == '123'

def solve_(digits):
    if is_tidy(digits):
        return digits
    for i in range(1, len(digits)):
        if digits[i - 1] > digits[i]:
            digits = solve_(digits[:i - 1] + [digits[i - 1] - 1]) + [9] * (len(digits) - i)
    return digits

def solve(s):
    s = digits_to_str(solve_(str_to_digits(s))).lstrip('0')
    return s or '0'

run()
