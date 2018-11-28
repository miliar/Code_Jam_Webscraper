# read in number of lines T
from sys import stdin
line = stdin.readline()

T = int(line.strip())

for x in range(T):
    line = stdin.readline().strip()
    max_shyness, shyness_str = line.split()
    max_shyness = int(max_shyness)
    # want a list of integers, rather than a string
    shyness_list = list(map(int, shyness_str))

    ans = 0
    running_count = 0
    for y in range(len(shyness_list)):
        running_count += shyness_list[y]
        if running_count < y+1:
            ans += 1
            running_count += 1

    print("Case #%d: %d" % (x+1, ans))


