def check(lista):
    return sum(lista) == len(lista)

def convert(string):
    return [True if i=='+' else False for i in string]

def invert(lis):
    return [not i for i in lis]
    
def fun(string,n):
    lista = convert(string)
    count = 0
    for i in range(len(lista)-n+1):
        if not lista[i]:
            lista[i:i+n] = invert(lista[i:i+n])
            count += 1
    res = 'IMPOSSIBLE'
    if check(lista):
        res = count
    return res

t = int(input())
for i in range(1, t + 1):
  n, m = input().split(" ")  # read a list of integers, 2 in this case
  print("Case #{}: {}".format(i, fun(n, int(m))))