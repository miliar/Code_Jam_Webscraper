def make_array(n):
    a = []
    s = n
    while s > 0:
        a.append(s%10)
        s /= 10
    a.reverse()
    return a

def is_tidy(check_array):
     for i in xrange(len(check_array)-1):
         if check_array[i] > check_array[i+1]:
             return i
     return -1

if __name__ == "__main__":
    t = int(raw_input())  # read a line with a single integer
    for i in xrange(1, t + 1):
        n = int(raw_input())
        array = make_array(n)
        while  (is_tidy(array) != -1):
            k = is_tidy(array)
            j = len(array) - (k+1)
            n = int(n/(10**j))
            n = n * 10**j - 1
            array = make_array(n)


        # read a list of integers, 2 in this case
        print "Case #{}: {}".format(i, n)
      # check out .format's specification for more formatting options
