def read_file(filename):
    """
    reads file and makes it into a list
    """
    f = open(filename, 'r')
    lis = []
    for line in f:
        lis.append(line.strip())
    
    f.close()
    return lis

def find(array, number):
    for z in range(len(array)):
        if array[z] > number:
            return z

def run(lis):
    T=int(lis[0])
    del lis[0]
    
    for i in range(T):
        kenpoints=0
        naomipoints=0
        kp=0
        np=0
        
        row1=str(lis[(i*3+1)])
        row2=str(lis[(i*3+2)])
    
        naomi=sorted(row1.split())
        ken=sorted(row2.split())
        
        n2=sorted(row1.split())
        k2=sorted(row2.split())
       
        for d in range(len(naomi)):
            
            if float(naomi[0])<float(ken[0]):
                kenpoints+=1
                del naomi[0]
                del ken[-1]
            else:
                naomipoints+=1
                del naomi[0]
                del ken[0]
 
        for x in range(len(n2)):
            if float(n2[-1])>float(k2[-1]):
                np+=1
                del n2[-1]
                del k2[0]
         
            else:
                kp+=1
                y=find(k2, n2[-1])
            
                del n2[-1]
                del k2[y]
   
        print "Case #" + str(i+1)+": " + str(naomipoints) + " " + str(np)


run(read_file("war.txt"))