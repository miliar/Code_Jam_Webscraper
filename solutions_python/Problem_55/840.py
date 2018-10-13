from collections import deque
from copy import copy

def calc_amount(r, k, n, queue):
    amount = 0
    nrides = 0
    while nrides < r:
        ride = 0
        groups = 0
        while groups < n and ride + queue[groups] <= k:
            ride += queue[groups]
            groups += 1
        queue.rotate(-groups)
        nrides += 1
        amount += ride

    return amount

def main():
    ifile = open('C-small-attempt0.in')
    ofile = open('C-small-attempt0.out', 'w')
    ncases = int(ifile.readline())

    for i in range(ncases):
        test_case = ifile.readline().strip().split()
        r = int(test_case[0])
        k = int(test_case[1])
        n = int(test_case[2])
        groups_str = ifile.readline().strip().split()
        groups = [int(group) for group in groups_str]
        ofile.write('Case #%d: %s\n' % (i + 1, calc_amount(r, k, n, deque(groups))))

    ifile.close()
    ofile.close()

if __name__ == '__main__':
    main() 
