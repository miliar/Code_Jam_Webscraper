#Google Code Jam 5/7/2011
#Sean and Patrick are brothers who just got a nice bag of candy 
#from their parents. Each piece of candy has some positive integer
#value, and the children want to divide the candy between them. 
#First, Sean will split the candy into two piles, and choose one 
#to give to Patrick. Then Patrick will try to calculate the value
#of each pile, where the value of a pile is the sum of the values 
#of all pieces of candy in that pile; if he decides the piles don't 
#have equal value, he will start crying.

#Unfortunately, Patrick is very young and doesn't know how to add 
#properly. He almost knows how to add numbers in binary; but when 
#he adds two 1s together, he always forgets to carry the remainder 
#to the next bit. For example, if he wants to sum 12 (1100 in binary) 
#and 5 (101 in binary), he will add the two rightmost bits correctly, 
#but in the third bit he will forget to carry the remainder to the 
#next bit:

  #1100
#+ 0101
#------
  #1001

#So after adding the last bit without the carry from the third bit, 
#the final result is 9 (1001 in binary). Here are some other examples 
#of Patrick's math skills:

#5 + 4 = 1
#7 + 9 = 14
#50 + 10 = 56

#Sean is very good at adding, and he wants to take as much value as he 
#can without causing his little brother to cry. If it's possible, he 
#will split the bag of candy into two non-empty piles such that Patrick 
#thinks that both have the same value. Given the values of all pieces 
#of candy in the bag, we would like to know if this is possible; and, 
#if it's possible, determine the maximum possible value of Sean's pile.
#Input

#The first line of the input gives the number of test cases, T. T test 
#cases follow. Each test case is described in two lines. The first line
#contains a single integer N, denoting the number of candies in the 
#bag. The next line contains the N integers Ci separated by single 
#spaces, which denote the value of each piece of candy in the bag.
#Output

#For each test case, output one line containing "Case #x: y", where 
#x is the case number (starting from 1). If it is impossible for 
#Sean to keep Patrick from crying, y should be the word "NO". 
#Otherwise, y should be the value of the pile of candies that 
#Sean will keep.
#Limits

#1 ≤ T ≤ 100.
#1 ≤ Ci ≤ 106.
#Small dataset

#2 ≤ N ≤ 15.
#Large dataset

#2 ≤ N ≤ 1000.
#Sample

#Input
  	
#Output
 
#2
#5
#1 2 3 4 5   Case #1: NO
#3
#3 5 6       Case #2: 11
	
import sys
import itertools
    
def Patrick(numbers):
    output=0
    for n in numbers:
        output^=n
    return output
    
def Sean(numbers):
    output=0
    for n in numbers:
        output+=n
    return output
    
def Seperate(total,sub):
    output=list(total)
    for n in sub:
        output.remove(n)
    return output


Cases=[]

count=0

outputfile=open('/home/jeff/Downloads/C-small-attempt1.out','w')
for line in open('/home/jeff/Downloads/C-small-attempt1.in'):
    count+=1
    if count<3: continue
    if count%2==0: continue
    line=line.strip()
    Cases.append([int(i) for i in line.split(' ')])

for C in range(len(Cases)):
    Case=Cases[C]
    largest=0
    for n in range(1,len(Case)):
        for case in itertools.combinations(Case,n):
            sean=case
            patrick=Seperate(Case,sean)
            if Patrick(sean)==Patrick(patrick):
                _sean=Sean(sean)
                if _sean>largest:
                    largest=_sean
    if largest==0:
        print('Case #'+str(C+1)+': NO')
        outputfile.write('Case #'+str(C+1)+': NO\n')
    else:
        print('Case #'+str(C+1)+':',largest)
        outputfile.write('Case #'+str(C+1)+': '+str(largest)+'\n')
                
outputfile.close()



