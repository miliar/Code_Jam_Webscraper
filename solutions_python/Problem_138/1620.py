import sys
import time
import msvcrt
import logging
from multiprocessing import Pool

ACTIVE_PROCESSES = 8


def normal_war(naomi, ken):
    n_wins = 0
    k_wins = 0

    for n in naomi:
        choice = max(ken)
        for k in ken:
            if k < choice and k > n:
                choice = k

        if choice < n:
            choice = min(ken)

        ken.remove(choice)

        if choice > n:
            k_wins += 1
        else:
            n_wins += 1

    return n_wins


def deceitful_war(naomi, ken):
    assert isinstance(naomi, list)
    naomi.sort()
    ken.sort()

    logging.info("naomi: %r, ken: %r" % (naomi, ken))

    n_wins = 0
    k_wins = 0

    while len(naomi) > 0:
        while naomi[-1] > ken[-1]:

            choice = max(naomi)
            for n in naomi:
                if n > ken[-1]:
                    choice = n

            n_wins += 1
            naomi.remove(choice)
            ken.pop(-1)

            if len(naomi) == 0:
                break

        if len(naomi) == 0:
            break

        if naomi[0] < ken[-1]:
            k_wins += 1
        else:
            n_wins += 1
        naomi.pop(0)
        ken.pop(-1)

    return n_wins


def test_one_case(arg):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    case, naomi, ken, outf = arg
    norm = normal_war([n for n in naomi], [k for k in ken])
    dec = deceitful_war([n for n in naomi], [k for k in ken])

    with open(outf, 'ab') as fh:
        fh.write('%d %d %d\r\n' % (case, dec, norm))


def main():
    with open(sys.argv[1], 'rb') as fh:
        inp = fh.readlines()

    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    t = int(inp.pop(0))
    results_file = sys.argv[1] + '.out'
    with open(results_file, 'wb') as fh:
        pass
    data = list()
    pool = Pool(ACTIVE_PROCESSES)

    for i in range(t):
        expected_len = int(inp.pop(0))
        n = map(float, inp.pop(0).strip().split(" "))
        k = map(float, inp.pop(0).strip().split(" "))

        assert len(n) == len(k) and len(k) == expected_len

        data.append((i+1, n, k, results_file))

    pool.map(test_one_case, data)

    with open(results_file, 'rb') as fh:
        cases = fh.readlines()

    cases = [c.strip().split(" ") for c in cases]
    cases.sort(key=lambda x: int(x[0]))

    with open(results_file, 'wb') as fh:
        for case in cases:
            line = "Case #%s: %s %s\r\n" % (case[0], case[1], case[2])
            print line,
            fh.write(line)
    

if __name__ == '__main__':
    main()
