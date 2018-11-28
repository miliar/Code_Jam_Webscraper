import collections as co
numbs = 'zero,one,two,three,four,five,six,seven,eight,nine'.split(',')

def minus(c, iters, num):
    for i in iters:
        c[i] -= num
    return c

def solve(idx, data):
    count = co.Counter(data)

    zero = count['Z']
    count = minus(count, 'ZERO', zero)

    two = count['W']
    count = minus(count, 'TWO', two)

    eight = count['G']
    count = minus(count, 'EIGHT', eight)

    three = count['H']
    count = minus(count, 'THREE', three)

    four = count['R']
    count = minus(count, 'FOUR', four)

    five = count['F']
    count = minus(count, 'FIVE', five)

    seven = count['V']
    count = minus(count, 'SEVEN', seven)

    six = count['X']
    count = minus(count, 'SIX', six)

    one = count['O']
    count = minus(count, 'ONE', one)

    nine = count['E']
    count = minus(count, 'NINE', nine)
    dic = locals()

    string=''.join([str(i)*dic.get(k)for i,k in enumerate(numbs) if dic.get(k)])
    print("Case #{}: {}".format(idx+1,string))


def main():
    num = int(input())
    for p_idx in range(num):
        solve(p_idx, input())

if __name__ == '__main__':
    main()
