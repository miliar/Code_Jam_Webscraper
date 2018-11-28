import sys


##def print_status(snapper_powered, snapper_on):
##    on_str = reduce(lambda x, y: x + y,
##                    map(lambda x: '1' if x else '0', snapper_on), "")
##    pwr_str = reduce(lambda x, y: x + y,
##                     map(lambda x: '*' if x else ' ', snapper_powered), "")
##    print on_str
##    print pwr_str
##
##
##def snap(snapper_powered, snapper_on):
##    k = 0
##    while snapper_powered[k]:
##        snapper_on[k] = not snapper_on[k]
##        k = k + 1
##
##    snapper_powered[0] = True
##    for k in xrange(1,len(snapper_powered)):
##        if snapper_powered[k - 1] and snapper_on[k - 1]:
##            snapper_powered[k] = True
##        else:
##            snapper_powered[k] = False
##
##    
##def process_case_test(N, K):
##    snapper_on = N*[False]
##    snapper_powered = N*[False]
##    snapper_powered[0] = True
##
##    for k in xrange(K):
##        snap(snapper_powered, snapper_on)
##        print_status(snapper_powered, snapper_on)
##        
##def test():
##    process_case_test(20, 20)
##


def is_light_on(N, K):
    # Only the N lowest bits of K matter
    lowK = K % 2**N

    # in lowK is all ones in binary, power flows all the way to the light
    if lowK == 2**N - 1:
        return True

    return False


def process_case(case_number, N, K):
    if is_light_on(N, K):
        print "Case #%d: ON" % case_number
    else:
        print "Case #%d: OFF" % case_number

def main():
    nbCases = int(sys.stdin.readline())
    for k, line in enumerate(sys.stdin):
        numbers = map(int, line.split())
        process_case(k + 1, numbers[0], numbers[1])


if __name__ == "__main__":
    main()
