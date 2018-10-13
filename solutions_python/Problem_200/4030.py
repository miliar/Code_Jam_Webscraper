def is_tidy(l):
    tidy = False
    pos_failed = 0

    for i in xrange(0, len(l) - 1):
        if l[i + 1] and int(l[i]) <= int(l[i+1]):
            tidy = True
        else:
            tidy = False
            pos_failed = i
            break

    return {
        'tidy': tidy,
        'pos_failed': pos_failed
    }


def tidy(l, pos_failed):
    if pos_failed == 0:
        if l[0] == 1:
            l.remove(l[0])
            l = [9 for x in l]
        else:
            l[0] -= 1
            l = [l[0]] + [9 for x in l[:-1]]

    if pos_failed != 0:
        l[pos_failed] -= 1
        l = l[:pos_failed+1] + [9 for x in l[pos_failed+1:]]

    return l


def list_to_string(l):
    return ''.join(str(e) for e in l)


def int_to_list(num):
    return [int(x) for x in str(num)]


def printer(i, o):
    print "Case #{}: {}".format(i, o)

t = int(raw_input())

for i in xrange(1, t + 1):
    l = int_to_list(raw_input())

    while True:
        if len(l) == 1:
            printer(i, l[0])
            break
        tidy_obj = is_tidy(l)
        if tidy_obj['tidy']:
            printer(i, list_to_string(l))
            break
        else:
            l = tidy(l, tidy_obj['pos_failed'])
