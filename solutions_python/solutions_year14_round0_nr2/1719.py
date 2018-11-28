import sys
sys.setrecursionlimit(10000)
a = []
def produce(c, f, x, time):
    rate = 2+time*f
    directTime = float(x/rate)
    rate1 = 2+(time+1)*f
    unDirectTime = float(c/rate) + float(x/rate1)
    if directTime > unDirectTime:
        a.append(float(c/rate))
        produce(c, f, x, time+1)
    else:
        a.append(float(x/rate))
    
def load():
    result = []
    ff = open("B-small-attempt2.in", "r")
    n = int(ff.readline())
    for i in range(n):
        line = ff.readline()
        list1 = line.split(" ")
        c = float(list1[0])
        f = float(list1[1])
        x = float(list1[2])

        produce(c, f, x, 0)
        result.append(sum(a))
        del a[:]
    ff.close()

    ff = open("output", "w")
    for index, value in enumerate(result):
        ff.write("Case #"+str(index+1)+": "+"%.7f"%value+"\n")
    ff.close()

load()
