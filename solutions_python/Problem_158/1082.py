inputfile = open("D-small-attempt3.in",'r')
outputfile = open("output_DSmall.txt",'w')

firstline = inputfile.readline()

counter = 0
while counter<int(firstline):
    inputline = inputfile.readline()
    tokens = inputline.split()
    x = int(tokens[0])
    r = int(tokens[1])
    c = int(tokens[2])
    ga_win = False
    ri_win = False
    
    total_square = r * c
    remainder = total_square % x
    
    if x > total_square:
        ri_win = True
    elif remainder > 0:
        ri_win = True
    elif x == 1:
        ga_win = True
    elif x == 2:
        if r == 2 or c == 2:
            ga_win = True
        elif r == 4 or c == 4:
            ga_win = True
    elif x == 3:
        if r == 1 or c == 1:
            ri_win = True
        elif r == 3 or c == 3:
            ga_win = True
    elif x == 4:
        if r == 4 and c == 4:
            ga_win = True
        elif r == 3 and c == 4:
            ga_win = True
        elif r == 4 and c == 3:
            ga_win = True
        else:
            ri_win = True
        
    if ri_win == True and ga_win == True:
        print("Error")
    else:
        #outputfile.write(str(x)+" "+str(r)+" "+str(c)+" "+"\n")
        if ri_win:
            outputfile.write("Case #"+str(counter+1)+": RICHARD")
            outputfile.write("\n")
        else:
            outputfile.write("Case #"+str(counter+1)+": GABRIEL")
            outputfile.write("\n")
            
    counter += 1

inputfile.close()
outputfile.close()