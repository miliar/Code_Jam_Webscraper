input_file = "A-large.in";
output_file = "0.out";

input = open(input_file,"r");
output = open(output_file,"w+");

num_tests = int(input.readline());

for test in range(num_tests):

    size = int(input.readline());
    matrix = []
    a = []
    for i in range(size):
        gg = input.readline()
        matrix.append(gg.strip());
        a.append(len(gg.rstrip('\n0')))
    
    if test != 2:
        #continue
        pass
    
    #print(matrix)
    
    n = 0
    for i in range(size):
        idx = i + 1
        
        found = i;
        for j in range(i,size):
            if (a[j] <= idx):
                found = j
                break
        
        # swap
        if i != found:
            s = a[i:found]
            a[i] = a[found]
            a[i+1:found+1] = s
            n = n + found - i
            #print("{0} -> {1}".format(i,found))
            
    print("Case #{0}: {1}".format(test+1,n));
            

                        