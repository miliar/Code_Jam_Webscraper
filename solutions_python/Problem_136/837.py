def get_test_values(f,t):
    test_list = []
    for i in range(t):
        s = f.readline().strip()
        list_per_line = s.split(" ")
        test_list.append(list_per_line)
    return test_list

def calculate_time(C,F,X,G):
    time_1 = X/G
    time_2 = C/G + X/(G+F)
    time = 0
    if(time_1 <= time_2):
        time = time_1
        return time
    else:
        while(time_1 > time_2):
            time += C/G
            G = G + F
            time_1 = time + X/G
            time_2 = time + C/G + X/(F+G)
            
    time += X/G
    return time
    

    
f = open("B-large.in")
f1 = open("output.txt","w")

s = f.readline().strip()
test_case = int(s)

gain = 2.0
test_values = get_test_values(f,test_case)

count = 1
for i in test_values:
    C = float(i[0])
    F = float(i[1])
    X = float(i[2])

    req_time = calculate_time(C,F,X,gain)
    f1.write("Case #"+str(count)+": "+str(req_time)+"\n")
    #print "actual time = "+str(req_time)
    count += 1

f.close()
f1.close()
    
