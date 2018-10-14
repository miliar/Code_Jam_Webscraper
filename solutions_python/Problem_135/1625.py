  
def parse_file(input_file):
    T = int(input_file.readline().replace('\n',''))        
    out_file = file("A-small.out", "w")        
    for counter in xrange(T):
        A1 = int(input_file.readline().replace('\n',''))
        Arr1 = []
        for i in xrange(4):
            Arr1.append([int(x) for x in input_file.readline().replace('\n','').split(' ')])
        A2 = int(input_file.readline().replace('\n',''))
        Arr2 = []
        for i in xrange(4):
            Arr2.append([int(x) for x in input_file.readline().replace('\n','').split(' ')])
        
        Arr1 = Arr1[A1-1]
        Arr2 = Arr2[A2-1]
        Arr1.sort()
        Arr2.sort()
        i = 0
        j = 0;
        count = 0
        res = "Volunteer cheated!"
        while i < 4 and j < 4:
            if Arr1[i] == Arr2[j]:
                count = count + 1;
                res = str(Arr1[i])
                i = i + 1
                j = j + 1
            elif Arr1[i] > Arr2[j]:
                j = j + 1
            else:
                i = i + 1
        
        if count > 1:
            res = "Bad magician!"
        out_file.write("Case #"+str(counter+1)+": " + res + "\n") 
        
    out_file.close()
    
if __name__ == "__main__":
    input_file = file("A-small-attempt0.in")
    parse_file(input_file)
