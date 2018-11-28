def readint(stream):
    return int(stream.next()[:-1])


def main():
    nums = []

    with open('input.txt', 'r') as f:
        count = readint(f)
        for i in range(count):
            nums.append(readint(f))

    with open('output.txt', 'w') as f:
        for index, num in enumerate(nums):
            f.write("Case #{}: {}\n".format(index + 1, solve(num)))


def solve(num):
    if num < 10:
        return num

    s = [x for x in str(num)]
    i = len(s) - 1
    while i > 0:
        if s[i] < s[i-1]:
            for j in range(i, len(s)):
                s[j] = '9'
            s[i-1] = chr(ord(s[i-1]) - 1)
        i -= 1
    return int(''.join(s))


if __name__=='__main__':
    main()