def can_be_elf(p, q, n=0):
    if p == 0:
        return False
    if n > 40:
        return False
    if p >= q:
        # we have passed 1
        # check if it's possible for the other parent to be a valid
        # distribution
        p -= q
        if p == 0 or can_be_elf(p * 2, q, n + 1):
            return n
    else:
        return can_be_elf(p * 2, q, n + 1)


if __name__ == '__main__':
    with open('test.txt') as instream:
        with open('result.txt', 'w') as outstream:
            t = int(instream.readline())
            for c in xrange(t):
                p, q = map(int, instream.readline().strip().split('/'))
                result = can_be_elf(p, q)
                outstream.write("Case #{}: {}\n".format(
                    c + 1, result if result else "impossible"))
