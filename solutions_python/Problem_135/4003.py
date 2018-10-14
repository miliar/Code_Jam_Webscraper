def magic_trick(file):
    with open(file+".txt") as f:
        case=1
        remove_line=f.readline()
        i=0
        
        for line in f:
            
            if i==0:
                row1=int(line.rstrip('\n'))
                i+=1
            elif i==1 or i==2 or i==3 or i==4:
                if i==row1:
                    R1=line.split()
                else:
                    pass
                i+=1
                
            elif i==5:
                row2=int(line.rstrip('\n'))
                i+=1
                
            elif i==6 or i==7 or i==8 or i==9:
                if i-5==row2:
                    R2=line.split()
                else:
                    pass
                i+=1
                if i==10:
                    matches=0
                    for x in R1:
                        for y in R2:
                            if x==y:
                                matches+=1
                                card=y
                            
                    if matches==0:
                        print ("case #%d: Volunteer cheated!" %(case))
                        i=0
                        case+=1
                    elif matches==1:
                        print ("case #%d: %s" %(case,card))
                        i=0
                        case+=1
                    elif matches>1:
                        print ("case #%d: Bad magician!" %(case))
                        i=0
                        case+=1
                    
   
magic_trick("input")
                    
        

