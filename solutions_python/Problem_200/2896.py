def tidy_number(numbers):
    if len(numbers) == 1:
        return int(''.join(numbers))
    big_idx = 0
    for i in range(1, len(numbers)):
        if numbers[i] > numbers[i-1]:
            big_idx = i
        elif numbers[i] < numbers[i-1]:
            numbers[big_idx] = str(int(numbers[big_idx]) - 1)
            for j in range(big_idx+1, len(numbers)):
                numbers[j] = '9'
            break
    return int(''.join(numbers))


if __name__ == '__main__':
    t = int(raw_input())
    for i in xrange(1, t + 1):
        n = raw_input()
        print "Case #{}: {}".format(i, tidy_number(list(n)))
