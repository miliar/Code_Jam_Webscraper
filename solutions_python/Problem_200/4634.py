def ham(text):
    if text.count('1') == len(text):
        return '9' * (len(text) - 1)
    elif len({x for x in text}) == 1:
        return str(int(text[0]) - 1) + '9' * (len(text) - 1)
    else:
        tmp = text[-1]
        return text.replace(tmp, str(int(tmp) - 1))


def spam(num):
    old = 0
    ans = ''
    for n in [int(x) for x in str(num)]:
        if n < old:
            ans = ham(ans) + '9' * (len(str(num)) - len(ans))
            break
        else:
            ans += str(n)
        old = n
    return int(ans)


def main():
    with open('B-small-attempt0.in') as f:
        T = int(f.readline()[:-1])
        for i in range(T):
            print('Case #{0}: {1}'.format(i + 1, spam(int(f.readline()[:-1]))))


if __name__ == '__main__':
    main()
