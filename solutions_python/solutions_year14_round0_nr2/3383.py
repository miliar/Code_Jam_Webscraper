file = open("B-small-attempt1.in", 'r')
input = file.readlines()
file.close()
file = open("B-small-attempt1.out", "w")

count = 1
T = int(input[0])

for k in range(1, T + 1):
    row1= input [count]
    count += 1
    
    row = []
    index = 0
    for i in range (len (row1)):
        if (row1 [i:i+1] == " "):
            row.append (row1 [index:i])
            index = i + 1
    row.append (row1 [index:-1])
    
    C = float (row[0])
    F = float (row[1])
    X = float (row[2])
    
    #wait for farm
    time = []
    speed = 2.0
    for i in range (int (X / C + F)):
        time.append(C / speed)
        speed += F
    
    #wait for cookies
    time2 = set ()
    speed = 2
    for i in range (int (X / C + F)):
        farm_time = 0
        for j in range (i):
            farm_time += time [j]
        print k, farm_time + X/speed
        
        time2.add(farm_time + X / speed)  
        speed += F  
   
    
    file.write("Case #" + str(k) + ": " + str (min (list (time2))) + "\n")
    
file.close()
