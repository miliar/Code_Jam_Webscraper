def procEachCase(X,R,C):
    #print(str_case)
    g_ans = "GABRIEL"
    r_ans = "RICHARD"

    #print(X,R,C)
    if X==1:
        return g_ans
    elif X >=7:
        return r_ans
    elif (R*C < X) | (R*C % X >0):
        return r_ans
    elif (R*C == X) & (R*C % X==0):
        if(X <=2):
            return g_ans
        else:
            return r_ans
    elif (R*C == 2*X) & (R*C %X == 0):
        if(X <= 3):
            return g_ans
        else :
            return r_ans
    else:
        return g_ans


#---- main code here
filepath = "D-small-attempt5.in"
anspath = "answer"

file = open(filepath,'r')
ans_file = open(anspath,'w')

str_T = file.readline()
T = int(str_T)
print(T)
for i in range(1,T+1):
    print(i)
    str_case = file.readline()
    case_pars = str_case.split(" ")
    X = int(case_pars[0])
    R = int(case_pars[1])
    C = int(case_pars[2])
    answer = procEachCase(X,R,C)
    ans_file.write("Case #%d: %s\n" %(i,answer))
    #ans_file.write("%d,%d,%d, Case #%d: %s\n" %(X,R,C,i,answer))

ans_file.close()
file.close()

#print(procEachCase(3,1,3))

