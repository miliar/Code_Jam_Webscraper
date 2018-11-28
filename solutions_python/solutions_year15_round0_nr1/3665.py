def read_file():
    in_file=open("A-small-attempt0.in","r")
    test_cases=in_file.readline() #number of test cases
    T=test_cases.rstrip('\n') #remove line end
    test_data=[]
    for i in range(int(T)):
        line=in_file.readline()
        test_data.append(line.rstrip('\n'))
    in_file.close()
    return test_data

def write_output(extras_list):
    out_file=open("ovation.out","w")
    upper=len(extras_list)
    for i in range(upper):
        out_file.writelines("Case #{}: {}\n".format(str(i+1),extras_list[i]))
    out_file.close()
                      
                                      
def ovation():
    test_data=read_file()
    extras_list=[]
    for test in test_data:
        data=test.split(" ")
        S_max=int(data[0])
        people=data[1]
        up=0
        extras=0
        for k in range(S_max+1):
           #print ("{} people with shyness level {}".format(people[k], k) )
           if k > up and int(people[k])>0:
               #print ("{} extras needed".format(k-up))
               extras=extras+(k-up)
               up=up+extras
           up=up+int(people[k])
        extras_list.append(extras)
    write_output(extras_list)

        
    
          
          
    
