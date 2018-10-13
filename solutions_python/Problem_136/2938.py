fread = open("infileL.txt","r")
fwrite = open("outfileL.txt","w")

t = int(fread.readline())
for i in range(t):
    cfx=fread.readline().split(" ")
    c =  float(cfx[0])
    f = float(cfx[1])
    x = float(cfx[2])
    time = 0.0
    pres = 0.0
    rate = 2.0
    while(1):
        if (x-pres)/rate > (((c-pres)/rate)+((x)/(rate+f))):
            time += (c-pres)/rate
            pres =0
            rate += f
        else:
            time += (x-pres)/rate
            pres = x
            List = str(time).split(".")
            if(len(List[1])>=7):
                ans = "case #"+str(i+1)+": "+List[0]+"."+List[1][:7]+"\n"
            else:
                ans = "case #"+str(i+1)+": "+List[0]+"."+List[1]+"\n"
            fwrite.write(ans)
            break

fwrite.close()
