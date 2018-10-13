
def isTidy(N):
    non_sorted = str(N)
    sort = ''.join(sorted(non_sorted))

    return sort == non_sorted


def tidy_number(N):
    last = 0
    i = N
    while i > -1:
        if isTidy(i):
            return i
        i -= 1
    return last

def main():
    T = int(raw_input())  # read a line with a single integer
    for i in range(1, T+1):
        [N] = [long(s) for s in raw_input().split(" ")]  # read a list of integers, 2 in this case
        last_num = tidy_number(N)
        print "Case #{}: {} ".format(i, last_num)
    # check out .format's specification for more formatting options

if __name__ == '__main__':
    main()
