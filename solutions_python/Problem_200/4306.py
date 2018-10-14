def tidy(N):
    digits = list(str(N))
    for i in range(len(digits)-1, 0, -1):
        prev, cur = int(digits[i-1]), int(digits[i])
        if prev > cur:
            digits[i-1] = str(prev-1)
            for j in range(i, len(digits)):
                if digits[j] == '9':
                    break
                digits[j] = '9'

    return int(''.join(digits))

if __name__ == "__main__":
    T = int(raw_input())  # read a line with a single integer
    for i in range(T):
        N = int(raw_input())
        print "Case #{}: {}".format(i+1, tidy(N))
