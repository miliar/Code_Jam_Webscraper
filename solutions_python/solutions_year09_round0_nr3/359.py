TEXT = "welcome to code jam"
#some_str = "elcomew elcome to code jam"


def do_it(some_str):
    save = [{} for i in range(len(TEXT))]
    count = 0
    
    # Initiaitiatino for the suffix which is only one letter
    for index in range(len(some_str) -1, -1, -1):
        # If the letter on which were stannding on in the TEXT is the actual letter
        if some_str[index] == TEXT[-1]:
            count += 1
        save[0][index] = count
    
    len_mes = len(some_str)
    for len_suffix in range(1, len(TEXT)):
        save[len_suffix][len(some_str) - 1] = 0
        sum = 0
        for index in range(len(some_str) - 2, -1, -1):
            # If the letter on which were stannding on in the TEXT is the actual letter
            if some_str[index] == TEXT[- len_suffix - 1]:
                save[len_suffix][index] = save[len_suffix - 1][index + 1] + sum
            else:
                save[len_suffix][index] = sum
            sum = save[len_suffix][index]
    
    return  save[len(TEXT) - 1][0]
    
def fix(n):
    if n < 10:
        return "000" + str(n)
    if n < 100:
        return "00" + str(n)
    return "0" + str(n)

def main():
    bla = r"D:\Project CodeJam\Test\C-small-attempt0.in"
    #bla = r"D:\Project CodeJam\Test\1.txt"
    
    f = open(bla)
    lines = f.readlines()
    f.close()

    f_write = open(r"D:\Project CodeJam\Test\output31.txt", "w")

    num_rows = int(lines[0])
    
    for test_case_index in range(1, num_rows + 1):
        test_case = lines[test_case_index]
        s = fix(do_it(test_case) % 1000)
        new_str = "Case #%d: %s\n" % (test_case_index, s)
        f_write.write(new_str)
    f_write.close()
    print "Done"
    
main()