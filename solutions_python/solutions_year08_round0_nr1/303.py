import sys

def process_file(fp):
    test_cases = int(fp.readline())
    result = []
    for i in range(test_cases):
        result.append("Case #%d: %d" % (i+1, process_case(fp)))
    return '\n'.join(result)

def process_case(fp):
    num_ses = int(fp.readline())
    ses = []
    for i in range(num_ses):
        ses.append(fp.readline().strip())
    num_reqs = int(fp.readline())
    reqs = []
    for i in range(num_reqs):
        reqs.append(fp.readline().strip())

    res = count_switches(ses, reqs)
    return res

def count_switches(ses, reqs):
    res = get_order(ses, reqs, None)
    return len(res)-1

def get_order(ses, reqs, last):
    s_ses, reqs2 = set(ses), reqs
    if last:
        s_ses.discard(last)
    result = []
    while True:
        while s_ses:
            if not reqs2:
                return result + [s_ses.pop()]
            if reqs2[0] in s_ses:
                popped = reqs2[0]
                s_ses.discard(popped)
            reqs2 = reqs2[1:]
        s_ses = set(ses)
        s_ses.discard(popped)
        result.append(popped)
#    return [popped] + get_order(ses, reqs2, popped)


if __name__ == '__main__':
#    import pdb;pdb.set_trace()
    print process_file(sys.stdin)

