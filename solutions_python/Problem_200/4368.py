def is_tidy(n):
    last = 9
    while n > 0:
        if last < (n % 10):
            return False

        last = n % 10
        n //= 10

    return True

def main():
    t = int(input())

    for j in range(t):

        number = int(input())
        n = number
        last = 9

        while n > 0:
            if last < (n % 10):
                number -= (number % 10) + 1
                n = number

            last = n % 10
            n //= 10


        print("Case #{}:".format(j+1), number)

main()