#!/usr/bin/python

multiply = {
    ('1', '1'): (1, '1'),
    ('1', 'i'): (1, 'i'),
    ('1', 'j'): (1, 'j'),
    ('1', 'k'): (1, 'k'),
    ('i', '1'): (1, 'i'),
    ('i', 'i'): (-1, '1'),
    ('i', 'j'): (1, 'k'),
    ('i', 'k'): (-1, 'j'),
    ('j', '1'): (1, 'j'),
    ('j', 'i'): (-1, 'k'),
    ('j', 'j'): (-1, '1'),
    ('j', 'k'): (1, 'i'),
    ('k', '1'): (1, 'k'),
    ('k', 'i'): (1, 'j'),
    ('k', 'j'): (-1, 'i'),
    ('k', 'k'): (-1, '1')
}

testcases = int(raw_input());
for testcase in xrange(1, testcases+1):
    line = raw_input()
    line = line.split(' ')
    l = int(line[0])
    x = int(line[1])

    line = raw_input()
    chars = list(line * x)

    sign = 1 
    current = '1'
    while ((current != 'i') and (chars)):
        (new_sign, current) = multiply[(current, chars.pop(0))]
        sign = sign * new_sign
    if (not chars): 
        print('Case #%d: NO'% testcase)
        continue
    current = '1'
    while ((current != 'j') and (chars)):
        (new_sign, current) = multiply[(current, chars.pop(0))] 
        sign = sign * new_sign 
    if (not chars):
        print('Case #%d: NO'% testcase)
        continue
    current = '1'
    while (chars): 
        (new_sign, current) = multiply[(current, chars.pop(0))] 
        sign = sign * new_sign 
    if (sign == -1):
        print('Case #%d: NO'% testcase)
        continue 
    if (current != 'k'):
        print('Case #%d: NO'% testcase)
        continue
    print('Case #%d: YES'% testcase)
