class SafeBetting:
    def minRounds(self, N):

        st = str(N)
        length = len(st)
        j = length - 1;
        num = N;
        if length==1:
            return N
        for i in range(length - 1, 0, -1):
            qian = int(st[i - 1])
            hou = int(st[i])
            if hou < qian:
                num = N - (hou + 1) * pow(10, (length - i - 1))
                if i != length - 1:
                    shengxia = int((length - i - 1) * '9') - int(st[i + 1:])
                    num = num + shengxia;
        return num


test = SafeBetting()
result = test.minRounds(1000)
print(result)
i = 0
f=open("C:\\Users\\davy\\Desktop\\output.txt","w+")
for line in open("C:\\Users\\davy\\Desktop\\12.txt"):
    i = i + 1;
    result = test.minRounds(int(line))
    if i>1:
        f.writelines('Case #' + str(i-1) + ': ' + str(result) + '\n')

