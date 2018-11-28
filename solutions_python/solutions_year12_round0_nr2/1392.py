def main():
    f = open("input.txt", "r")

    num_test = int(f.readline())
    test_cases = f.readlines()

    test_num = 1
    result = ""
    for i in range(num_test):
        cur_test = test_cases[i].strip().split(" ")

        N = int(cur_test[0])     # number of googler
        S = int(cur_test[1])     # number of surprising triplets
        P = int(cur_test[2])     # cut-line

        temp = 3*P

        rest = cur_test[3:]

        made_cut = 0

        ## should loop N times
        for points in rest:
            found = False

            # check if it makes the cut without being surprising
            for i in range(3):
                if temp-i <= int(points):
                    # makes the cut
                    made_cut += 1
                    found = True
                    break

            if found:
                continue

            ## let it be surprising, and see if makes the cut
            if S > 0 and P >= 2:
                for i in range(3, 5):                        
                    
                    if temp-i <= int(points):
                        S -= 1
                        made_cut += 1
                        break
            
        
        result += "Case #" + str(test_num) + ": " + str(made_cut)
        if test_num < num_test:
            result += "\n"

        test_num += 1

    f2 = open("output.txt", "w")
    f2.write(result)

if __name__ == "__main__":
    main()
