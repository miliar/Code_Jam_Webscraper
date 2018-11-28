import sys
import time
import msvcrt
import logging
from multiprocessing import Pool


ACTIVE_PROCESSES = 8


def click_dem_cookies(arg):
    case, c, f, x, out_file = arg
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    logging.info('Started process for case %d, c: %.3f, f: %.3f, x: %.3f.' % (case, c, f, x))

    prev_result = None
    curr_result = None
    farm_count = 0
    start = time.time()

    while any([prev_result is None, curr_result is None]) or prev_result > curr_result:
        prev_result = curr_result

        cps = 2
        this_time = 0

        for i in range(farm_count):
            farm_time = c / cps
            this_time += farm_time
            cps += f

        this_time += x / cps

        if prev_result and prev_result < this_time:
            curr_result = prev_result
            break
        else:
            curr_result = this_time
            farm_count += 1

    logging.info("Took %.1f secs to calculate case %d" % (time.time() - start, case))

    with open(out_file, 'ab') as fh:
        fh.write('%d %.7f\r\n' % (case, curr_result))


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
        c, f, x = map(float, inp.pop(0).strip().split(" "))
        data.append((i+1, c, f, x, results_file))

    pool.map(click_dem_cookies, data)

    with open(results_file, 'rb') as fh:
        cases = fh.readlines()

    cases = [c.strip().split(" ") for c in cases]
    cases.sort(key=lambda x: int(x[0]))

    with open(results_file, 'wb') as fh:
        for case in cases:
            i, time_taken = case
            strn = "Case #%s: %s\r\n" % (i, time_taken)
            print strn,
            fh.write(strn)

    #     assert result is not None and type(result) is float
    #     case = 'Case #%d: %.7f\r\n' % (i + 1, result)
    #     print case,
    #     output += case
    #
    # with open(sys.argv[1] + '.out', 'wb') as fh:
    #     fh.write(output)
    

if __name__ == '__main__':
    main()
