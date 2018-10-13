def solve(num):
    if len(num) == 1:
        return num
    peak = 0
    for i in range(1, len(num)):
        if num[i] > num[i - 1]:
            peak = i
        elif num[i] < num[i - 1]:
            break
    else:
        return num
    return (num[:peak] + str(int(num[peak]) - 1) + '9' * (len(num) - peak - 1)).lstrip('0')



def main():
    T = input()
    for i in xrange(1, T + 1):
        num = raw_input().strip()
        print 'Case #{0}: {1}'.format(i, solve(num))

if __name__ == '__main__':
    main()
