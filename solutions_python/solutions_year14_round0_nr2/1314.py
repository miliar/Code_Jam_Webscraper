import sys
sys.setrecursionlimit(50000) #this is not needed by time2
def time(C, F, X, rate):
    if C >= X:
        return X/rate
    if (C/rate + X/(F+rate)) >= X/rate:
        return X/rate
    return C/rate + min((X-C)/rate, time(C, F, X, rate+F))

def time2(C, F, X, rate):
    if C>=X:
        return X/rate
    #bad estimate
    fixed_part = C/rate
    other_part = (X-C)/rate
    t = fixed_part + other_part
    condition = True
    while(condition):
        rate += F
        fixed_part = fixed_part + C/(rate)
        other_part = (X-C)/rate
        t_new = fixed_part + other_part
        condition = t_new < t
        if condition: t = t_new
    return t

if __name__ == "__main__":
    output_file = open("%s.%s"%(sys.argv[1].split(".")[0],"out"),"w")
    file_name = sys.argv[1]
    input_file = open(file_name)
    case_count = int(input_file.readline())
    for i in xrange(case_count):
        C, F, X = map(float, input_file.readline().strip().split(" "))
        #result = time(C, F, X, 2)
        result_2 = time2(C, F, X, 2)
        output_file.write("Case #%s: %.7f\n"%(i+1, result_2))
    output_file.close()
    input_file.close()
    print "Done!"