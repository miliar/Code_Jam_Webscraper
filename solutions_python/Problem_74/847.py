'''
Created on 7/05/2011

@author: Ed
'''

def bottrust(infile, outfile):
    input = open(infile, "r").readlines()
    output = open(outfile, "w")
    result = []
    for lineno in xrange(1, len(input)):
        turns = input[lineno].split(" ")
        onextturn = 0
        bnextturn = 0
        #Find index of O's first button number in list
        for turnno in xrange(1, len(turns), 2):
            if turns[turnno] == "O":
                onextturn= turnno + 1
                break;
        #Find index of B's first button number in list
        for turnno in xrange(1, len(turns), 2):
            if turns[turnno] == "B":
                bnextturn = turnno + 1
                break;
        #Step through each 1 second at at time  
        ocurrentbutton = 1
        bcurrentbutton = 1
        onextbutton = int(turns[onextturn])
        bnextbutton = int(turns[bnextturn])
        currentturn = 2 #index of the current turn
        turnno = 1

        seconds = 0
        turn = 0
        while turn < int(turns[0]):
            pleasewaitorange = False #Asks orange to wait until next turn to press his button
            
            if bnextturn != 0:
                if bnextbutton > bcurrentbutton:
                    bcurrentbutton += 1
                elif bnextbutton < bcurrentbutton:
                    bcurrentbutton -=1
                elif bcurrentbutton == bnextbutton:
                    if bnextturn == currentturn:
                        bnextturn = 0
                        for turnno in xrange(currentturn + 1, len(turns), 2):
                            if turns[turnno] == "B":
                                bnextturn = turnno + 1
                                bnextbutton = int(turns[bnextturn])
                                break;
                        currentturn += 2
                        turn += 1
                        pleasewaitorange = True
                        
            if onextturn != 0:
                if onextbutton > ocurrentbutton:
                    ocurrentbutton += 1
                elif onextbutton < ocurrentbutton:
                    ocurrentbutton -=1
                elif ocurrentbutton == onextbutton:
                    if not pleasewaitorange:
                        if onextturn == currentturn:
                            onextturn = 0
                            for turnno in xrange(currentturn + 1, len(turns), 2):
                                if turns[turnno] == "O":
                                    onextturn = turnno + 1
                                    onextbutton = int(turns[onextturn])
                                    break;
                            currentturn += 2
                            turn += 1
            seconds += 1
        result.append("Case #" + str(lineno) + ": " + str(seconds) + "\n")
    output.writelines(result)
             

        
        #Execute whoever has the current turn and then give them a next turn
        #Do this until both don't have any more turns
        
             
                         

def main():
    bottrust("A-large.in", "output.out")

if __name__ == '__main__': main()