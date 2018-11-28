single_comb = []
double_comb = []

def gen_tuple(num):
    tup = []
    if (num % 3 == 0):
        tup.append([num / 3, num / 3, num / 3])
        tup.append([num / 3 - 1 , num / 3, num / 3 + 1])
    elif (num % 3 == 1):
        tup.append([num / 3, num / 3, (num / 3) + 1])
        tup.append([(num / 3) + 1, (num / 3) + 1, (num / 3) - 1])
    elif (num % 3 == 2):
        tup.append([num / 3, (num / 3) + 1, (num / 3) + 1])
        tup.append([num / 3, num / 3, num / 3 + 2])
        
    return tup

single_comb.append([0,0,0])
single_comb.append([0,0,1])
single_comb.append([10,10,9])
single_comb.append([10,10,10])

for i in range (2, 29):
    double_comb.append(gen_tuple(i))
        
f = open('C:/Users/SACHIN/Desktop/B-large.in', 'r')
g = open('C:/Users/SACHIN/Desktop/ouput.txt', 'w')
inp = f.readlines()


for i in range(1,len(inp)):
    line = inp[i].split()
    N = int(line[0])
    S = int(line[1])
    p = int(line[2])
    count = 0
    surp = 0
    for j in range(0,N):
        val = int(line[j+3])
        if val < 2 :
            if max(single_comb[val]) >= p:
                count += 1
        elif val > 28 :
            if max(single_comb[val-27]) >= p:
                count += 1
        else:
            if max(double_comb[val-2][0]) >= p:
                count += 1
            elif max(double_comb[val-2][1]) >= p:
                surp += 1
    
    if surp > S:
        count = count + S
    else:
        count = count + surp
    output_str = "Case #" + str(i) + ": " + str (count)+ "\n"
    g.write(output_str)
    
                
                
          
        
    
    












