from sys import argv

def gcd(a, b):
    a, b = max(a,b), min(a,b)
    if b == 0:
        return a
    return gcd(b, a - b * (a / b))

def solve_line(num_elems, *elems):
    assert num_elems == len(elems)
    min_elem = reduce(min, elems)
    adj_elems = [elem - min_elem for elem in elems]
    gcd_of_elems = reduce(gcd, adj_elems)

    
    i = -(min_elem % gcd_of_elems)
    while i < 0:
        i += gcd_of_elems

    return i
    
def process_file(fin, fout):
    numLines = int(fin.readline())
    for i in range(numLines):
        result = solve_line(*map(int, fin.readline().split(' ')))
        fout.write("Case #%s: %s\n" % (i + 1, result))

process_file(open(argv[1]), open(argv[1].replace("in", "out"), "w"))