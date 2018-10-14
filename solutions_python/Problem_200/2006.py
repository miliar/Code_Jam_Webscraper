
def get_last_tidy(number):
    len_nbr = len(number)

    for i in range(len_nbr - 1, 0, -1):
        if number[i - 1] > number[i]:
            number[i - 1] -= 1
            for x in range(i, len_nbr):
                number[x] = 9

    return number


def main():
    nbr_rows = int(input())

    for row_index in range(1, nbr_rows + 1):
        number = list(map(int, input()))
        last_tidy = get_last_tidy(number)
        last_tidy = int(''.join(map(str, last_tidy)))
        print("Case #{row_index}: {last_tidy}".format(
            row_index=row_index, last_tidy=last_tidy))


if __name__ == "__main__":
    main()
