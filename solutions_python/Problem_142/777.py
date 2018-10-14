from multiprocessing import Pool
import os

def solvePuzzle(num, strings):
    compressedString = compressString(strings[0][:-1])
    for i in range(1,num):
        if compressString(strings[i][:-1]) != compressedString:
            return "Fegla Won"

    leng = len(compressedString)
    totals=[0]*leng
    averages = [0]*leng
    arrays = [0]*num
    answer=0
    for i in range(0,num):
        arrays[i] = nString( strings[i][:-1])
        for j in range(0, leng):
            totals[j]+=arrays[i][j]
    for j in range(0,leng):
        averages[j]=int(totals[j]/num+.5)
    for i in range(0,num):
        for j in range(0, leng):
            answer+=abs(arrays[i][j]-averages[j])
    return str(answer)
        


def compressString(string):
    lastChar=''
    newString=''
    for i in string:
      if i!=lastChar:
         lastChar = i
         newString+= i
    return newString

def nString(string):
    lastChar=string[0]
    newString=[]
    number=0
    for i in string[1:]:
      number+=1
      if i!=lastChar:
         lastChar = i
         newString+=[number]
         number=0
    return newString+[number]


    
    

input_text = open("input.in")
lines = input_text.readlines()
input_text.close()
currentLine=1
with open("output", "a") as outputfile:
    pool = Pool(processes=6)
    results = {}
    for num in range(0,int(lines[0])):
        size = int(lines[currentLine])
        strings = lines[currentLine+1:currentLine+size+size]
        currentLine= currentLine+size+1
        results[num]= pool.apply_async(solvePuzzle, [size, strings])
        #outputfile.write("Case #"+str(num+1)+": "+solvePuzzle(size,strings)+"\n")
    for num in range(0,int(lines[0])):
        outputfile.write("Case #"+str(num+1)+": "+results[num].get()+"\n")
