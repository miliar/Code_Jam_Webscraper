#ALRIGHT MUHFUGUHS

def determineNumber(case, board1, answer1, board2, answer2):
    row1 = board1[int(answer1) - 1]
    row2 = board2[int(answer2) - 1]
    mutual = set(row1[0]).intersection(set(row2[0]))
    
    #Good case: 
    if len(mutual) == 1:
        print "Case #" + str(case) + ":", mutual.pop()
      #  return "Case #" + str(case) + ":", mutual.pop()
    
    #Bad magician
    elif len(mutual) > 1:
        print "Case #" + str(case) + ":", "Bad magician!"
       # return "Case #" + str(case) + ":", "Bad magician!"
    
    #Volunteer cheat
    else: 
        print "Case #" + str(case) + ":", "Volunteer cheated!"
        #return "Case#" + str(case) + ":", "Volunteer cheated!"

def derp(file): 
    txt = open(file, "r")
    cases = int(txt.readline().strip())
    
    for i in range(cases): #Read cases
        #Read first board
        num1 = int(txt.readline().strip())
        board1 = [[txt.readline().strip().split()],[txt.readline().strip().split()],[txt.readline().strip().split()],[txt.readline().strip().split()]]
        
        num2 = int(txt.readline().strip())
        board2 = [[txt.readline().strip().split()],[txt.readline().strip().split()],[txt.readline().strip().split()],[txt.readline().strip().split()]]
        
        determineNumber(i+1, board1, num1, board2, num2)
        
        
        