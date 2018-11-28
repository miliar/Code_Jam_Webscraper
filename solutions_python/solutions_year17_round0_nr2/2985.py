def listar(num):
    lista = [int(i) for i in str(num)]
    return lista

def fun(num):
    lis = listar(num)
    for i in range(1,len(lis)):
        if lis[-i] < lis[-i-1]:
            lis[-i] = 9
            lis[-i-1] -= 1
    aux = 0
    for i in range(len(lis)):
        if aux == 9:
            lis[i] = 9
        elif lis[i] == 9:
            aux=9
    return int(''.join(map(str,lis)))

t = int(input())
for i in range(1, t + 1):
  n = input()  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, fun(int(n))))