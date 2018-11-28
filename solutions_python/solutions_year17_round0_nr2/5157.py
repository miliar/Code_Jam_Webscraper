def previous_tidy_cycle(n):
    n_to_string=str(n)
    l= len(n_to_string)
    if '0' in n_to_string:
        idx= n_to_string.index('0')
        sub_zero=int(n_to_string[idx:])
        n= n- sub_zero
    n=n-1
    return n


def check_tidy(n):

    n_to_str= str(n)
    for i in range(0, len(n_to_str)-1):
        if int(n_to_str[i]) > int(n_to_str[i+1]):
            return False
    return True


def previous_tidy(n):
    while not check_tidy(n):
        n=previous_tidy_cycle(n)
    return n


if __name__ == '__main__':


    # print previous_tidy(1111111111111111110)
    with open('result.txt','w') as r:
        with open('test.txt') as f:
            N = int(f.readline())
            count = 1
            for line in f:
                tidy = previous_tidy(int(line))
                r.write('Case #' + str(count) + ': ' + str(tidy)+ '\n')
                count += 1
