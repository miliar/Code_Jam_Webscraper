def main():
    t = int(input())
    for i in range(1, t + 1):
        n = input()
        print_tidy(n, i)


def print_tidy(n, case):
    tidy = n
    if len(n) > 1:
        while not is_tidy(tidy):
            tidy = find_tidy(tidy)
    print("Case #" + str(case) + ": " + tidy)


def is_tidy(n):
    number_list = [x for x in n]
    sorted_list = sorted(number_list)
    if number_list == sorted_list:
        return True
    return False


def find_tidy(n):
    index = index_of_small(n)
    if n[index] == '1':
        index = index + 1
    first_half = int(n[:index + 1]) - 1
    second_half = n[index + 1:]
    return str(first_half) + '9' * len(second_half)


def index_of_small(n):
    counter = 0
    while counter < len(n)-1:
        if n[counter] > n[counter + 1]:
            return counter
        counter += 1
if __name__ == '__main__':
    main()
