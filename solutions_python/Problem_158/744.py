file1 = open("D-small-attempt1.in", "r")
my_file = open("output.txt", "r+")

t = int(file1.readline())

i = 1
while (i <= t):
    domino = file1.readline().split()
    domino = [int(j) for j in domino]

    if domino[0] == 1:
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 2 and (domino[1]*domino[2])%2 ==1 :
        my_file.write(("Case #%d: %s\n" % (i,'RICHARD')))
        
    elif domino[0] == 2:
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 4 and (domino[1]*domino[2])== 12:
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 4 and (domino[1]*domino[2])== 16:
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 4:
        my_file.write(("Case #%d: %s\n" % (i,'RICHARD')))
        
    elif domino[0] == 3 and (domino[1]*domino[2])==6:
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 3 and (domino[1]*domino[2])==9 :
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
        
    elif domino[0] == 3 and (domino[1]*domino[2])==12 :
        my_file.write(("Case #%d: %s\n" % (i,'GABRIEL')))
    else:
        my_file.write(("Case #%d: %s\n" % (i,'RICHARD')))
    i+=1
my_file.close()
file1.close()	
        
        
    
