def is_tidy(number):
    n = str(number)
    for i in range(1, len(n)):
        if n[i] < n[i-1]:
            return False
    return True


def main():
    # Get the number of inputs
    t = int(input())

    # Foreach input
    for case in range(1, t + 1):
        # Read a line of the input
        number = int(input())

        # Computing
        while number > 0 and not(is_tidy(number)):
            number -= 1

        # Print the result
        print("Case #{}: {} ".format(case, number))


if __name__ == '__main__':
    main()
