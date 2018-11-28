from sys import argv

script, filename = argv

txt = open(filename)
filewrite = open('result_large.txt', 'w+')

with txt as f:
    tests = [int(x) for x in f.readline().split()]
    array = [[x for x in line.split()] for line in f]

for index in range(len(array)):
   array[index][1] = map(int,str(array[index][1]))
   total = 0
   count = 0

   if array[index][1][0] == 0:
   	total = total + 1
   	count = count + 1
   
   for i in range(len(array[index][1])): 
   	
   	if total < i:
   		count = count + 1
   		total = total + 1

   	total = total + array[index][1][i]
   string = "Case #" + str(index+1) +  ": " + str(count) + '\n'
   filewrite.write(string)



   
