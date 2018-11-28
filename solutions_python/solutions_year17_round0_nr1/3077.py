


def flip(part):
    for i in range(len(part)):
        if part[i]=="+":
            part[i]="-"
        elif part[i]=="-":
            part[i]="+"
    return(part)




def main(n, m):
    number_flips = 0
    for i in range(len(n)):
        if n[i]== '-' and i + m <= len(n):
            part = flip(n[i: i+m])
            n[i : i+m] = part
            number_flips += 1
        elif n[i]== '-' and i + m > len(n):
            number_flips = "IMPOSSIBLE"
    return number_flips




lines = int(input())
for i in range(1, lines + 1):
    n, m = [str(s) for s in input().split(" ")]
    n = list(n)
    m = int(m)
    result = main(n, m)
    print("Case #{}: {}".format(i, result))




