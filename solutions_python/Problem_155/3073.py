__author__ = 'Taras'

file_name = 'data/A-large.in'
f = open(file_name)

N = int(f.readline())
input_data = [f.readline().split(' ') for i in range(N)]
f.close()

for i in range(N):
    s_max, ss = int(input_data[i][0]), input_data[i][1]
    acc = int(ss[0])
    needed = 0
    for j in range(1, s_max + 1):
        curr = int(ss[j])
        if curr != 0 and acc < j:
            diff = j - acc
            needed += diff
            acc += diff
        acc += curr
    print("Case #{0}: {1}".format(i + 1, needed))