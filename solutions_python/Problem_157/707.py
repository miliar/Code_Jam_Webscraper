DEBUG = 0

def mul (s1,s2):
    if s1[0] == '-' and s2[0] == '-':
        return mul(s1[1:],s2[1:])
    if s1[0] == '-' and s2[0] != '-':
        tmp = mul(s1[1:],s2)
        if tmp[0] == '-':
            return tmp[1:]
        else:
            return "-"+tmp
    if s1[0] != '-' and s2[0] == '-':
        tmp = mul(s1,s2[1:])
        if tmp[0] == '-':
            return tmp[1:]
        else:
            return "-"+tmp
    
    if s1 == "1":
        if s2 == "1":
            return "1"
        elif s2 == "i":
            return "i"
        elif s2 == "j":
            return "j"
        else:
            return "k"
    elif s1 == "i":
        if s2 == "1":
            return "i"
        elif s2 == "i":
            return "-1"
        elif s2 == "j":
            return "k"
        else:
            return "-j"
    elif s1 == "j":
        if s2 == "1":
            return "j"
        elif s2 == "i":
            return "-k"
        elif s2 == "j":
            return "-1"
        else:
            return "i"
    elif s1 == "k":
        if s2 == "1":
            return "k"
        elif s2 == "i":
            return "j"
        elif s2 == "j":
            return "-i"
        else:
            return "-1"


read_file = open('C-small-attempt1.in','r')

n_cases = int(read_file.readline())

#n_cases = int(raw_input())

for i in range(n_cases):
    #lst = raw_input().split(" ")
    lst = read_file.readline().split(" ")

    L = int(lst[0])
    X = int(lst[1])

    thestring = read_file.readline()

    string = ""

    for tm in range(X):
        string += thestring[:len(thestring)-1]

    index_i = 0
    index_k = len(string)-1

    i_string = ""
    j_string = ""
    k_string = ""

    result = "1"

    if DEBUG == 1:
        print("i string")

    while result != "i" and index_i < len(string)-2:
        result = mul(result,str(string[index_i]))
        if DEBUG == 1:
            print(result)
        i_string += str(string[index_i])
        index_i += 1

    if result != "i":
        print("Case #"+str(i+1)+": NO")
        continue

    result = "1"

    if DEBUG == 1:
        print("k string")
        
    while result != "k" and index_k > index_i:
        if DEBUG == 1:
            print(str(string[index_k]),result)
        result = mul(str(string[index_k]),result)
        if DEBUG == 1:
            print(result)
        k_string = str(string[index_k])+k_string
        index_k -= 1

    if result != "k":
        print("Case #"+str(i+1)+": NO")
        continue

    index_k += 1

    result = "1"

    if DEBUG == 1:
        print("j string")
        
    for index in range(index_i, index_k):
        result = mul(result,str(string[index]))

    if result != "j":
        print("Case #"+str(i+1)+": NO")
    else:
        print("Case #"+str(i+1)+": YES")
