import sys
def needCompute(shyLevel,people,totalStands):
    if(int(people) !=0):        
        need = shyLevel-totalStands
    else:
        need = 0
    return need
def fileRead(filename):
    #"function_docstring"
    #except IOError:
    lines = [line.strip() for line in open(filename)]
    return lines
def lineToCompute(line):
    arr = line.split()
    #print arr
    aud = arr[1]
    maxShy = arr[0]
    length=len(arr[1])
    #print "\n\n\nFirst Line ",length
    need = 0
    totalStands = 0
    count = 0
    shyLevel = 0
    while(count<length):
        #print "Shyness Level : ",shyLevel,"\t\t audiunce : ",line[count]
        if(totalStands>=shyLevel):
            totalStands = totalStands+int(aud[count])
            
        else:
            tempNeed = needCompute(shyLevel,aud[count],totalStands)
            need = need + tempNeed
            totalStands = totalStands+tempNeed+int(aud[count])
            #print "Total Stands",totalStands
        count = count+1
        shyLevel = shyLevel + 1
        #print "Total Stands",totalStands
        #print "Maximum Shyness :",line[0],"\n audiunce : ",aud
    return need
def main():
    lines = fileRead("A-large.in")
    #print lines[0]
    count = 1
    value = 0
    while (count <= int(lines[0])):
        #print count
        
        value = lineToCompute(lines[count])
        f = open('myfile.txt','w')
        f.write("Case #%d: %d" %(count,value)) # python will convert \n to os.linesep
        f.close()
        print "Case #%d: %d" %(count,value)
        count = count+1
        

    
main()
