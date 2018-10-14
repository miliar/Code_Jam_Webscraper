input_file = open("B-large.in","r")
output = open("B-large.out","w")
T = int(input_file.readline())

for test in xrange(1,T+1):
    answer = 0
    case = [int(i) for i in input_file.readline().split()]
    [[N,surprise,best],scores] = [case[:3],case[3:]]
    for score in scores:
        s1 = score/3
        score -= s1
        s2 = score/2
        s3 = score - s2
        if(s3 >= best):
            answer +=1
        elif(s3 == best-1):
            
            if(surprise > 0):
                if(s1 == s3):
                    if(s1 != 0):
                        answer +=1
                        surprise -= 1
                elif(s2 == s3):
                    answer += 1
                    surprise -= 1
    #print ("Case #" + str(test) + ": " + str(answer))
    output.write("Case #" + str(test) + ": " + str(answer) + "\n")

input_file.close()
output.close()


    
