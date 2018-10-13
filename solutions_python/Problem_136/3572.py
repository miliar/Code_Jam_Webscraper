import sys

def recursive_plan(C,F,X,cookies_second,plan,number_seconds,num_iter,max_flag):
    num_iter = num_iter+1
##    if num_iter == 900:
##        max_flag = num_iter
##        plan.append(number_seconds)
##        return max_flag
    if C/cookies_second + X/(cookies_second+F) < X/cookies_second:
        number_seconds = number_seconds + C/cookies_second
        cookies_second = cookies_second + F
        max_flag = recursive_plan(C,F,X,cookies_second,plan,number_seconds,num_iter,max_flag)
        return max_flag
    number_seconds = number_seconds + X/cookies_second
    plan.append(number_seconds)
    return max_flag
    

def problem2(inputfile):
    sys.setrecursionlimit(3000)
    f = open(inputfile,'r')
    lines = f.read().splitlines()
    f.close
    number_examples = int(lines[0])
    o = open("output.txt",'w')
    for i in range(number_examples):
        max_flag = 0
        num_iter = 0
        cookies_second = 2
        number_seconds = 0
        minimum = 0
        plan = []
        plan1 = []
        line = lines[i+1]
        line = str(line).split(' ')
        C = float(line[0])
        F = float(line[1])
        X = float(line[2])
        max_flag = recursive_plan(C,F,X,cookies_second,plan,number_seconds,num_iter,max_flag)
##        if max_flag != 0:
##            cookies_second = cookies_second + max_flag*F
##            recursive_plan(C,F,X,cookies_second,plan1,plan[0],num_iter,0)
##            plan = plan1
        minimum = min(plan)
        o.write("Case #")
        o.write(str(i+1))
        o.write(': ')
        o.write(str(minimum))
        o.write('\n')
    o.close
    return;
