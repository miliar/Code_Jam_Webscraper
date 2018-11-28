import sys
sys.setrecursionlimit(2000)

T = int(input())
for t in range(1, T+1):
    n = input()
    dlzka = len(n)
    napor = '1'*dlzka
    print("Case #%d: " % t, end="")
    if n < napor:
        print('9'*(dlzka-1))
        continue

    devinky = dlzka
    cislo = [int(x) for x in n]
    for i in range(dlzka-1, 0, -1):
        if cislo[i-1] > cislo[i]:
            cislo[i-1] -= 1
            devinky = i
    print(*cislo[:devinky],'9'*(dlzka - devinky),sep="")
