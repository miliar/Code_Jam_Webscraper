# bendingunit22; usage: prog_name.py <input.in >output.out

def meth_one(mush):
    min_val = 0
    prev = mush[0]
    for m in mush[1:]:
        if m <= prev:
            min_val += (prev - m)
        prev = m
    return min_val


def meth_two(mush):

    min_val = 0
    prev = mush[0]
    for m in mush[1:]:
        if m <= prev:
            min_val = max(min_val, prev - m)
        prev = m


    ate = 0
    for m in mush[:-1]:
        if m >= min_val:
            ate += min_val
        else:
            ate += m
    return ate


cases = int(raw_input())
for case in range(cases):
    print "Case #%s:" % (case+1),
    N = int(raw_input())
    mush = map(int, raw_input().split())
    print meth_one(mush[:]), meth_two(mush)
