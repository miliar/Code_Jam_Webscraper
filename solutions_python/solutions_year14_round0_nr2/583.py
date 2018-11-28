def solve(c, f, x):
    product = 2.0
    result = 0
    while True:
        time_cost = (c / product)
        if time_cost + x / (product + f) > x / product:
            break
        
        product += f
        result += time_cost
    return result + x / product

file_in = open("B-large.in", "r")
#file_in = open("in.txt", "r")
file_out = open("out.txt", "w")

n_case = int(file_in.readline())

for case_index in range(0, n_case):
    line = file_in.readline().strip().split(" ")
    print line
    (c, f, x) = line
    result = solve(float(c), float(f), float(x))
    file_out.write("Case #%d: %s\n" % (case_index + 1, str(result)))

file_out.close()
file_in.close()
