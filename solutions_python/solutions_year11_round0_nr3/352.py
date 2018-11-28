#!/usr/bin/python3

def xor_sum(bag):
    xs = bag[0]
    for candy in bag[1:]:
        xs = xs ^ candy
    return xs

def main():
    cases = int(input())
    for i in range(cases):
        int(input()) # number of candies
        bag = [int(x) for x in input().split()]
        first = min(bag)
        bag.remove(first)
        bag.insert(0, first)
        not_possible = xor_sum(bag)
        if not_possible:
            print('Case #{0}: NO'.format(i+1))
        else:
            print('Case #{0}: {1}'.format(i+1,sum(bag[1:])))

if __name__ == '__main__':
    main()
