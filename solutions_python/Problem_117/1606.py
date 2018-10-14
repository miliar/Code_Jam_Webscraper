f = open('B-small-attempt0.in', 'r')
q = open('output', 'w')
x = f.readlines()

for i in range(len(x)):
    x[i] = x[i].split()
#x = [item for sublist in x for item in sublist]

t = int(x[0][0])

counter = 1
field = []

for i in range(t):
    Value = "YES"
    N = int(x[counter][0])
    M = int(x[counter][1])
    for j in range(N):
        field.append(x[counter+1])
        counter += 1
        
    field2 = zip(*field)
    
    for h in range(N):
        for o in range(M):
            if (field[h][o] < max(field[h])) and (field2[o][h] < max(field2[o])):
                Value = "NO"

    q.write("Case #" + str(i+1) + ": " + str(Value) + "\n")
    counter += 1
    field = []

f.close()
q.close()
print "Finished"
