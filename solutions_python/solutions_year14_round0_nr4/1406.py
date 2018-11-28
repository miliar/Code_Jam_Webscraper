from heapq import nlargest


def GetNumber(temp, templist):
    list = [t for t in templist if float(temp) < float(t)]
    #print(list)
    if list: return min(list)
    else: return None 

with open("D-large.in", "r") as f:
    num_case = int(f.readline())
    #lst.append(f.readline().split())

    for n in range(1, num_case + 1):

        numOfblock = int(f.readline())
        naomi =(f.readline().split())
        ken =(f.readline().split())

        Warnaomi = naomi[:]
        Warken = ken[:]
        
        naomiScore = 0
        warScore = 0

        while (naomi and ken):
            if(min(naomi) < min(ken)):
                #print("burn naomi ",min(naomi))
                #print("burn ken",max(ken))
                naomi.remove(min(naomi))
                ken.remove(max(ken))

            elif(min(naomi) > max(ken)):
                naomiScore = naomiScore+1
                #print("burn naomi ",min(naomi))
                #print("burn ken",min(ken))
                naomi.remove(min(naomi))
                ken.remove(min(ken))
                
            elif(min(naomi)> min(ken)):
                naomiScore = naomiScore+1
                #print("burn naomi ",min(naomi))
                #print("burn ken",min(ken))
                naomi.remove(min(naomi))
                ken.remove(min(ken))  

            else:
                print("None")   

        while (Warnaomi and Warken):
            
            if(min(Warnaomi) < min(Warken)):
                #print("burn naomi ",min(Warnaomi))
                #print("burn ken",min(Warken))
                Warnaomi.remove(min(Warnaomi))
                Warken.remove(min(Warken))

            elif(min(Warnaomi) > min(Warken)):
                chosenKen = GetNumber(min(Warnaomi), Warken)
                #print("ken " ,min(Warnaomi), chosenKen)
                if(chosenKen == None):
                    warScore = warScore + 1
                    #print("burn naomi ",min(Warnaomi))
                    #print("burn ken",max(Warken))
                    Warnaomi.remove(min(Warnaomi))
                    Warken.remove(min(Warken))
                else:
                    #print("burn naomi ",min(Warnaomi))
                    #print("burn ken",max(Warken))
                    Warnaomi.remove(min(Warnaomi))
                    Warken.remove(chosenKen)


        print("Case #{0}: {1} {2}".format(n, naomiScore, warScore))

