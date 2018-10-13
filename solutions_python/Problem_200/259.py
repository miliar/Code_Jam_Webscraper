def tidy(s):
    l = [int(n) for n in str(s)]
    val = 0
    count = 0
    for n in l:
        if n >= val:
            count += 1
            val = n
        else:
            break

    if len(str(s)) == count:
        return s

    base = int(s[0:count]) - 1

    bs = None
    if base == 0:
        bs = ''
    else:
        bs = tidy(str(base))

    for i in range(count, len(s)):
        bs += '9'

    return bs

with open('B-large.in') as inp:
    with open('output.txt', 'w') as outp:
        ncases = int(inp.readline().strip())
        for nc in range(0, ncases):
            last = inp.readline().strip()
            outp.write('Case #{}: {}\n'.format(nc + 1, tidy((last))))