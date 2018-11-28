def maxSpeed(D, horses):
    bestTime=0
    for horse in horses:
        arrivalTime=(D-horse[0])/horse[1]
        if arrivalTime > bestTime:
            bestTime=arrivalTime
    return D/bestTime
        

def main():
    t=int(input())
    for number in range(1, t + 1):
        D, N = input().split(" ")
        D=int(D)
        N=int(N)
        horses=[]
        for i in range(N):
            horses.append([int(x) for x in input().split(" ")])
        
        print("Case #{}: {}".format(number, maxSpeed(D, horses)))
        
main()