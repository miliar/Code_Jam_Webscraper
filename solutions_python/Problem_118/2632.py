import math

def is_square(integer):
    root = math.sqrt(integer)
    if int(root + 0.5) ** 2 == integer: 
        return True
    else:
        return False

def reverse_number(n, partial=0):
    if n == 0:
        return partial
    return reverse_number(n / 10, partial * 10 + n % 10)

def _get_fair_square(inp):
    start = int(inp[0])
    end = int(inp[1])
    cnt = 0
    for i in range(start, end + 1):
        if reverse_number(i) == i and is_square(i) and reverse_number(int(math.sqrt(i))) == int(math.sqrt(i)):
            cnt += 1
    return cnt



file_in = "C-small-attempt0.in.txt"
file_out = "C-small-attempt0.out.txt"

with open(file_in, "r") as ff, open(file_out, "w") as out:
    num = int(ff.readline())
    inputs = []
    for each in xrange(num):
        inputs.append([int(x) for x in ff.readline().rstrip().split()[:2]])

    for i, each in enumerate(inputs):
        output = _get_fair_square(each)
        print ("Case #%s: %s\n" % (i+1, str(output)))
        out.write("Case #%s: %s\n" % (i+1, str(output)))
