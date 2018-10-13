def main():
    f = open("/home/ayush/random.txt","r+")
    y = f.readlines()
    t = int(y[0])
    x = 1
    while x<=t:
        s,arr = y[x].split()
        s = int(s)
        summ = 0
        count = 0
        for i in xrange(0,s+1):
            summ+=int(arr[i])
            if arr[i]=='0' and (i+1 - summ >=0):
                count+= i-summ+1
                summ += i-summ+1
        print 'Case #'+`x`+': '+`count`
        x+=1
main()
