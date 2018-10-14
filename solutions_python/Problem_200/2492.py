file_name = "B-large.in"

in_file = open("./{}".format(file_name), 'r')
out_file = open("./{}.out".format(file_name), 'w')

inputs = in_file.read().strip().split("\n")
t_c = int(inputs.pop(0))


def is_tidy(n):
    l = len(n)
    for x in range(l - 1):
        if n[x] > n[x + 1]:
            return False
    return True


def make_tidy(n):
    l = len(n)
    for x in range(l - 1):
        if n[x + 1] < n[x]:
            for y in range(x + 1, l):
                n[y] = '9'
            n[x] = str(int(n[x]) - 1)
    return n


t = 1
while t <= t_c:
    t_num = list(inputs[t - 1])
    while not is_tidy(t_num):
        t_num = make_tidy(t_num)

    out_file.write("Case #{}: {}\n".format(t, int(''.join(t_num))))

    t += 1

in_file.close()
out_file.close()
