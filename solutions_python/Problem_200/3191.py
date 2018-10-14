def last_tidy_number(n_str):
    if len(n_str) <= 1:
        return n_str
    # find the first untidy digit
    for idx in range(1, len(n_str)):
        if int(n_str[idx]) >= int(n_str[idx - 1]):
            continue
        # find the last tidy number no larger than (first part minus one)
        first_part = last_tidy_number(str(int(n_str[0:idx]) - 1))
        if first_part == "0":  first_part = ""
        return first_part + "9" * (len(n_str) - idx)
    return n_str


def main():
    """The main driver"""
    n_tests = int(input())
    for i in range(n_tests):
        n_str = input()
        output = last_tidy_number(n_str)
        print("Case #{}: {}".format(i + 1, output))


if __name__ == "__main__":
    main()
