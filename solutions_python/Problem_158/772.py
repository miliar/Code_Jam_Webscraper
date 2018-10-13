output = ""
file = open('in','r')
cases = int(file.readline())


NOFIT = 0
FIT = 1
def case(case_no, fit):
    global output
    output += ("Case #{}: {}\n".format(case_no+1, "GABRIEL" if fit == FIT else "RICHARD"))
def d(msg):
    #print(msg)
    return


for case_no in range(cases):
    line = file.readline().split()
    x = int(line[0])
    r = int(line[1])
    c = int(line[2])
    
    d("X: {} R: {} C: {}".format(x,r,c))
    
    if(x == 1):
        case(case_no, FIT)
        continue
    if ((r * c) / x) != int((r * c) / x):
        case(case_no, NOFIT)
        continue
    if(x == 2):
        case(case_no, FIT)
        continue
    if(r == 1 or c == 1):
        case(case_no, NOFIT)
        continue
    if(x > r and x > c):
        case(case_no, NOFIT)
        continue
    if(x == 3):
        case(case_no, FIT)
        continue
    if not (r * c >= 3*4):
        case(case_no, NOFIT)
        continue
    case(case_no, FIT)
    

out_file = open("out","w")
out_file.truncate(0);
out_file.write(output)


print(output)