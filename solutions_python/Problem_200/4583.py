fp = open("input.txt","r")

f1 = open("output.txt","w")

f = fp.readlines()

count = 0



def identify_tiny( str1, count):

    for x in range(int(str1), 0, -1):

        tiny_number = 0;

        if (x < 10):
            tiny_number = x

        str1 = str(x)
        for i in range(0, len(str1)):

            if(i < len(str1)-1):
                if (str1[i] > str1[i+1]):
                    break;

            if (i == len(str1)-2):
                if (str1[i] <= str1[i+1]):
                     tiny_number = int(str1)

        if (tiny_number != 0):
            break;



    
    f1.write("Case #" + str(count-1) + ": " + str(tiny_number)+ "\n")

    
    
    
                    
    
 

for line in f:
   line = line.rstrip()
   if line:
       count = count+1;
       print line
       if(count != 1):
           identify_tiny(line, count)





f1.close()





