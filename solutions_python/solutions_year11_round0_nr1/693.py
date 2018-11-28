
f=open('A-large.in','r')
f1=open('output.txt','w')
t=int(f.readline())
i=0
while(i<t) :
    testcase = f.readline()
    testcase = testcase
    j=0
    j0=j
    literals =[]
    while j < len(testcase):
        if testcase[j] == ' ' or testcase[j] == '\n' :
            literals.append(testcase[j0:j])
            j0=j+1
        j=j+1
    #print literals
    no_of_but = int(literals[0])

    O_list=[]
    B_list=[]
    j=1
    while (j < len(literals) -1) :
        if literals[j] == 'O' :
            O_list.append(literals[j+1])
        if literals[j] == 'B' :
            B_list.append(literals[j+1])
        j=j+2
    #print B_list
    #print O_list
    O_count= 0
    B_count= 0
    step_count = 0
    k=1
    but_pressed= 0
    O_location = 1
    B_location = 1
    while but_pressed < no_of_but :
        if literals[k] == 'O' :
            k=k+1
            destination = int(literals[k])
            steps_to_take = destination - O_location
            if O_location > destination :
                steps_to_take = O_location - destination
            O_location = destination
            step_count = step_count + steps_to_take + 1
            if O_count < (len(O_list) -1) :
                O_count = O_count +1
    #        print B_count
            
            if len(B_list) != 0    :
                if int(B_list[B_count]) > int(B_location) :
                    if (steps_to_take + 1) > (int(B_list[B_count]) - int(B_location)):
                        B_location = int(B_list[B_count])
                    else :
                        B_location = B_location + steps_to_take + 1
                else :
                    if (steps_to_take + 1) > (int(B_location) -int(B_list[B_count]) ):
                        B_location = int(B_list[B_count])
                    else :
                        B_location = B_location - steps_to_take -1

        if literals[k] == 'B':
            k=k+1
            destination = int(literals[k])

            steps_to_take = destination - int(B_location)
            if B_location > destination :
                steps_to_take = B_location - destination
            B_location = destination
            step_count = step_count + steps_to_take + 1
    #        print B_count
            if B_count < (len(B_list)-1):
                B_count = B_count + 1
            print O_count
            if len(O_list) != 0 :
                if int(O_list[O_count]) > int(O_location) :
                    if (steps_to_take + 1) > (int(O_list[O_count]) - int(O_location)):
                        O_location = int(O_list[O_count])
                    else :
                        O_location = O_location + steps_to_take + 1
                else :
                    if (steps_to_take + 1) > (int(O_location) -int(O_list[O_count]) ):
                        O_location = int(O_list[O_count])
                    else :
                        O_location = O_location - steps_to_take -1

        k=k+1
        but_pressed = but_pressed +1
    output_string = "Case #"+ str(i+1) +': ' + str(step_count) + '\n'
    print output_string
    f1.write(output_string)    
    i=i+1
f.close()
f1.close()