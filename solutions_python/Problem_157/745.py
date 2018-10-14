import math
f = open('CInput.txt')
lines = f.readlines()
f.close()

def q_m(chr1, chr2):
    if(chr1 == "1"):
        return chr2
    elif(chr2 == "1"):
        return chr1
    elif((chr2 == "i") and (chr1 == "i")):
        return "-1"
    elif((chr2 == "j") and (chr1 == "i")):
        return "k"
    elif((chr2 == "k") and (chr1 == "i")):
        return "-j"
    elif((chr2 == "i") and (chr1 == "j")):
        return "-k"
    elif((chr2 == "j") and (chr1 == "j")):
        return "-1"
    elif((chr2 == "k") and (chr1 == "j")):
        return "i"
    elif((chr2 == "i") and (chr1 == "k")):
        return "j"
    elif((chr2 == "j") and (chr1 == "k")):
        return "-i"
    elif((chr2 == "k") and (chr1 == "k")):
        return "-1"
    else:
        print "ERROR"

def q_mult(string):
    if(len(string)==1):
        return string
    else:
        tmp = q_m(string[0], string[1])
        for i in range(len(string)-2):
            if(tmp[0] == "-"):
                tmp = q_m(tmp[1], string[i+2])
                if(tmp[0] == "-"):
                    tmp = tmp[1] #negatives cancel
                else:
                    tmp = "-" + tmp
            else:
                tmp = q_m(tmp, string[i+2])
        return tmp

output = open('COutput.txt','w')

for i in range(int(lines[0])):
#for i in range(8):
    X = int(lines[2*i+1].split()[1])
    Chars = lines[2*i+2].strip()
    C_rep = ""
    for j in range(X):
        C_rep += Chars
    
    print "chars",
    print Chars
    print "C_rep ",
    print C_rep
    print "X: ",
    print X
    answer = "No"
    k_pivot = -1
    i_pivot = -1
    if(len(C_rep) < 3):
        answer = "No"
    else:
        tmp = C_rep[0]
        for j in range(len(C_rep)-2):
            #print tmp
            if(tmp == "i"):
                #print "found it!"
                i_pivot = j
                break
            if(tmp[0] == "-"):
                tmp = q_m(tmp[1], C_rep[j+1])
                if(tmp[0] == "-"):
                    tmp = tmp[1] #negatives cancel
                else:
                    tmp = "-" + tmp
            else:
                tmp = q_m(tmp, C_rep[j+1])
        tmp = C_rep[-1]
        for k in range(len(C_rep)-2):
            #print tmp
            if(tmp == "k"):
                #print "found k!"
                k_pivot = k
                break
            if(tmp[0] == "-"):
                tmp = q_m(C_rep[-k-2], tmp[1])
                if(tmp[0] == "-"):
                    tmp = tmp[1] #negatives cancel
                else:
                    tmp = "-" + tmp
            else:
                tmp = q_m(C_rep[-k-2], tmp)
        print i_pivot
        print k_pivot
        if((k_pivot != -1) and (i_pivot != -1) and (i_pivot < len(C_rep) - k_pivot - 2)):
            tmp = C_rep[i_pivot+1]
            for l in range(i_pivot+2, len(C_rep)-k_pivot-1):
                if(tmp[0] == "-"):
                    tmp = q_m(tmp[1], C_rep[l])
                    if(tmp[0] == "-"):
                        tmp = tmp[1] #negatives cancel
                    else:
                        tmp = "-" + tmp
                else:
                    tmp = q_m(tmp, C_rep[l])
            if(tmp == "j"):
                answer = "Yes"
            print C_rep[0:i_pivot+1]
            print q_mult(C_rep[0:i_pivot+1])
            print C_rep[i_pivot+1:len(C_rep)-k_pivot-1]
            print q_mult(C_rep[i_pivot+1:len(C_rep)-k_pivot-1])
            print C_rep[len(C_rep)-k_pivot-1:len(C_rep)]
            print q_mult(C_rep[len(C_rep)-k_pivot-1:len(C_rep)])
        #for j in range(len(C_rep)-2):
            ##print "J ",
            ##print j
            #sub_i = C_rep[0:j+1]
            #if(q_mult(sub_i) == "i"):
                #for k in range(len(C_rep)-j-2):
                    ##print "K ",
                    ##print k                    
                    #sub_j = C_rep[j+1:j+k+2]
                    #if(q_mult(sub_j) == "j"):
                        #for l in range(len(C_rep)-j-k-2):
                            ##print "L ",
                            ##print l                            
                            #sub_k = C_rep[j+k+2:j+k+l+3]
                            #if(q_mult(sub_k) == "k"):
                                #answer = "Yes"
    print answer
    output.write("Case #")
    output.write(str(i+1))
    output.write(": ")
    output.write(answer)
    output.write("\n")
        
output.close()         