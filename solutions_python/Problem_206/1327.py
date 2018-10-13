

def parse_input(matrix):
    str_vals = [str.split() for str in matrix]
    print(str_vals)
    return str_vals

def solve(matrix,dest):
    str_vals = parse_input(matrix)
    max_time = 0
    for horsee in str_vals:
        time = (dest-float(horsee[0]))/float(horsee[1])
        if time > max_time:
            max_time = time

    return "{0:.6f}".format(dest/time)
