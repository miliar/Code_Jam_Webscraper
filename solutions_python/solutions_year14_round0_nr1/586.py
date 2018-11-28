f_in = open("A-small-attempt0.in", 'r')
f_out = open("a_real.out", 'w')

def get_int():
    return int(f_in.readline().rstrip())

def get_row(n):
    grid = []
    for i in range(0, 4):
        grid.append(f_in.readline().rstrip())
    return grid[n-1].split()

n = get_int()

for case in range(1, n + 1):
    first_row_n = get_int()
    first_row = get_row(first_row_n)
    
    second_row_n = get_int()
    second_row = get_row(second_row_n)

    shared = [i for i in first_row if i in second_row]

    result = "MEOW"

    if len(shared) == 1:
        result = shared[0]
    elif len(shared) == 0:
        result = "Volunteer cheated!"
    else:
        result = "Bad magician!"

    f_out.write("Case #{0}: {1}\n".format(case, result))

f_in.close()
f_out.close()
