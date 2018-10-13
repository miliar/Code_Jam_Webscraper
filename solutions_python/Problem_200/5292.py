
#Tidy Numbers

def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return False
    return True


T = input()
for i in range(int(T)):
    #print(i)
    N = input()
    Temp = N
    for j in range(int(N)):
        #print(i)
        #
        if(isInAlphabeticalOrder(Temp)==True):
            print("Case #"+str(i+1)+": " + Temp)
            break;
        N = int(N)-1
        Temp = str(N)
#print ("End")




