from sys import argv
script = argv 
filename = raw_input("Input File   ")
outputfile = raw_input("Output File   ")
target = open(filename)
answer = (target.readline()) 
oput = open(outputfile , 'w+')
oput.truncate()
answ =  int(answer)
for i in range(1,(answ+1)):
 c = 0
 ans = (target.readline())
 ans =int(ans)
 ans1 = target.readline()
 ans2 = target.readline()
 ans3 = target.readline()
 ans4 = target.readline()
 aray=[ ans1 , ans2 , ans3 ,ans4 ] 
 ans = ans-1
 answer2 =  aray[ans]
 answer2 = answer2.split()
 a1,a2,a3,a4 = answer2
 arr1 = [a1,a2,a3,a4]
 line= (target.readline())
 line = int(line)
 line1 = (target.readline())
 line2 =  (target.readline() )
 line3 =  (target.readline())
 line4= (target.readline())
 array =[line1 , line2 , line3 , line4]
 line = (line) - 1
 answer3 = array[line]
 answer3 = answer3.split()
 b1,b2,b3,b4= answer3
 arr2 = [b1,b2,b3,b4]
 for j in range(0,4):
  luck = arr1[j]
  for p in range(0,4):
   luck1 = arr2[p]
   if luck==luck1 :
    c=c+1 ;
    ansarr =[luck]   
 if c == 0:
   output = "Case #%s: Volunteer cheated!" %i
   oput.write(str(output)+"\n")
 elif c == 1:
  you = ansarr[0]
  output = "Case #%s: %s " %(i , you)
  oput.write(str(output)+"\n")
 else :
  output = " Case #%s: Bad magician! " %i
  oput.write(str(output)+"\n")
oput.close()