def calc_next(n):
    n_list = [int(x) for x in list(str(n))]
    n_list.reverse()
    print n_list
    # first we find the first non monotonic digit
    index = 0
    size = len(n_list)
    found = False
    while (index + 1< size) and (n_list[index] <= n_list[index + 1]):
        index += 1
        
    if index < size - 1: # meaning n_list[size] > n_list[size + 1]
        # we start to change the number stating from size + 1
        # The smallest number after it, we comes in
        rest = n_list[0 : index + 1]
        print "Rest is",  str(rest)
        # we need to find the smallest number in there, that is bigger than n_list[size + 1]
        # there is at least one of those
        my_num = n_list[index + 1]
        remain = [x for x in rest if x > my_num]
        
        next_leading_digit = min(remain)
        print "next leading", str(next_leading_digit)
        rest.remove(next_leading_digit)
        rest.append(my_num)
        rest.sort()
        rest.reverse()
        print "Rest is now", str(rest)
        print "what's left of the list", str(n_list[(index + 2):])
        all = rest + [next_leading_digit] + n_list[(index + 2):]
        all.reverse()
        final = "".join(str(x) for x in all)
        return final
    else:
        save_list = n_list[:]
        save_list.append(0)
        n_list.sort()
    
        # help save zeros
        how_many_zeroes = save_list.count(0)
        while 0 in save_list:
            save_list.remove(0)
        
        new_list = [save_list[0]] + [0] * how_many_zeroes +save_list[1:]
        
        final2 = int("".join(str(x) for x in new_list))
        
        return final2
            
def main():
    bla = r"D:\Project CodeJam\Test\ddd.in"
    
    f = open(bla)
    lines = f.readlines()
    f.close()

    f_write = open(r"D:\Project CodeJam\Test\roubdboutput.txt", "w")

    num_rows = int(lines[0])
    
    for test_case_index in range(1, num_rows + 1):
        test_case = lines[test_case_index]
        s = calc_next(int(test_case))
        new_str = "Case #%d: %s\n" % (test_case_index, str(s))
        f_write.write(new_str)
    f_write.close()
    print "Done"
    
main()
#print calc_next(50000)

