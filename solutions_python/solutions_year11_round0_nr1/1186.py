import sys

f_input = open(sys.argv[1])
problems = int(f_input.readline().rstrip())

for i in range(problems):
    sys.stdout.write("Case #%d: " % (i+1))

    O_buttons=[]
    B_buttons=[]
    turns = []
    linenums = f_input.readline().rstrip().split(" ")
    buttonnum = int(linenums.pop(0))
    #print buttonnum
    while(len(linenums)>0):
        newin = linenums.pop(0)
        if newin == "O":
            O_buttons.append(int(linenums.pop(0)))
            turns.append("O")
        if newin == "B":
            B_buttons.append(int(linenums.pop(0)))
            turns.append("B")

    #print O_buttons
    #print B_buttons
    
    step=0
    O_pos=1
    B_pos=1
    step_flag=0
    while(len(turns)>0):
        step+=1
        #print step
        if(len(O_buttons)>0):
            if(O_pos==O_buttons[0]):
                if(turns[0]=="O"):
                    O_buttons.pop(0)
                    step_flag=1
            elif(O_pos>O_buttons[0]):
                O_pos-=1
            elif(O_pos<O_buttons[0]):
                O_pos+=1

        if(len(B_buttons)>0):
            if(B_pos==B_buttons[0]):
                if(turns[0]=="B"):
                    B_buttons.pop(0)
                    step_flag=1
            elif(B_pos>B_buttons[0]):
                B_pos-=1
            elif(B_pos<B_buttons[0]):
                B_pos+=1

        if(step_flag):
            turns.pop(0)
            step_flag=0
    sys.stdout.write(str(step)+"\n")



    
