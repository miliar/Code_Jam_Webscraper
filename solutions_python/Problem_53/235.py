
import math

with open('A-large.in') as input, open('out.txt', 'w') as output:
    cases = int(input.readline())
    for i in range(1,cases+1):
        case=input.readline().split(" ")
        n = int(case[0])
        k = int(case[1])
        magic = 2**n;
        test1 = k>=(magic-1)
        div = float(k+1)/magic;
        test2 = (int(div) == div)
        if (test1&test2):
            print('Case #{}: {}'.format(i,'ON'))
            output.write('Case #{}: {}\n'.format(i,'ON'))
        else:
            print('Case #{}: {}'.format(i,'OFF'))
            output.write('Case #{}: {}\n'.format(i,'OFF'))
    output.close()
        