import sys

def get_impossible_set(d, v):
    possible_list = [] + d

    for j in range(2**(len(d))):
        k = j
        counter = 0
        num = 0
        while k > 0:
            if k % 2 == 1:
                num += d[counter]
            k /= 2
            counter += 1
        possible_list.append(num)


    impossible_set = []
    for j in range(v+1):
        if not (j in possible_list):
            impossible_set.append(j)
    return impossible_set


in_file = open(sys.argv[1], "r")

out_file = open("output.out", "w")

t = int(in_file.readline())

for i in range(t):
    params = in_file.readline().split(' ')

    c = int(params[0])

    v = int(params[2])

    d = map(int, in_file.readline().split(' '))
    d.sort()

    impossible_set = get_impossible_set(d, v)

    counter = 0
    while impossible_set != []:
        d.append(impossible_set[0])
        d.sort()
        counter += 1
        impossible_set = get_impossible_set(d, v)

    out_file.write("Case #" + str(i + 1) + ": " + str(counter))

    out_file.write("\n")

in_file.close()
out_file.close()
