def getAnswer(price, increase, goal):
    result = 0.0
    cur_rate = 2.0

    while (goal/cur_rate) > (goal/(cur_rate+increase)+price/cur_rate):
        result += price/cur_rate
        cur_rate += increase

    result += goal/cur_rate
    return result


response = ""
f = open("in.txt", "r")
data = f.readlines()
f.close()

cases = int(data[0].rstrip())
for i in xrange(cases):
    line = data[i+1].rstrip().split()
    c = float(line[0])
    f = float(line[1])
    x = float(line[2])
    ans = getAnswer(c,f,x)
    response += "Case #"+str(i+1)+": "+str(ans)+"\n"

f = open("out.txt", "w")
f.write(response)
f.close()