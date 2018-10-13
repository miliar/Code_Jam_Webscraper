#! /usr/bin/python3
in_file = open('/home/blaidd-drwg/pancake_input.txt', 'r')
out_file = open('/home/blaidd-drwg/pancake_output.txt', 'w')

in_data = in_file.readlines()
cases = int(in_data[0])

for case in range(1, cases + 1):
    case_data = in_data[case].split()
    pancakes = case_data[0]
    k = int(case_data[1])
    stack = []

    for p in pancakes:
        if p == '-':
            stack.append(False)
        else:
            stack.append(True)

    flips = 0
    for i in range(0, len(stack) - (k-1)):
        if not stack[i]:
            flips += 1
            for f in range(0, k):
                stack[i + f] = not stack[i + f]

    flips_string = str(flips)
    for p in stack:
        if not p:
            flips_string = 'IMPOSSIBLE'

    out_file.write('Case #%d: %s' % (case, flips_string))
    out_file.write('\n')

in_file.close()
out_file.close()
