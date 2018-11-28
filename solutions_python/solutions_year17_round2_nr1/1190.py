
f = open("A-large.in");
f.readline() # Remove total tc cnt..
tc_cnt = 1;


while True:

    line = f.readline()
    if not line: break
    token = line.split(" ")
    D = int(token[0])
    N = int(token[1])

    speed_arr = []

    for x in range(N):
        line = f.readline()
        token = line.split(" ")
        speed_arr.append((D - int(token[0])) / int(token[1]))

    print("Case #"+str(tc_cnt)+": " + str(D/max(speed_arr)))

    tc_cnt+=1


f.close()

