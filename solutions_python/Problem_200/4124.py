#!/usr/bin/env python3
import sys


"""

1000000
0999999


1000005
0999999

102345678
099999999

132
129
1345456780
1344999999

140238
139999

1111110222
1111109999

2222222203333
2222219999999

if next digit < current digit
current digit -1
for remaining next digit become 9

"""

def parse_test_file(filename):
    tc_list = []
    with open(filename) as f:
        t = next(f)
        for l in f:
            l = [int(_) for _ in l.strip()]
            tc_list.append(l)
    return tc_list


def process(l):
    cutoff = 0
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            l[i] -= 1
            for j in range(i+1, len(l)):
                l[j] = 9
            cutoff = i
            break

    if cutoff > 0 and l[cutoff-1] > l[cutoff]:
        for j in range(cutoff-1, -1, -1):
            l[i] = 9
            l[j] -= 1
            i = j



    
    return int(''.join(str(_) for _ in l))





def output_results(results, file=sys.stdout):
    for i, result in enumerate(results):
        print(f"Case #{i+1}: {result}", file=file)



def main(tc_list):    
    results = []
    for tc in tc_list:
        results.append(process(tc))

    output_results(results)



if __name__ == '__main__':
    filename = sys.argv[1]
    tc_list = parse_test_file(filename)
    main(tc_list)