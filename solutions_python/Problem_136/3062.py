import decimal

def getValues(name, count):
    file = open(name, 'r')
    while(count != 0):
        count = count - 1
        file.readline()
    returnVal = file.readline()        
    file.close()        
    return returnVal.strip()



def getTuple(name, line):
        string1 = getValues(name, line)
                

        row = int(string1)
        #print("row", row)
        #print("line", line)
        string2 = getValues(name, line + row).split()
        array = list(map(int, string2 ) )

        return array


def addZr(string):
    index = string.index('.')
    whole = string[0:index ]
    decimal = string[index +1 : len(string)]
##    print("string", string)
##    print("whole", whole)
##    print("index", index)
##    print("decimal", decimal)
    if(len(decimal) < 7):
        #decimal += ('0' *  (7 - len(decimal)) ) + '1'
        decimal += ('0' *  (7 - len(decimal)) )
##    print("whole + '.' + decimal", whole + '.' + decimal + '\n\n')         
    return whole + '.' + decimal;    

def main():
    
    filename = "B-large.in"
    #line = 0
    #case = int( getValues(name,line) )
    case = int( getValues(filename,0) )
    strVal = ""
    
    
    for num in range(0, case):
        
        totalT = 0
        totalT1 = 0
        ratePerSec = 2
    
        string = getValues(filename, num + 1).split()
        #array = list( map(int,   map(float, string ))  )
        array = list(   map(float, string ))
        #array = list(   map(float, map(addZr, string) ))
        #array = list(   map("%.7f" %, string ))  

        valC = array[0]
        
        valF =    array[1] 
        valX = array[2] 

##        print("#valC" + str(valC))
##        print("valF" , str(valF))
##        print('valX', str(valX) )
        doLoop = True
        totalTH = 0
        while(doLoop) :
            totalT1 = totalT
            time2 = valX / ratePerSec
            #time2 = float("%.7f" % time2)
            totalT1 += time2

            

##            if(ratePerSec >= valX):
##                doLoop = False
            
##            cookieHolder = valX
##            timeHolder = 0
##            ratePerSecHolder = ratePerSec
##
##            
##            
##            while(cookieHolder > valC):
##                time = valC / ratePerSecHolder
##                timeHolder += time
##                ratePerSecHolder += valF
##                
##                cookieHolder -= valC

            #timeCheck = (timeHolder + valX) / (ratePerSecHolder + ratePerSec)
##            timeCheck = (valX - cookieHolder) / (ratePerSecHolder )
##            timeHolder += timeCheck
##            timeHolder += totalT
##            print("totalT1", totalT1) 
##            print("totalT", totalT)
##            print("timeCheck", timeCheck)
##            print("timeHolder", timeHolder)
##            print("ratePerSecHolder", ratePerSecHolder)
##            print("ratePerSec", ratePerSec)
##            if(totalT1 < timeHolder):
##                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZZZZZZZZZZZZZ")
##                #totalT = 0
##                doLoop = False
            
            time = valC / ratePerSec
            #time = float("%.7f" % time)
            totalT += time
            
            #totalT = float("%.7f" % totalT)
            
            ratePerSec += valF

            totalTH = totalT
            time2 = (valX )/ ratePerSec
            #time2 = float("%.7f" % time2)
            totalTH += time2


##            print("totalT1", totalT1) 
##            print("totalT", totalT)
##            print("timeCheck", totalTH)
##            print("ratePerSec", ratePerSec)
            if(totalT1 < totalTH):
                print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAZZZZZZZZZZZZZ")
                #totalT = 0
                doLoop = False


                
##            print("time2", time2)
##            print("time", time)
            
    ##            print("totalT", totalT)

        print("Case #" + str(num + 1) + ": " + str(round(totalT1, 7))   )
        print('\n\n\n')
        strVal += "Case #" + str(num + 1) + ": " + addZr(str(round(totalT1, 7)))  + '\n'  
##        elif(totalT1 >= totalT):
##        if(totalT1 < totalT):
##            print("Case #" + str(num + 1) + ": " + str(totalT1) )
##            strVal += "Case #" + str(num + 1) + ": " + str(totalT1) + '\n'   
##        elif(totalT1 >= totalT):
##            print("Case #" + str(num + 1)  + ": " + str(totalT))
##            strVal += "Case #" + str(num + 1)  + ": " + str(totalT) + '\n'
##        else:
##            print("Case #" + str(num + 1)  + ":---- " + "hmm")
            #strVal +=
        #strVal += "Case #" + str(num + 1) + ': ' + str(moves) + '\n'                 

        #print("Case #" + str(num + 1) )
        #print("array1string1 " , array1)
        #print('array2', array2 )
        #print('array', array )
        #print('\n')
                           
        
        writeToFile(strVal)        

def writeToFile( string):
    f = open("output", 'w')
    f.write(string)
    f.close()

 
