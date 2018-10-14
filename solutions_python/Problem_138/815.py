f = open('input.in', 'r')
f2 = open('output2.out', 'w')

i = 1

def write(output):
    print(output, end="")
    f2.write(output)

def War(bloks, naomi, ken ):
    #print("--War-------------------")
    wins = 0
    i = 0
    while naomi:
        #print(i)
        if ken[0] < naomi[0]:
                k = ken.pop()
                n = naomi.pop(0)
                #print("naomi:", n, "ken", k, "Wins")
                #print("naomi",naomi)
                #print("ken",ken)
                wins += 1
        else:
            n = naomi.pop(0)
            k = ken.pop(0)
    write(str(wins))

def DWar(bloks, naomi, ken ):
    #print("--DWar-------------------")
    wins = 0
    i = 0
    while naomi:
        #print(i)
        if ken[0] < naomi[0]:
            k = ken.pop(0)
            n = naomi.pop(0)
            #print("naomi:", n, "ken", k, "Wins")
            #print("naomi",naomi)
            #print("ken",ken)
            wins += 1
        else:
            n = naomi.pop()
            k = ken.pop(0)
            #print("naomi:", n, "ken", k)
            #print("naomi",naomi)
            #print("ken",ken)
    write(str(wins)+" ")
            
            
        
            
def process(bloks, naomi, ken ):
    a = DWar(bloks, naomi[:], ken[:] )
    b = War(bloks, naomi, ken )
            
    

test_cases = int(f.readline())
for test_case in range(test_cases):
    bloks = int(f.readline())
    #print(bloks)
    
    naomi = f.readline().strip().split()
    naomi = sorted(naomi, reverse=True)
    #print("naomi",naomi)
     
    ken = f.readline().strip().split()
    ken = sorted(ken, reverse=True)
    #print("ken",ken)

    
    write("case #"+str(i)+": ")
    
    process(bloks, naomi, ken )
    
    i += 1
    write("\n")

f.close()
f2.close()
print("Done")
            
            
            
