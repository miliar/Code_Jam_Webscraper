def is_tidy(n):
    last = 0
    for i, d in enumerate(n):
        if d < last:
            return i
        last = d
    return -1

def print_dig_list(case, n_lst):
    n = ''.join(map(str, n_lst)).lstrip('0')
    print("Case #{}: {}".format(case, n))

def main():
    T = int(input())
    for case in range(1, T + 1):
        N = [int(digit) for digit in input()]
        
        first_incor = is_tidy(N)
        if first_incor == -1:
            print_dig_list(case, N)
            continue


        for i in range(len(N) -1, 0, -1):
            # print(N)
            if i >= first_incor or N[i - 1] > N[i]:
                N[i] = 9
                N[i - 1] -= 1
            else:
                break

        print_dig_list(case, N)


if __name__ == '__main__':
    main()
