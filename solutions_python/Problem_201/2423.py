import math

def minmax_one(N):
    if N%2==1:
        return [N//2,N//2] #max, min
    else:
        return [N//2,N//2-1]

def PbC(Input):
    f = open(Input)
    T = f.readline()
    T = int(T.rstrip('\n'))
    # print(T==4)
    out = open("output.txt",'w')
    count = 1
    for line in f:
        #print('Case # ' + str(count))
        L = line.rstrip('\n')
        L= L.split(' ')
        #print(N)

        N = int(L[0])
        K = int(L[1])

        Bathrooms = [N]
        
        for k in range(K):
            n_bath = len(Bathrooms)
            #print(Bathrooms)
            Min = -1
            for b in range(n_bath):
                Aux = minmax_one(Bathrooms[b])
                if Aux[1] > Min:
                    Min = Aux[1]
                    ind_mins = [b]
                else:
                    if Aux[1]== Min:
                        ind_mins = ind_mins + [b]

            if len(ind_mins)==1:
                chosen_bath = ind_mins[0]
            else:
                Max = -1
                for index in ind_mins:
                    Aux = minmax_one(Bathrooms[index])
                    if Aux[0] > Max:
                        Max = Aux[0]
                        ind_maxs = [index]
                    else:
                        if Aux[0] == Max:
                            ind_maxs = ind_maxs + [index]
                chosen_bath = ind_maxs[0]
            #print(chosen_bath)
            if k == K-1:
                out.write('Case #'+str(count)+': '+str(minmax_one(Bathrooms[chosen_bath])[0])+ ' ' + str(minmax_one(Bathrooms[chosen_bath])[1])+'\n')
                count = count+1
                break
            else:
                if Bathrooms[chosen_bath]==1:
                    Bathrooms = Bathrooms[0:chosen_bath] + Bathrooms[chosen_bath+1:]
                else:
                    if Bathrooms[chosen_bath]==2:
                        Bathrooms = Bathrooms[0:chosen_bath] + [1] + Bathrooms[chosen_bath+1:]
                    else:
                        Bathrooms = Bathrooms[0:chosen_bath] + [minmax_one(Bathrooms[chosen_bath])[1]] + [minmax_one(Bathrooms[chosen_bath])[0]] + Bathrooms[chosen_bath+1:]




    out.close()
        
