def get_cases(g,t):
    list_test = []
    for i in range(t):
        q = g.readline().strip()
        list_per_line = q.split(" ")
        list_test.append(list_per_line)
    return list_test

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
f1 = open("output22.txt","w")

s = f.readline().strip()
num_cases = int(s)

gain = 2.0
test_values = get_cases(f,num_cases)

count = 1
for i in test_values:
    C = float(i[0])
    F = float(i[1])
    X = float(i[2])

    time_required = calculate_time(C,F,X,gain)
    f1.write("Case #"+str(count)+": "+str(time_required)+"\n")
    count += 1

f.close()
f1.close()
    
