import fileinput

def solve(l):
    total_xor = reduce(lambda x,y: x ^ y, l, 0)
    # if the total XOR isn't 0, the array can't be devided into 2
    # piles with the same XOR value - if it could be, the XOR of these
    # 2 piles together would have been 0!
    if total_xor != 0:
        return "NO"
    return str(sum(l) - min(l))


it = fileinput.input()
num_cases = int(it.next())
for i in range(num_cases):
    num_elems = int(it.next())
    elements = [int(x) for x in it.next().split()]
    assert len(elements) == num_elems
    print "Case #%d: %s"%(i+1,solve(elements))
