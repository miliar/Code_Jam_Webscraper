def largest_tidy_number(N):
    """
    Return the highest "tidy" number smaller or equal to N
    A tidy number is a number in which all digits are non-decreasing from left to right. 
    :param N: The largest number to check
    :return: The largest tidy number
    """
    if is_tidy(N):
        return N
    s = str(N)
    # If there is an untidiness between digit i and i+1, remove it by dimishing digit i by 1 and putting all 9s after
    # This is equivalent to removing everything that comes after digit i, and then removing again 1
    # However, if digit i is the same as before, then an untidiness will arise between i-1 and i
    # One should then remove everything coming after i-1 and 1 more
    # This is taken into account by the digit k that keeps track of how many equal numbers in a row we have found
    k = 0
    for i in range(len(s) - 1):
        if s[i + 1] > s[i]:  #
            k = 0
        if s[i + 1] == s[i]:
            k += 1
        if s[i + 1] < s[i]:
            mod = 10**(len(s) + k - i - 1)
            return N - N % mod - 1

def is_tidy(x):
    """
    A number whose tidiness we have to check.
    A tidy number is a number in which all digits are non-decreasing from left to right.
    :param x: 
    :return: boolean, true or false
    """
    if x < 10:
        return True  # All numbers with just one digit are tidy

    s = str(x)
    return all(s[i+1] >= s[i] for i in range(len(s)-1))

with open("./B-large.in", "r") as fin:
    with open("./B-large.out", "w+") as fout:
        T = int(fin.readline().strip("\n"))

        for i in range(T):
            N = int(fin.readline().strip("\n"))
            res = largest_tidy_number(N)
            fout.write("Case #%d: %d\n" % (i + 1, res))
