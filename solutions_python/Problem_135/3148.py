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

def main():
    
    filename = "A-small-attempt0.in"
    #line = 0
    #case = int( getValues(name,line) )
    case = int( getValues(filename,0) )
    strVal = ""
    temp = 0
    
    for num in range(0, case):
        count = 0
        offset = num + 1
        lineToget = (num * 10) + 1
        
        array1 = getTuple(filename, lineToget)
        lineToget = (num  * 10) + (1 * 5) + 1
        array2 = getTuple(filename, lineToget)

        for item1 in array1:
            for item2 in array2:
                if(item1 == item2):
                    count += 1
                    temp = item1
        if(count == 1):
            #print("Case #" + str(num + 1) + ": " + str(temp))
            strVal += "Case #" + str(num + 1) + ": " + str(temp) + '\n'   
        elif(count > 1):
            #print("Case #" + str(num + 1)  + ": " + "Bad magician!")
            strVal += "Case #" + str(num + 1)  + ": " + "Bad magician!" + '\n'
        elif(count == 0):
            #print("Case #" + str(num + 1)  + ": " +  "Volunteer cheated!")
            strVal += "Case #" + str(num + 1)  + ": " +  "Volunteer cheated!"  + '\n'
        else:
            print("Case #" + str(num + 1)  + ":---- " + "hmm")
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

 
