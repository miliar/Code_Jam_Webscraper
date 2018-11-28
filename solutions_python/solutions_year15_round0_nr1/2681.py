#!/usr/bin/env python2


def main():
    cases = int(raw_input())
    for case in range(cases):
        up_so_far = 0
        friends = 0
        s_max, shynesses = raw_input().split()
        for shyness, count_str in enumerate(shynesses):
            if up_so_far < shyness:
                friends += shyness - up_so_far
                up_so_far = shyness
            up_so_far += int(count_str)
        print("Case #{}: {}".format(case + 1, friends))


if __name__ == "__main__":
    main()
