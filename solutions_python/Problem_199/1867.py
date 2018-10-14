HAPPY_SIDE = True
BLANK_SIDE = False


def flip(row, flipper_size, index):
    for x in range(flipper_size):
        try:
            row[index + x] = HAPPY_SIDE if row[index + x] == BLANK_SIDE else BLANK_SIDE
        except IndexError:
            return


def get_nbr_flips(row, flipper_size):
    counter = 0
    for i in range(len(row) - flipper_size + 1):
        if row[i] == BLANK_SIDE:
            flip(row, flipper_size, i)
            counter += 1
    if any(x == BLANK_SIDE for x in row):
        return "IMPOSSIBLE"
    else:
        return counter


def main():
    nbr_rows = int(input())

    for nbr_row in range(1, nbr_rows + 1):
        row, flipper_size = input().split()
        row = [char == "+" for char in row]
        flipper_size = int(flipper_size)
        nbr_flips = get_nbr_flips(row, flipper_size)
        print("Case #{nbr_rows}: {nbr_flips}".format(
            nbr_rows=nbr_row, nbr_flips=nbr_flips))


if __name__ == "__main__":
    main()
