#------------------------------------------------------------------------
#Solve function
#------------------------------------------------------------------------
def flip_cake(i_list, start, k):
    flip_list = i_list[start:start+k]
    for i in range(0, k):
        if flip_list[i] == "+":
            flip_list[i] = "-"
        else:
            flip_list[i] = "+"
    i_list[start:start+k] = flip_list

def solve(i_str_list):
    s = i_str_list[0]
    k = int(i_str_list[1])
    char_list = []
    for c in s:
        char_list.append(c)
        
    n = 0
    for i in range(0, len(char_list)-k+1):
        if char_list[i] != "+":
            flip_cake(char_list, i, k)
            n = n + 1;

    for i in range(len(char_list)-k+1, len(char_list)):
        if char_list[i] != "+":
            return "IMPOSSIBLE"
    
    return n
#------------------------------------------------------------------------
#Simple tests
#------------------------------------------------------------------------
if False:
    simple_test_input = "++-+-"
    
    test_list = []
    int_list  = []
    int_list.append(simple_test_input)
    int_list.append(3)
    test_list.append(int_list)

    print(solve(test_list[0]))

#------------------------------------------------------------------------
#Read Code Jam input file for integers and Write output
#------------------------------------------------------------------------
if True:
    t = int(raw_input())
    test_list = []
    for i in range(0, t):
        string_list = []
        for s in raw_input().split(" "):
            string_list.append(s)
        test_list.append(string_list)
#------------------------------------------------------------------------
        n = solve(test_list[i])
#------------------------------------------------------------------------
        #Write to output file
        print(("Case #{}: {}").format(i+1, n)) 

