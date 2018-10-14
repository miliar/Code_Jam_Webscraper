fp = open("input.txt","r")

f1 = open("output.txt","w")

f = fp.readlines()

count = 0



def identify_bathroom( availability, persons, count):

    a = [0,0]

    if (persons == 1):
        availability = availability -1;

        if( availability % 2 == 0):
             a[0] = availability/2
             a[1] = availability/2

        else:
            a[0] = int(availability/2)+1
            a[1] = int(availability/2)


        f1.write("Case #" + str(count-1) + ": " + str(int(a[0]))+ " " + str(int(a[1]))+  "\n")

        #print (int(a[0]), int(a[1]))


    a1 = 0;
    if (persons > 1):
        for x in range(persons, 0, -1):

            if (a1 != 0 and x != 1):
                b = a[0]
                a = a[1:]
                length = len(a)

                b = b-1;


                if( b % 2 == 0):
                      a.append(b/2)
                      a.append(b/2)
                      
                else:
                     a.append(int(b/2)+1)
                     a.append(int(b/2))

                a.sort(reverse=True)


            if (a1 != 0 and x == 1):
                b = a[0]

                b= b-1;


                if( b % 2 == 0):
                      f1.write("Case #" + str(count-1) + ": " + str(int(b/2))+ " " + str(int(b/2))+  "\n")
                      #print(int(b/2), int(b/2))

                else:
                     f1.write("Case #" + str(count-1) + ": " + str(int(b/2)+1)+ " " + str(int(b/2))+  "\n")
                     #print (int(b/2)+1,int(b/2))
                    
            
            if(a1 == 0):
                 availability = availability -1;


                 if( availability % 2 == 0):
                      a[0] = availability/2
                      a[1] = availability/2

                 else:
                     a[0] = int(availability/2)+1
                     a[1] = int(availability/2)
                
                 a1 = 1

            
                

    
    
for line in f:
   line = line.rstrip()
   if line:
       count = count+1;
       if(count != 1):
           str2 = line.split()
           identify_bathroom(int(str2[0]),int(str2[1]), count)



f1.close()





