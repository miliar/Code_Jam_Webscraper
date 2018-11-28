def is_tidy(digits):
    for i in range(len(digits) - 1):
        if int(digits[i]) > int(digits[i + 1]):
            return False
    return True

f = open('output.txt', 'w')
T = int(input())
for tc in range(T):
    N = input()
    digits = list(N)
    untidy = not is_tidy(digits)
    while untidy:
        if int(N) < 20 and N != "10":
            break
        for i in range(len(digits)-1):
            if int(digits[i]) > int(digits[i+1]):
                sum = 0
                for digit in digits[:i+2]:
                    sum = sum*10 + int(digit)
                sum -= 1
                digits = [int(char) for char in str(sum)] + [9]*(len(digits)-(i+2))
                untidy = not is_tidy(digits)
                break
    ans = ""
    for digit in digits:
        ans += str(digit)
    print("Case #{0}: {1}".format(tc+1, ans))