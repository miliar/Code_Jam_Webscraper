gdata = open("C:\Users\Feynman\Downloads\B-large.in","r")
data = []
k=1
for line in gdata:
    line = line.strip()
    data.append(line)
gdata.close()

    
testcase = int(data.pop(0))

for i in range(testcase):
 a = data[i].split(" ")

 
 C = float(a[0])
 F = float(a[1])
 X = float(a[2])
 time = 0
 step = 0.2  
 
 while (k != 3):    
  x = (X/step)/10
  y = (C/step)/10
  z = (X/(step+(F/10)))/10
 


  if x <= (y+z):
     time +=x
     break
    
  if x > (y+z):
     time +=y
     step +=(F/10)
     
 print "Case #" +str(i+1)+": " +str(round(time,7))



