f=open('B-small-attempt1.in','r')
f1=open('output.txt','w')
t=int(f.readline())
s=0
while(s<t) :
    testcase = f.readline()
    no_combo = testcase[0]
    no_of_sp = 0
    j=1
    combos=[]
    while no_of_sp < int(no_combo) :
        if testcase[j] == ' ':
            no_of_sp = no_of_sp +1
            s1= testcase[j+1]
            s2= testcase[j+2]
            s3= testcase[j+3]
            combos.append(s1+s2+s3)
            combos.append(s2+s1+s3)
    #        print combos
        j=j+4

    no_of_sp = 0
    oppos = []
    no_oppo=testcase[j+1]
    #print no_oppo
    j=j+2
    while no_of_sp < int(no_oppo) :
        if testcase[j] == ' ':
            no_of_sp = no_of_sp +1
            s1= testcase[j+1]
            s2= testcase[j+2]
            oppos.append(s1+s2)
            oppos.append(s2+s1)
    #        print oppos
        j=j+3
    j=j+1
    j0=j
    while j<len(testcase) :
        if testcase[j] == ' ':
            len_elemlist = int(testcase[j0:j])
            break
        j=j+1
    j=j+1
    j0=j
    j_end = j+len_elemlist
    sublist=''
    i=0
    elemlist = testcase[j0:j_end]
    print elemlist
    while i <len(elemlist):
        check = 0
        if len(sublist) > 0 :
            #checking combos
            check_string = sublist[-1:]+elemlist[i]
            j=0
            while j<len(combos) :
                if combos[j][:2] == check_string :
                    replace = combos[j][2:3]
                    check=1
                    sublist = sublist[:-1] + str(replace)
                    break
                j=j+1
            #check in oppos
            if check != 1 :
                k=0
                while k<len(oppos) :
                    if oppos[k][:1] == elemlist[i] :
                        elem_to_find = oppos[k][1:2]
                        if sublist.find(elem_to_find) != -1 :
                            sublist = ''
                            check=2
                            break
                    k=k+1
        if (check == 0) :
            sublist = sublist + elemlist[i]
        i=i+1
    print sublist
    print_i = 0
    output_string = "Case #"+ str(s+1) +': [' 
    while print_i < len(sublist) :
        output_string = output_string + str(sublist[print_i]) + ', '
        print_i = print_i + 1
    if output_string[-1:] !='[' :
        output_string = output_string[:-2] + ']' + '\n'
    else :
        output_string = output_string + ']' + '\n'
    print output_string
    f1.write(output_string)
    s=s+1
