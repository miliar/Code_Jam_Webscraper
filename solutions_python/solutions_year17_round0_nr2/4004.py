def rompe(string):
    for i in range(len(string)-1):
        if int(string[i]) > int(string[i+1]):
            return i+1
    return -1

def mayor(string):
    l = [int(x) for x in string]
    if l == []:
        return 0
    m = max(l)
    return l.index(m)

def main():
    cases = int(input())
    for i in range(1,cases+1):
        n = input()


        le = len(n)
        rom = rompe(n)

        if rom == -1:
            print("Case #{}: {}".format(i,n))
        else:
            may = mayor(n[:rom])
            aux = int(n[may])
            cambio = aux - 1 if (aux-1) > 0 else 0
            res = int(n[:may] + str(cambio) +(len(n[may:])-1)*'9')
            print("Case #{}: {}".format(i,res))

main()
