def flip_stack(stack):
    return ''.join(["+" if x == "-" else "-" for x in stack])

def solve_case(stack, k):

    unsorted_stack = stack[stack.find("-"):] if stack.find("-") != -1 else ''
    flip_counter = 0
    while len(unsorted_stack) >= k:
        stack = stack[:stack.find("-")] + flip_stack(unsorted_stack[:k]) + unsorted_stack[k:]
        unsorted_stack = stack[stack.find("-"):] if stack.find("-") != -1 else ''
        flip_counter += 1

    if len(unsorted_stack) > 0:
        return "IMPOSSIBLE"
    else:
        return flip_counter

def solve_from_file(infile, outfile):
    fin = open(infile, 'rb')
    fout = open(outfile, 'wb')
    t = int(fin.readline())
    res = []
    for i in xrange(t):
        stack, k = fin.readline().split()
        res.append("Case #{i}: {res}\n".format(
            i=i+1,
            res=solve_case(stack, int(k))
        ))
    fout.writelines(res)

if __name__ == "__main__":
    solve_from_file("/Users/yoni/Downloads/A-large.in", "/Users/yoni/Downloads/A-large.out")
