import sys

def pancake_dynamic(pancakes, flipper):
    p_list = []
    positive_bool = True
    for p in pancakes:
        if p == "-":
            positive_bool = False
        p_list.append(p)
    if positive_bool:
        return 0
    if int(flipper) == 0 or int(flipper) > len(p_list):
        return 'IMPOSSIBLE'
    flips = len(p_list) + 1 - int(flipper)
    flip_count = 0
    for i in range(flips):
        if p_list[i] == '-':
            for p in range(i,i+int(flipper)):
                p_list[p] = '+' if p_list[p] == '-' else '-'
            flip_count += 1
    postitve_bool = True
    for p in p_list:
        if p == '-':
            postitve_bool = False
    if postitve_bool:
        return flip_count
    else:
        return 'IMPOSSIBLE'

# raw_input() reads a string with a line of input, stripping the '\n' (newline) at the end.
# This is all you need for most Google Code Jam problems.
# t = int(raw_input())  # read a line with a single integer
f = open(sys.argv[1], 'r')
input_file = f.read().splitlines()
f.close()
output_file = open('output_large.out', 'w')
t = int(input_file[0])
for i in xrange(1, t + 1):
  n, m = [s for s in input_file[i].split(" ")]  # read a list of integers, 2 in this case
  output = pancake_dynamic(n,m)
  out_string = "Case #" + str(i) + ": " + str(output)
  print out_string
  output_file.write(out_string)
  output_file.write('\n')
  # print m
  # check out .format's specification for more formatting options