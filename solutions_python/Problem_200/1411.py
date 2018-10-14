f = open("B-small-attempt1.in", "r").read()


lines = f.split("\n")
cases = int(lines[0])

for case in range(1, cases+1):
    line = lines[case]

    index = 1

    for i in range(int(line)):
        y = (int(line)-i)
        if index == 0:
            print("Case #{0}: {1}".format(case, y+1))
            break
        
        else :  
            x = y  
            while x/10 != 0:
                if (x%10) < ((x/10)%10) :
                    index += 1 
                    break
                else :
                    x = x/10
                    continue
                x/10 
                continue     
            index = index -1   
