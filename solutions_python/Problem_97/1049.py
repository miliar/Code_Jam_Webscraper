kb = []
output = open('dancing.in', 'w')

def read(path):
    f = open(path)
    x = 1
    f.readline()
    for line in f:
        line = line.strip('\n')
        list = line.split(" ")
        A = list[0]
        B = list[1]
        n = int(A)
        count = 0
        while n <= int(B):
            strN = str(n)
            i = 1
            while i < len(strN):
                i = i + 1
                bound = len(strN)-1
                strN = strN[bound] + strN[0:bound]
                m = int(strN)
                if m <= int(B) and n < m:
                    count = count + 1
            n = n + 1
        out = "Case #" + str(x) + ": " + str(count) + "\n"
        output.write(out)
        x = x + 1
        print B

def close():
    output.close()
