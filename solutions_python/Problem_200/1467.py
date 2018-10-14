t = int(raw_input())  # read a line with a single integer


def is_tidy(num):
    # checks if the number is tidy
    istidy = True
    num_string = str(num)
    for n in range(0, len(num_string)-1):
        if int(num_string[n]) > int(num_string[n+1]):
            istidy = False
    return istidy


for i in xrange(1, t + 1):
    N = int(raw_input())
    string_N = str(N)
    d = 0

    while is_tidy(N)==False:
        N = N - (int(string_N[len(string_N)-(d+1)])+1)*(10**d)
        string_N = str(N)
        d = d + 1

    print "Case #{}: {}".format(i, N)
  # check out .format's