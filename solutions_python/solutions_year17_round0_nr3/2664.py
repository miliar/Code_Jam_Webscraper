import sys        

def case(n, s):
    print("Case #" + str(n+1) + ": " + s)

Input = open("C-small-2-attempt1 (1).in", "r")

T = int(Input.readline()[:-1])
for i in range(T):
    N, K = (int(n) for n in Input.readline()[:-1].split())
    empty = [[N, 1]]
    while K > 0:
        Max = max([n[0] for n in empty])
        for k in range(len(empty)):
            if empty[k][0] == Max:
                if K >= empty[k][1]:
                    if Max % 2 == 0:
                        if(Max/2-1 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == int(Max/2-1):
                                    empty[l][1] += empty[k][1]
                                    break
                            else:
                                empty.append([int(Max/2-1), empty[k][1]])
                        if(Max/2 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == int(Max/2):
                                    empty[l][1] += empty[k][1]
                                    break
                            else:
                                empty.append([int(Max/2), empty[k][1]])
                    else:
                        if((Max-1)/2 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == (Max-1)/2:
                                    empty[l][1] += empty[k][1]*2
                                    break
                            else:
                                empty.append([int((Max-1)/2), empty[k][1]*2])
                    K += -empty[k][1]
                    empty.pop(k)

                else:
                    if Max % 2 == 0:
                        if(Max/2-1 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == int(Max/2-1):
                                    empty[l][1] += min(K, empty[k][1])
                                    break
                            else:
                                empty.append([int(Max/2-1), min(K, empty[k][1])])
                        if(Max/2 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == int(Max/2):
                                    empty[l][1] += min(K, empty[k][1])
                                    break
                            else:
                                empty.append([int(Max/2), min(K, empty[k][1])])
                    else:
                        if((Max-1)/2 > 0):
                            for l in range(len(empty)):
                                if empty[l][0] == (Max-1)/2:
                                    empty[l][1] += min(K, empty[k][1])*2
                                    break
                            else:
                                empty.append([int((Max-1)/2), min(K, empty[k][1])*2])
                    K += -1*min(K, empty[k][1])
                    if empty[k][1] > min(K, empty[k][1]):
                        empty[k][1] += min(K, empty[k][1])*-1
                    else:
                        empty.pop(k)
                break
        #print(empty, K)
    #print(Max)
    if Max % 2 == 0:
        case(i, str(int(Max/2)) + " " + str(int(Max/2-1)))
    else:
        case(i, str(int((Max-1)/2)) + " " + str(int((Max-1)/2)))
