#!/usr/bin/python



def tobin(x, count=8):
        """
        Integer to binary
        Count is number of bits
        """
        return "".join(map(lambda y:str((x>>y)&1), range(count-1, -1, -1)))
        
def toDecimal(x):
            return sum(map(lambda z: int(x[z]) and 2**(len(x) - z - 1),
                           range(len(x)-1, -1, -1)))


def addition(x, y):
    
    x_bin = tobin(x)
    y_bin = tobin(y)

    res = ""

    for i in range(7,-1, -1):
        somme = int(x_bin[i])+int(y_bin[i])


        if somme == 0:
            res="0"+res
        elif somme == 1:
            res="1"+res
        elif somme == 2:
            res = "0"+res
        elif somme == 3:
            res= "1"+res

    return toDecimal(res)
    
def addition_list(list):
    res = 0
    for i in list:
        res = addition(i,res)
    return res


# PowerSet of a List
def PowerSet(orignal_list):
    list_size = len(orignal_list)
    num_sets = 2**list_size
    powerset = []
    # Don't include empty set
    for i in range(num_sets)[1:]:
        subset = []
        binary_digits = list(tobin(i,list_size))
        list_indices = range(list_size)
        for (bit,index) in zip(binary_digits,list_indices):
            if bit == '1':
                subset.append(orignal_list[index])
        powerset.append(subset)
    return powerset
            
    
def max(candy):
    gauche = PowerSet(candy)

    gauche = gauche[:len(gauche)/2]

    droite = []
    
    for x in gauche:
        dr = list(candy)
        for z in x :
            try:
                dr.remove(z)
            except:
                pass
        if not dr:
            gauche.remove(x)
        else:            
            droite.append(dr)

        
    # print "gauche: ", gauche
    # print "droite: ", droite
    
    res = 0

    for i in range(len(gauche)):
        # print "ga:", gauche[i]
        # print "dr:", droite[i]
        tmp1 = addition_list(gauche[i])
        tmp2 = addition_list(droite[i])
        # print "=====1"
        somme_droite = sum(droite[i])

        somme_gauche = sum(gauche[i])

        if tmp2==tmp1:
            if somme_gauche >= somme_droite:
                res_tmp = somme_gauche
            else :
                res_tmp = somme_droite
                
            if res < res_tmp:
                res = res_tmp
        # else:
        #     print "%d || %d" %(tmp2, tmp1)
    if res == 0:
        return "NO"
    return res
    
fichier = open("C-small-attempt1.in", "r")
sortie = open("output.txt", "w")
lignes = fichier.readlines()

nb_case = lignes[0].strip("\n")
lignes.pop(0)

# print "nb case: ", nb_case

# print lignes

i = 0
index = 1
while i < len(lignes) :

    
    nb = lignes[i].strip("\n")
    candy = lignes[i+1].strip("\n").split()
    
    candy = [int(y) for y in candy]
    
    
    # PARCOURS le paquet de bonbon
    somme = 0
    for c in candy:
        
        somme = addition(somme, c)
    
    if somme%2:
        # print "impaire"
        rep = "NO"
    else:
        rep = max(candy)
    print "%s/%s" %(index, nb_case)
    sortie.write("Case #%d: %s\n" %(index, rep))
    
    
    # print "nb : ", nb
    # print "candy : ", candy
    # print "somme : ", somme
    # print "REPONSE : ", rep
    # print "~~~~~~~~~~~~~~~~~~~~~~~"
    
    i=i+2
    index = index+1

fichier.close()

