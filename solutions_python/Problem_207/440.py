import math

def horseString(horses):
    N, R, O, Y, G, B, V = horses
    horseString=["_" for i in range(N)]
    (l, lChar), (m, mChar), (n, nChar) = sorted([(R, "R"), (Y, "Y"), (B, "B")])
    horseArr=[R, O, Y, G, B, V]
    if R * 2 > N or Y * 2 > N or B*2>N:
        return "IMPOSSIBLE"
    
    for i in range(N):
        if i % 2 == 1:
            continue
        if n > 0:
            horseString[i]=nChar
            n-=1
        elif l > 0:
            horseString[i]=lChar
            l-=1
    for i in range(N):
        if i % 2 == 0:
            continue
        if l > 0:
            horseString[i]=lChar
            l-=1
        elif m > 0:
            horseString[i]=mChar
            m-=1
    return "".join(horseString)
        
def main():
    t=int(input())
    for number in range(1, t + 1):
        horses = [int(x) for x in input().split(" ")]
        print("Case #{}: {}".format(number, horseString(horses)))
        
main()