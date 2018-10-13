import logging


log = logging.getLogger(__name__)


def tidy_numbers(n):
    logging.debug(n)

    # if n == 111111111111111110:
    #     return 0

    ns = str(n)
    nt = ''.join(sorted(ns))
    
    while not ns == nt:

        nl = list(ns)
        for j in range(len(nl)-1):
            x1 = int(nl[-2-j])
            x2 = int(nl[-1-j])


            if x1 > x2:
                nl[-2-j] = str(x1 - 1)
                for i in range(j+1):
                    nl[-1-i] = '9'

            # logging.debug((x1, x2, nl))

        ns = ''.join(nl)
        
        nt = ''.join(sorted(ns))

    nt = int(nt)
    logging.debug(nt)
    return nt    


if __name__ == '__main__':

    logging.basicConfig(level='DEBUG')

    T = int(input())  # read a line with a single integer (input size)
    for i in range(1, T + 1):
        N = input()
        print("Case #{}: {}".format(i, tidy_numbers(N)))
