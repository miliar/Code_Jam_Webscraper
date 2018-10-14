#!/usr/bin/python

def readInput():
    inputfile = open("A-small-attempt1.in","r");
    inputlist = inputfile.readlines()                   # make list of string
    inputlist = [word.strip() for word in inputlist]    # remove \n from the list of string
    inputlist = [x for x in inputlist if x]             # remove empty string from the list of string
    inputfile.close()
    return inputlist

def result(input_list):
    inputlist = input_list[1:]
    case_count = int(input_list[0]) 
    result = []
    temp_result = []
    temp = []
    for i in range(0,len(inputlist)):
        if (i%5)==0:
            index = int(inputlist[i])
            temp = temp + [inputlist[i+index]]
    templist = []
    for i in temp:
        templist = templist + [i.split()]
    
    
    for i in range(0,len(templist)):
        if(i%2)==0:
            check = 0
            element = ''
            for x in templist[i]:
                for y in templist[i+1]:
                    if x == y:
                        check = check +1
                        if check == 1:
                            element = x
            if check == 0:
                temp_result = temp_result + ["Volunteer cheated!\n"]
            if check == 1:
                temp_result = temp_result + [element + "\n"]
            if check > 1:
                temp_result = temp_result + ["Bad magician!\n"]
    
    for i in range(0,case_count):
        temp = "Case #" + str(i+1) + ": " + temp_result[i]
        result = result + [temp]
    
    
    return result

def writeOutput(result_list):
    outputfile = open("SOmagictrick","w")
    #print outputfile
    #outputfile.write('Output\n\n')
    #outputfile = outputfile.write('\n')
    for i in result_list:
        outputfile.write(i)
    
    outputfile.close()

input_list = readInput()


#print inputlist

case_count = int(input_list[0])

print case_count
#print type(case_count) 

result_list = result(input_list)

writeOutput(result_list)


