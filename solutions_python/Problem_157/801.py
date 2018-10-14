def dijkstra(string):
    #Note it's not commutative, so I simply can pluck
    #elements from the left until I get i,
    #then j, then k. If anything reduces to 1, then I can just ignore it,
    #as it doesn't matter which side it goes on.
    i = 0
    acc = "1"
    while acc != "i":
        if i>=len(string):
            return False
        acc = quat_mul(acc, string[i])
        i+=1
    acc = "1"
    while acc != "j":
        if i>=len(string):
            return False
        acc = quat_mul(acc, string[i])
        i+=1
    acc = "1"
    while acc != "k":
        if i>=len(string):
            return False
        acc = quat_mul(acc, string[i])
        i+=1
    acc = "1"
    while i<len(string):
        acc = quat_mul(acc, string[i])
        i+=1
    if(acc!="1"):
        return False
    return True
        

def quat_mul(s1, s2):
    #precondition: s2 is positive
    if s1 == "1":
        return s2
    elif s1 == "-1":
            return "-"+s2
    elif s1 == "i":
        if s2=="1":
            return "i"
        elif s2=="i":
            return "-1"
        elif s2=="j":
            return "k"
        else:
            return "-j"
    elif s1 == "j":
        if s2=="1":
            return "j"
        elif s2=="i":
            return "-k"
        elif s2=="j":
            return "-1"
        else:
            return "i"
    elif s1 == "k":
        if s2=="1":
            return "k"
        elif s2=="i":
            return "j"
        elif s2=="j":
            return "-i"
        else:
            return "-1"
    else:
        second_part = quat_mul(s1[1], s2)
        if second_part[0] == "-":
            second_part = second_part[1]
        else:
            second_part = "-" + second_part
        return second_part




#main
Input = open("C-small-attempt0.in", "r")
Output = open("C_out.out", "w")
num_cases = int(Input.readline()[:-1])
for i in range(num_cases):
    params = Input.readline()[:-1]
    string = Input.readline()[:-1]
    x = int(params.split(" ")[1])
    if dijkstra(string*x):
        Output.write("Case #"+str(i+1)+": YES\n")
    else:
        Output.write("Case #"+str(i+1)+": NO\n")
    
Input.close()
Output.close()
