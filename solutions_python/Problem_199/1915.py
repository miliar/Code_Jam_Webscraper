
for i in range(int(input())):
        lst = input().split()
        leng = int(lst[1])
        strn = list(lst[0])
        lol = 0
        while(True):
                if '-' in strn :
                        t = strn.index('-')
                        if(t+leng > len(strn)):
                                print("Case #"+i+1+": IMPOSSIBLE")
                                break
                        for j in range(leng):
                                if(strn[t+j]=='-'):
                                        strn[t+j] = '+'
                                else:
                                        strn[t+j] = '-'
                        lol += 1
                else :
                        print("Case #"+str(i+1)+":",lol)
                        break
