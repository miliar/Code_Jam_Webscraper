import logging


log = logging.getLogger(__name__)


def bathroom_stalls(input_):

    n, k = map(int, input_.split())

    log.debug("N=%d, K=%d", n, k)


    # distribute k people in n stalls

    if n == k:
        output_ = (0, 0)
    else:
        
        pn = []

        for i in range(k):
            mid = (n // 2) + (n % 2) - 1
    
            ls = mid - 0
            rs = n - 1 - mid
    
            if ls > 0:
                pn.append(ls)
            
            if rs > 0:
                pn.append(rs)

            pn = sorted(pn, reverse=True)

            # log.debug((n, k, mid, ls, rs, pn))

            n = pn.pop(0)
    
        output_ = (max(ls, rs), min(ls, rs))

    # log.debug((input_, output_))

    return ' '.join(map(str, output_))


if __name__ == '__main__':

    logging.basicConfig(level='DEBUG')

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        N = input()
        print("Case #{}: {}".format(i, bathroom_stalls(N)))
