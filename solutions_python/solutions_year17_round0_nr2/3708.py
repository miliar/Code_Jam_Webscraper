
def check_tidy(string):
    return all( int(d1) <= int(d2) for d1, d2 in zip(string[:-1],string[1:] ))

t = int(input())  # read a line with a single integer
for i in range(1, t + 1):

    n  = int(input())
    n_str = str(n)

    ret_string = ""

    while not check_tidy(n_str):
        last_digit = int(n_str[-1])
        n = int(n_str) - ( last_digit + 1 )
        ret_string = '9' + ret_string

        n_str = str(n)[:-1]

    ret_string = n_str + ret_string
    print("Case #{}: {}".format(i, ret_string))
