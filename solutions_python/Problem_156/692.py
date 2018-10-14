# -*-coding:Utf-8 -*

import sys,math,operator

# Parse args
with open("B-small-attempt2.in") as f:
        arg = f.readlines()

T = int(arg[0])
case = [0 for x in range(int(T))]

for ct in range(T):
        # We can safely ignore the line with the numbers of plates
        case[ct] = map(int, arg[2+ct*2].split())
        
f = open('B.out','w')
d = open('B.debug','w')

# More or less a recursive bruteforce search
def rec(plates):      
        # Endgame condition: everything is eaten
        plates = filter(lambda a: a != 0, plates)
        if(len(plates) == 0):
                return 0
        # d.write( "list : [" + ', '.join(map(str, plates)) + "]" +"\n" )
        # print "list : [" + ', '.join(map(str, plates)) + "]"
        # Eat a pancake
        # d.write ( "eat"+"\n")
        eat = rec(map(lambda x : x-1 , plates))
        if eat == 0:
                return 1
        # Swap all pancakes with all pancakes (ikk !)
        # d.write ( "swap"+"\n")
        plates = sorted(plates, reverse=True)
        tmp_plates = list(plates)
        tmp_plates.append(int(tmp_plates[0]/2))
        tmp_plates[0] = int(tmp_plates[0]/2) + tmp_plates[0]%2
        swap = rec(tmp_plates)
        if plates[0] == 9:
                tmp_plates = list(plates)
                tmp_plates.append(3)
                tmp_plates[0] = 6
                swap = min(swap, rec(tmp_plates))
                
        # Take the best option
        return min(eat, swap) +1


# Compute each case
for ct in range(int(T)):
        # Print data in memory
        # d.write ( "*************** case number " + str(ct)+"\n" )
        print "*************** case number " + str(ct)+"\n"
        # d.write ( "list : [" + ', '.join(map(str, case[ct])) + "]"+"\n")
        # print "list : [" + ', '.join(map(str, case[ct])) + "]"

        # Solve !
        hashtable = dict()
        plates = sorted(case[ct], reverse=True)
        time = rec(case[ct])
        # d.write ( "time needed : " + str(time) +"\n")
        print "time needed : " + str(time)
                
        # Write output
        f.write ("Case #" + str(ct+1) + ": " + str(time) + "\n"+"\n")

f.close()
d.close()
