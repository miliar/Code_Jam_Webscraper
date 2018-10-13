



def solve_case(people):
    sitting = sum(people)
    standing = 0
    friends = 0
    #print(people)

    for shy_level, p in enumerate(people):
        if p == 0:
            continue        
        
        if standing >= shy_level:
            standing += p
            sitting -= p
        else:
            #print("shy", 
            new_friends = shy_level-standing
            friends += new_friends
            standing += new_friends + p
            sitting -= p

        #print(shy_level, p, sitting, standing, friends)
        
    return friends



f_in = open("in.txt", "r")
f_out = open("out.txt", "w+")

cases = int(f_in.readline())

for case, line in enumerate(f_in):
    line_in = line[:-1]
    #print(line_in)
    
    s_max_string, shy_string = line_in.split()
    s_max = int(s_max_string)
    shy = [int(c) for c in shy_string]    
    #print(s_max, shy)
    ans = solve_case(shy)

    ans_string = "Case #" + str(case+1) + ": " + str(ans)
    print(ans_string)
    print(ans_string, file=f_out)
    #break


f_in.close()
f_out.close()
