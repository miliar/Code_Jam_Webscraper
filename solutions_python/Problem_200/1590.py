f = open("input.txt")
out = open("output.txt", "w")
t = int(f.readline().strip())

tt = 1
while tt <= t:
    num = list(f.readline().strip())
    i = 0
    while i < len(num)-1:
        if num[i] > num[i+1]:
            while i > 0 and num[i] == num[i-1]:
                i -= 1
            num[i] = str(int(num[i]) - 1)
            i += 1
            while i < len(num):
                num[i] = '9'
                i += 1
            break
        i += 1
    num = ''.join(num).lstrip('0')
    out.write("Case #" + str(tt) + ": " + num+"\n")
    tt += 1
