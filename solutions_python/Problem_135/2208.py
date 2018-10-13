f = open('A-small-attempt0.in','r')
n = int(f.readline())

for i in range(n):
    count = 0
    card = ''
    first_ans = int(f.readline())
    first_line1 = f.readline().split()
    second_line1 = f.readline().split()
    third_line1 = f.readline().split()
    fourth_line1 = f.readline().split()
    second_ans = int(f.readline())
    first_line2 = f.readline().split()
    second_line2 = f.readline().split()
    third_line2 = f.readline().split()
    fourth_line2 = f.readline().split()
    if(first_ans == 1):
        for j in first_line1:
            if(second_ans == 1):
                if(j in first_line2):
                    count +=1
                    card = j
            elif(second_ans ==2):
                if(j in second_line2):
                    count +=1
                    card = j
            elif(second_ans ==3):
                if(j in third_line2):
                    count +=1
                    card = j
            elif(second_ans ==4):
                if(j in fourth_line2):
                    count +=1
                    card = j
    elif(first_ans == 2):
        for j in second_line1:
            if(second_ans == 1):
                if(j in first_line2):
                    count +=1
                    card = j
            elif(second_ans ==2):
                if(j in second_line2):
                    count +=1
                    card = j
            elif(second_ans ==3):
                if(j in third_line2):
                    count +=1
                    card = j
            elif(second_ans ==4):
                if(j in fourth_line2):
                    count +=1
                    card = j

    elif(first_ans == 3):
        for j in third_line1:
            if(second_ans == 1):
                if(j in first_line2):
                    count +=1
                    card = j
            elif(second_ans ==2):
                if(j in second_line2):
                    count +=1
                    card = j
            elif(second_ans ==3):
                if(j in third_line2):
                    count +=1
                    card = j
            elif(second_ans ==4):
                if(j in fourth_line2):
                    count +=1
                    card = j

    elif(first_ans == 4):
        for j in fourth_line1:
            if(second_ans == 1):
                if(j in first_line2):
                    count +=1
                    card = j
            elif(second_ans ==2):
                if(j in second_line2):
                    count +=1
                    card = j
            elif(second_ans ==3):
                if(j in third_line2):
                    count +=1
                    card = j
            elif(second_ans ==4):
                if(j in fourth_line2):
                    count +=1
                    card = j

    if(count==1):
        output = card
    elif(count==0):
        output = "Volunteer cheated!"
    else:
        output = "Bad magician!"
        
    print("Case #"+str(i+1)+": "+output)
    
