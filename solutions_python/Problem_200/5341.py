#!/usr/bin/env python3


def tidy(a):
    b = str(a)
    low = int(b[0])
    for i in b:
        z = int(i)
        if z < low:
            return False
        elif z > low:
            low = z
    return True


def main():
    '''Main method
    '''
    with open('tidy_numbers.txt') as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    # data = [4, 132, 1000, 7, 111111111111111110]
    num = int(data[0])
    for i in range(1, num+1):
        top = int(data[i])
        # print(top)
        for z in range(top, 0, -1):
            if tidy(z):
                print("Case #{}: {}".format(i, z))
                break


if __name__ == '__main__':
    main()
