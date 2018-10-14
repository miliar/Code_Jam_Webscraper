# Atharv Sonwane


def check_tidy(num):
    n = True
    strn = str(num)
    for j in range(len(strn) - 1):
        if int(strn[j]) > int(strn[j + 1]):
            n = False
            break
    return n


def last_tidy(num):
    while num > 0:
        if check_tidy(num):
            break
        else:
            num -= 1
    return num


def first_dec(num):
    v = - 1
    arr = [int(i) for i in str(num)]
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            v = j + 1
            break
    return v


def to_largest_tidy(num):
    k = first_dec(num)
    if k < 0:
        ans = num
    else:
        arr = [int(i) for i in str(num)]
        arr[k - 1] -= 1
        for a, _ in enumerate(arr[k:]):
            arr[k + a] = 9
        ans = ''
        for i in arr:
            ans += str(i)
    if check_tidy(ans):
        return ans
    else:
        return to_largest_tidy(ans)


def main():
    t = int(input())
    for i in range(t):
        print("Case #%s: %s" % (i + 1, int(str(to_largest_tidy(int(input()))))))


if __name__ == '__main__':
    main()
