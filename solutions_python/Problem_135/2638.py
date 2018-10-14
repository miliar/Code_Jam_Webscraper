#!/usr/bin/python


def get_set():
    row = int(raw_input())
    grid = []
    for i in xrange(4):
        grid.append([])
        nums = raw_input().split()
        for j in xrange(len(nums)):
            grid[i].append(int(nums[j]))

    my_set = set()
    for i in range(4):
        my_set.add(grid[row-1][i])

    return my_set


def main():
    T = int(raw_input())
    for t in xrange(T):
        set1 = get_set()
        set2 = get_set()
        set3 = set1 & set2

        case = "Case #{}: ".format(t+1)

        if len(set3) == 0:
            print case + "Volunteer cheated!"
        elif len(set3) == 1:
            print case + str(set3.pop())
        else:
            print case + "Bad magician!"

if __name__ == '__main__':
    main()
