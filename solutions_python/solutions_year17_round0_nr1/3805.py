fp = open("input.txt","r")

f1 = open("output.txt","w")

f = fp.readlines()

count = 0

def convert_cake( str1, limit, count):
    attempt = 0;
    a = '+'; b = '-';
    length = len(str1)
    for i in range(0,length):
        if (str1[i] == a):
            continue;
        if (str1[i] == b and i+limit <= length):
            attempt = attempt + 1;
            for j in range(i, i+limit):
                if (str1[j] == b):
                     str1[j] = a
                    
                elif (str1[j] == a):
                    str1[j] = b
                    
            print str1
        if (str1[i] == b and i+limit > length):
            attempt = 'IMPOSSIBLE'
            break;

    f1.write("Case #" + str(count-1) + ": " + str(attempt)+ "\n")

    
    
    
                    
    


for line in f:
   count = count+1;
   if(count != 1):
       str2 = line.split()
       print str2
       convert_cake(list(str2[0]),int(str2[1]), count)



f1.close()





