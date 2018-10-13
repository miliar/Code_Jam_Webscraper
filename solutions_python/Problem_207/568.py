'''
def manager(N, R, O, Y, G, B, V):
    if O >= B:
        return 'IMPOSSIBLE'
    elif V >= Y:
        return 'IMPOSSIBLE'
    elif G >= R:
        return 'IMPOSSIBLE'
    result=''
    result += 'RG' * V + 'R'
    R -= G+1
    result += 'YV' * V + 'Y'
    Y -= V+1
    result+='BO'*O+'B'
    B -= O+1
    listn=[R,Y,B]
    lista=['R','Y','B']

    while min(listn) != 0:
        for i in range(3):
            if listn[i] == 0:
                continue
            if lista[i] == result[-1]:
                return 'IMPOSSIBLE'
            result+= lista[i]
            listn[i]-=1
    return result
    '''


def manager2(R, Y, B,):
    lista = [[R,'R'],[Y,'Y'],[B,'B']]
    lista.sort(key=lambda x: x[0])
    listv=[]
    listl=[]
    answer=''
    for el in lista:
        listv.append(el[0])
        listl.append(el[1])
    if listv[0]+listv[1]<listv[2]:
        return 'IMPOSSIBLE'
    steps = listv[2]-listv[1]
    answer += (listl[2]+listl[0])*steps
    listv[2] -= steps
    listv[0] -= steps

    steps =listv[2]-listv[0]
    answer += (listl[2] + listl[1]) * steps
    listv[2] -= steps
    listv[1] -= steps
    steps = listv[0]
    answer += (listl[2] + listl[1]+listl[0]) * steps
    return answer


t = int(input())
for i in range(1, t + 1):
    N, R, O, Y, G, B, V = [int(s) for s in input().split(" ")]
    result = manager2(R, Y, B,)
    print("Case #{}: {}".format(i, result))
