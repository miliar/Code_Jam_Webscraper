def find_time (c,f,x):
    if (x < c): return x/2
    current,time,rate = 0,0,2
    while(x/rate > ((c/rate) + x/(rate+f))):
        time += c/rate
        rate += f       
    return time + x/rate

 

with open("B-output.txt", "w") as output:
    with open("B-large.in", "r") as input:
        N = int(input.readline().strip())
        for i in range (0,N):
           C,F,X = map(float, input.readline().strip().split())
           print ('Case #' + str(i+1) + ': ' + str(find_time(C,F,X)),file=output)
           




