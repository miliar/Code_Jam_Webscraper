def war(Naomi,Ken,Blocks):

    Cnt_N = 0
    
    for i in range(0,Blocks):
        mini = min(Naomi)
        Naomi.remove(mini)
        lt = []
        for j in range(0,Blocks):
            
            if(Ken[j]> mini):
                lt.append(Ken[j])
        
        if len(lt) == 0:
            Cnt_N += 1
            Ken.remove(min(Ken))
        else:
            Ken.remove(min(lt))

        Blocks -= 1
        i=0
    return Cnt_N        

def decietwar(Naomi,Ken,Blocks):
    Cnt_N = 0

    for i in range(0,Blocks):
        
        if(max(Naomi)>max(Ken)):
            Cnt_N += 1
            Naomi.remove(max(Naomi))
            Ken.remove(max(Ken))
        else:
            Naomi.remove(min(Naomi))
            Ken.remove(max(Ken))

    return Cnt_N 


fob = open("wr","r")
TestCases = int(fob.readline())
Counter = 1
while TestCases != 0:
    

    Blocks = int(fob.readline())
    Naomi = fob.readline().split()
    Ken = fob.readline().split()

    Answer1 = war(Naomi.copy(),Ken.copy(),Blocks)
    Answer2 = decietwar(Naomi,Ken,Blocks)

    print("Case #{}: {} {}".format(Counter,Answer2,Answer1))

    Counter += 1
    TestCases -= 1
    
