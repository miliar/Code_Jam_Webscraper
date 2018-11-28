import os
import sys
from sure import that

MAPPING = {'y': 'a', 'e': 'o', 'q': 'z', 'z': 'q'}

input1 = 'ejp mysljylc kd kxveddknmc re jsicpdrysi'
input2 = 'rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd'
input3 = 'de kr kd eoya kw aej tysr re ujdr lkgc jv'

output1 = 'our language is impossible to understand'
output2 = 'there are twenty six factorial possibilities'
output3 = 'so it is okay if you want to just give up'

mappings = zip(input1, output1) + zip(input2, output2) + zip(input3, output3)
for googlerese, english in mappings:
    if not googlerese in MAPPING:
        MAPPING[googlerese] = english
    else:
        assert that(MAPPING[googlerese]).equals(english)

def translate(_input):
    output = ""
    for char in _input:
        output += MAPPING[char]
    return output

assert that(translate(input1)).equals(output1)
assert that(translate(input2)).equals(output2)
assert that(translate(input3)).equals(output3)

if len(sys.argv) > 1:
    dirname, _ = os.path.split(os.path.abspath(sys.argv[0]))
    input_file = open(os.path.join(dirname, sys.argv[1]), 'r')
    output_file = open(os.path.join(dirname, 'solution.txt'), 'w')
    
    T = int(input_file.readline().rstrip('\n'))
    case_num = 1
    while case_num - 1 < T:
        output_file.write('Case #{}: {}\n'.format(case_num, translate(input_file.readline().rstrip('\n'))))
        case_num += 1
