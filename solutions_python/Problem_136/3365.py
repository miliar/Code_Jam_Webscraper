def str_to_int(s):
    ints = []
    s += " "
    c = 0        
    for i in range(len(s)):
        if s[i] == " ":
             ints.append(float(s[c:i]))
             c = i
    return ints

def make_output(x):
    case_output = "Case #" + str(case) + ": " + str(x) + "\n"
    return case_output

case = 1
final_output =""
T = int(input())
for i in range(T):

    C_F_X = str_to_int(input(str()))
    C = C_F_X[0]
    F = C_F_X[1]
    X = C_F_X[2]
    no_of_farms = 1
    pre_time = X/2
    time = C/2 + X/(2+F)
    
    while pre_time > time:
        time_taken_to_build_farms = 0
        no_of_farms += 1
        pre_time = time
        for i in range(no_of_farms):
            time_taken_to_build_farms += C/(2 + i * F)
        time = time_taken_to_build_farms + X/(2 + no_of_farms * F)
              
                            
    final_output += make_output(pre_time)
    case += 1
print(final_output)

