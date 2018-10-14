T = int(input())  # read a line with a single integer
for t in range(1, T + 1):
    N = input()
    digits = [int(i) for i in list(str(N))]

    for i in range(len(digits)-1,0,-1):
        if digits[i] < digits[i-1]:
            digits[i] = 9
            digits[i-1] -= 1
            for j in range(len(digits)-1,i,-1):
                digits[j] = 9

    digits = [str(i) for i in digits]

    print("Case #{}: {}".format(t, str(int("".join(digits)))))