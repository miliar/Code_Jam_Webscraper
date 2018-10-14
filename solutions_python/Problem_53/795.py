 # -*- coding: utf-8 -*-

            
print 'if you are you submitting a small input insert 1'
if raw_input()== "1":
    myFile = "A-small-attempt0.in"
    myFileOut = "A-small-attempt0.out"
else :
    myFile = "A-large.in"
    myFileOut = "A-large.out"

myData = file(myFile,'r')
myDataOut = file(myFileOut,'w')
counter = 1

for line in myData:
        if counter == 1: T = int(line)
        if counter >=2 :
           datos = line.split(' ')
           N = int(datos[0])
#           print "N: " + str(N)
           K = bin(int(datos[1]))
 #          print "K: " + str(K)
           F = len(K) 
           I = F - N 
           a = K[I:F]
  #         print "a: " + a
           if ("0" in a) or (len(K) - 2) < N  : snSalida = "OFF"
           else :   snSalida = "ON"
           snSalida = "Case #" + str(counter - 1) + ": " + snSalida +"\n"
           myDataOut.write(snSalida)
        counter = counter + 1
        T = T - 1
        if T < 0: break

myData.close()
myDataOut.close()
print 'Finalizó'



