def war (p1, p2):
    result = 0
    right = 0
    for i in xrange(len(p1)):
        if (p1[i]>p2[right]):
           result+=1
           right +=1

            

    return result
        



with open('input.txt','r') as read:
    with open('output.txt', 'w') as write:
            total = read.readline()
            total = int(total)
            print total
            for i in xrange(total):
                num = int(read.readline())
                p1 = read.readline().split()
                p2 = read.readline().split()

                for j in xrange(len(p1)):
                    p1[j] = float(p1[j])
                    p2[j] = float(p2[j])

                p1.sort()
                p2.sort()
                write.write("Case #"+ str(i+1) +": " + str(war (p1, p2)) + " " + str(len(p1) - war(p2,p1))+ '\n')
                #print ("Case #"+ str(i+1) +": " + str(war (p1, p2)) + " " + str(len(p1) -war(p2,p1)))
    write.close()
read.close()
