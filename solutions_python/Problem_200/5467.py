def lastTidyNumber(num):
    for n in range(num, 0, -1):
        number = n
        tidy_number = True
        last_digit = 9
        for _ in range(len(str(n))):
            digit = n % 10;
            if digit > last_digit:
                tidy_number = False
                break
            last_digit = digit
            n = int((n - digit) / 10)
        if tidy_number == True:
            return number

def main():
    T = int(input().strip())
    numbers = []
    for t in range(T):
        numbers.append(int(input().strip()))
    for t in range(1, T + 1):
        print("Case #{}: {}".format(t, lastTidyNumber(numbers[t-1])))

main()
