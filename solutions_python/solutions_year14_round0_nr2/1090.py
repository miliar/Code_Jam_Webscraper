out = open("BLargeOut.txt", 'w')
text = open("BLarge.txt", 'r')
text = text.readlines()
#print(text)

def solve(a):
    c = a[0]
    f = a[1]
    x = a[2]
    r = 2
    t = 0
    while True:
        cut = (c / r) / (1 / r - 1 / (r + f))
        if cut < x:
            t += c / r
            r += f
        else:
            t += x / r
            return t            
        


tc = int(text[0])
line = 0
for c in range(tc):
    line += 1
    ints = [float(num) for num in text[line].split()]
    ans = solve(ints)
    #print(ans)
    out.write("Case #" + str(c + 1) + ": " + str(ans) + "\n")
out.close()
