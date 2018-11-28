#recycle

t = int(raw_input())
for i in range(0,t):
    input = raw_input().split(" ")
    count = 0
    a = input[0]
    b = input[1]
    ai = int(a)
    bi = int(b)


    if len(a) == 1 and len(b) == 1 or ai >= bi:
        count = 0
    else:

        for j in range(ai,bi+1):

            old = []
            rotate = str(j)
            l = len(rotate)
            for k in range(0,len(a)):
                rotate = rotate[-1] + rotate[0:(l-1)]
                if int(rotate) <= bi and int(rotate) >= ai and int(rotate) > j:
                    if int(rotate) not in old:
                        count += 1
                        old.append(int(rotate))
                    
    print "Case #" + str(i+1) + ": " + str(count)





    
