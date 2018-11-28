with open("A-small-attempt5.in","r") as fp:
    with open("ouput.out","w") as out:
        cases = fp.readline()
        
        for c in range(0,int(cases)):
            
            first_row = fp.readline() #First row that users choose 
            first_list = []          
            for r1 in range(1, 5):
                if(r1 == int(first_row)):
                    first_list = fp.readline().split()
                else:
                    fp.readline()
                        
            second_row = fp.readline() #Second row that users choose
            second_list = []                      
            for r2 in range(1, 5):
                if(r2 == int(second_row)):
                    second_list = fp.readline().split()
                else:
                    fp.readline()
                    
            x = set(first_list).intersection(second_list)
            if(len(x) == 1):
                s = x.pop()
                print("Case #" + str(c+1) + ": " + s)
                out.write("Case #" + str(c+1) + ": " + s + "\n")
            elif (len(x) > 1):
                print("Case #" + str(c+1) + ": Bad magician!")
                out.write("Case #" + str(c+1) + ": Bad magician!" + "\n")
            else:
                print("Case #" + str(c+1) + ": Volunteer cheated!")
                out.write("Case #" + str(c+1) + ": Volunteer cheated!" + "\n")
                

                