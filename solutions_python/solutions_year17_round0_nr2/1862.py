#! /usr/bin/python3
in_file = open('/home/blaidd-drwg/tidy_input.txt', 'r')
out_file = open('/home/blaidd-drwg/tidy_output.txt', 'w')

in_data = in_file.readlines()
cases = int(in_data[0])

for case in range(1, cases + 1):
    n = int(in_data[case])
    l = [int(c) for c in list(str(n))]
    done = False
    leftmost_sorted = len(l)
    while not done:
        done = True
        for i in range(1, leftmost_sorted):
            if l[i - 1] > l[i]:
                done = False
                l[i - 1] -= 1
                for j in range(i, len(l)):
                    l[j] = 9
                leftmost_sorted = i

        if leftmost_sorted == 0:
            break

    new_n = int(''.join([str(i) for i in l]))
    out_file.write('Case #%d: %d' % (case, new_n))
    out_file.write('\n')

in_file.close()
out_file.close()
