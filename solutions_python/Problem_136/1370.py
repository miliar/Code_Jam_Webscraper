
def function (c, f, x):
    if x <= c :
        time = x/2.0
    else:
        time = c/2.0
        i = 0
        v = 2.0
        while ((x-c)/v > x/(v+f)):
            v += f
            time += c/v
        time += (x-c)/v
    return time


if __name__ == "__main__":
    fin = open('B-large.in', 'rb')
    input = fin.read().split('\n')
    t = int(input[0])
    fout = open('output_large.txt','w')
    for i in range(t):
        list = [float(j) for j in input[i+1].split(" ")]
        c = list[0]
        f = list[1]
        x = list[2]
        result = function(c,f,x)
        #print("Case #"+str(i) + ": " + "%.7f" % result )
        fout.write("Case #"+str(i+1) + ": " + "%.7f" % result + "\n")
    fin.close()
    fout.close()