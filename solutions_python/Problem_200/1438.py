def tidy_number(n):
    for i in range(0, len(n)-1):
        a = int(n[i+1])
        b = int(n[i])
        if a < b:
            n[i]   = str(b-1)
            for j in range(i+1, len(n)):
                n[j] = str(9)
            tidy_number(n)
            break
    
#------------------------------------------------------------------------
#Solve function
#------------------------------------------------------------------------
def solve(i_int_list):
    s = i_int_list[0]

    char_list = []
    for c in s:
        char_list.append(c)
    
    if len(char_list) == 1:
        return s

    tidy_number(char_list)

    s = ""
    for a in char_list:
        s = s + a

    if s[0] != "0":
        return s
    else:
        return s[1:]
    
#------------------------------------------------------------------------
#Simple tests
#------------------------------------------------------------------------
if False:
    simple_test_input = "1110"
    
    test_list = []
    int_list  = []
    int_list.append(simple_test_input)
    test_list.append(int_list)

    print(solve(test_list[0]))
#------------------------------------------------------------------------
#Read Code Jam input file for integers and Write output
#------------------------------------------------------------------------
if True:
    t = int(raw_input())
    test_list = []
    for i in range(0, t):
        int_list = []
        for s in raw_input().split(" "): #split(",")
            int_list.append(s)
            test_list.append(int_list)
        #*****
        res = solve(test_list[i])
        #*****
        #Write to output file
        print(("Case #{}: {}").format(i+1, res))
