def getTidyNum(n):
    found_tidy = False
    while n >= 0 and not found_tidy:
        n_str = str(n)
        if len(n_str) == 1:
            found_tidy = True
        else:
            for j in xrange(1, len(n_str)):
                if int(n_str[j-1]) > int(n_str[j]):
                    found_tidy = False
                    n -= 1
                    break
                elif j == len(n_str)-1:
                    found_tidy = True
    return n

input_size = input()

for i in xrange(input_size):
    print "Case #%d:"%(i+1), getTidyNum(input())
