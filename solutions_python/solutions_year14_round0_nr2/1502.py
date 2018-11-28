lines = [line.strip() for line in open("c:\Users\Mingan\Downloads\B-large.in","r")]
data = []
output = open("c:\Users\Mingan\Downloads\Cookie Output.txt","w")
def clean_data(lines,data):
    for i in lines:
        data.append(list(i))
        temp = []
        temp2 = []
        if len(data[-1]) <= 3:
            temp2.append(float(''.join(data[-1])))
        else:        
            for j in data[-1]:
                if j != " ":
                    temp.append(j)
                else:
                    temp2.append(float(''.join(temp)))
                    temp = []
            temp2.append(float(''.join(temp)))
        data[-1] = temp2
    return data            

data = clean_data(lines,data)

T = data[0][0]
data.remove([T])

#data = [[30.0,1.0,2.0],[30.0,2.0,100.0],[30.50000,3.14159,1999.19990],[500.0,4.0,2000.0]]
def evaluate_realtime(cc,f,x):
    c = 0.0000
    cf = 0
    s = 0.0000
    while c < x:
        if c >= cc:
            s1 = (x - c)/(0.00000002 + float((f/100000000) * cf))
            s2 = (x - (c - cc))/(0.00000002 + float((f/100000000) * (cf + 1)))
            if s1 > s2:
                c = c - cc
                cf += 1
        scc = (cc - c)/ (0.00000002 + float((f/100000000) * cf))
        if scc > 0:
            a = 1 + scc
            if scc > (x - c)/(0.00000002 + float((f/100000000) * cf)):
                a = 1 + (x - c)/(0.00000002 + float((f/100000000) * cf))
        else:
            a = 1 + (x - c)/(0.00000002 + float((f/100000000) * cf))
        s += 0.00000001 * a
        c += (0.00000002 + float((f/100000000) * cf)) * a

    return s

#Case #1: 377.364809764
#Case #2: 158.783230039
#Case #3: 887.485238476
#Case #4: 784.744688735


def go_go(i):
    return evaluate_realtime(i[0],i[1],i[2])

counter = 1
solutions = []
for i in data:
    solution = go_go(i)
    print "Case #" + str(counter) + ": " +str(solution)
    solutions.append("Case #" + str(counter) + ": " +str(solution))
    counter += 1
for i in solutions:
    a=str(i)+str("\n")
    output.write(a)
output.close()    