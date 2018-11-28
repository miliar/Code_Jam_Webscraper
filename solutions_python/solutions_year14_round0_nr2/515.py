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


def run(lis):
    T=int(lis[0])
    del lis[0]
    base_income=2
    
    for i in range(T):
        current_assets=0
        time_spent=0
        row1=str(lis[i])
        
        array=row1.split()
        c=float(array[0])
        f=float(array[1])
        x=float(array[2])
        current_income=base_income        
        
        while (x/current_income)>((c/current_income)+(x/(current_income+f))):
            time_spent+=(c/current_income)
            current_income+=f
            
        time_spent+=x/current_income
        
        print "Case #" +str(i+1) + ": " + str(time_spent) #t is a string


run(read_file("cookie.txt"))