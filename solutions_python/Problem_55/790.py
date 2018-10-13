def process(R,k,N,group):

        lap = 1
        result = 0
        while lap <= R:
                temp = []
                z = 0
                for z in range(N):
                        temp.append(group[z])
                group = []
                board = range(N)
                for i in range(N):
                        board[i] = 0
                board[0] = temp[0]
                
                i = 1
                while i in range(1,N):
                        foo = 0
                        for j in range(i):
                                foo = foo + board[j]
                        
                        if (k-foo) >= temp[i]:
                                board[i] = temp[i]
                                i+=1
                                if i == N:
                                        return (R * (foo+temp[i-1]))
                        else:                           
                                for bar in range(i,N):
                                        group.append(temp[bar])
                                for m in range(len(range(len(group),N))):
                                        group.append(temp[m])
                                i = N

                s = 0
                for n in range(N):
                        s = s + board[n]
                result = result + s
                lap+=1
        return result
                




f = open('small.in')
text = f.read()
f.close()
myset = text.split('\n')

del(myset[len(myset)-1])

case_num = 0
i = 0

while i < len(myset):
        print i
        case_num = case_num + 1
        R = int(myset[i].split()[0])
        k = int(myset[i].split()[1])
        N = int(myset[i].split()[2])
        group = []

        for var in range(N):
                group.append(int(myset[i+1].split()[var]))
        if N > 1:
                t = process(R,k,N,group)
        else:
                t = int(myset[i+1].split()[0]) * R
        f = open('small.out','a')
        f.write("Case #%s: %s\n" % (str(case_num), t))
        f.close()
        i+=2




