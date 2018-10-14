def solve_normal(a, b):
    a = sorted(a, reverse = True)
    b = sorted(b, reverse = True)
    n = len(a)
    result = 0
    while a:
        a_item = a.pop()
        b_item = -1
        while b:
            b_item = b.pop()
            if b_item > a_item:
                break
        if a_item > b_item:
            result += 1
    return result

def solve_cheat(a, b):
    a = sorted(a, reverse = True)
    b = sorted(b, reverse = True)
    result = 0
    while a:
        if a[0] > b[0]:
            result += 1
            a.pop(0)
            b.pop(0)
        else:
            a.pop()
            b.pop(0)
    return result

file_in = open("D-large.in", "r")
#file_in = open("in.txt", "r")
file_out = open("out.txt", "w")

n_case = int(file_in.readline())

for case_index in range(0, n_case):
    file_in.readline()
    items = file_in.readline().strip().split(" ")
    a = []
    for item in items:
        a.append(float(item))
    items = file_in.readline().strip().split(" ")
    b = []
    for item in items:
        b.append(float(item))
    y = solve_cheat(a, b)
    z = solve_normal(a, b)
    file_out.write("Case #%d: %d %d\n" % (case_index + 1, y, z))

file_out.close()
file_in.close()
