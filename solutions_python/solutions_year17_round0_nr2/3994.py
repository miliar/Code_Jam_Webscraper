#!/usr/bin/env python

def get_tidy_digits(n): return [(True if int(str(n)[(i-1)])<=int(str(n)[i]) else False) for i in range(1, len(str(n)))]
def is_tidy(n): return not False in get_tidy_digits(n)

def get_last_tidy(n):
    while not is_tidy(n):
        tidy_digits = get_tidy_digits(n)
        n = (n-(1+int(str(n)[tidy_digits.index(False)+1:])))

    return n


cases = []
with open('input', 'r') as read_input: cases = read_input.read().split('\n')

output = ''

for ci in range(int(cases.pop(0))):
    output += ('Case #' + str(ci+1) + ': ' + str(get_last_tidy(int(cases[ci]))) + '\n')


with open('output', 'w') as write_output: write_output.write(output)
