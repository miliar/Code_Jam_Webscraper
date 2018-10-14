def istidy(num: int):
    s = str(num)
    lastdig = None
    for sdig in s:
        dig = int(sdig)
        if lastdig != None and dig < lastdig:
            return False
        lastdig = dig
    return True


def lasttidy_simple(num):
    while not istidy(num):
        num -= 1
    return num


def to_list(num):
    return [int(i) for i in str(num)]


def to_int(list):
    return int(sum([x * 10**(len(list) - 1 - i) for i, x in enumerate(list)]))


def lastindex(num, li):
    if num not in li: return len(li)
    return len(li) - 1 - li[::-1].index(num)


def lasttidy_quick(num):
    if istidy(num):
        return num
    else:
        return lasttidy_quick2(num)

def lasttidy_quick2(num):
    s = to_list(num)
    s[-1] = 9
    s[-2] -= 1
    num = to_int(s)
    if istidy(num):
        return num
    else:
        return to_int(to_list(lasttidy_quick(to_int(s[0:-1]))) + [s[-1]])

f = open('input', 'r')
lines = f.read().split('\n')[1:]

out = open('output', 'w')

for lnum, line in enumerate(lines):
    i = int(line)
    res = lasttidy_quick(i)
    out.write('Case #{}: {}\n'.format(lnum + 1, res))

out.close()