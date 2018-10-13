import string

in_file = open("A-small.in","r");
out_file = open("A-small.out","w");

case_num = 0;
case_max = 0;

a = 0
b = 0

for line in in_file:
    if (case_max == 0):
        case_max = str(line)
        case_num = 1
        continue
    if (a == 0):
        split_line = line.split(" ")
        a = int(split_line[0])
        b = int(split_line[1])
        continue
    print "START CASE # {0}".format(case_num)
    prob = []
    for num in line.split(" "):
        prob.append(float(num))
    
    backstrokes = [0] * (a+1)
        
    print prob
    naive = b + 2 # if we just press enter
    for num in range(0,2**(a)):
        # if 2^i digit is on, then we typed the character correctly
        this_prob = 1.0
        found_zero = 0
        best_len = 0
        for x in range(0,a):
            print "character {0}".format(x+1)
            #print "prob[x]: {0}".format(prob[x])
            print "this prob: {0}".format(this_prob)
            print "character matcher: {0}".format(int(2**(x)))
            if num & int(2**(x)):
                #print "buggy"
                #print this_prob
                #print this_prob * prob[x]
                this_prob = float(this_prob) * float(prob[x])
                #print this_prob
                if (found_zero == 0):
                    best_len+=1
            else:
                #print "buggy2"
                #print this_prob
                #print this_prob * prob[x]
                #print (1.0 - prob[x])
                this_prob = this_prob * float(1.0 - prob[x])
                #print this_prob
                found_zero = 1
        print "this_prob found: {0} - {1}".format(num,this_prob)
        #print "num: {0}".format(num)
        for z in range(0,a+1):
            tmp = (z + (b - a + z) + 1) 
            if (a - z > best_len):
                tmp += b + 1 
            print "tmp{0}: {1}".format(z,tmp*this_prob)
            backstrokes[z] += float(tmp) * float(this_prob)
    print "done w/ strokes calc"
    print backstrokes
    backstrokes.append(b+2)
    newline = str(min(backstrokes))
    print newline
    out_file.write("Case #"+str(case_num)+": "+newline+"\n")
    case_num += 1
    a = 0
