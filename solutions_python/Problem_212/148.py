import math, sys

def main():
    T = int(sys.stdin.readline())
    for i in range(1, T + 1, 1):
        sys.stdout.write("Case #" + str(i) + ": " + solveCase() + "\n")

def solveCase():
    N, P = map(int, sys.stdin.readline().split())
    sizes = list(map(int, sys.stdin.readline().split()))
    modSizes = [0] * P
    fresh = 0

    for i in range(N):
        modSizes[sizes[i] % P] += 1

    fresh += modSizes[0]
    modSizes[0] = 0
    curUnfresh = 0
    while max(modSizes) > 0:
        if curUnfresh == 0:
            i = modSizes.index(max(modSizes))
            modSizes[i] -= 1
            curUnfresh = P - i
            fresh += 1

        elif modSizes[curUnfresh]:
            modSizes[curUnfresh] -= 1
            curUnfresh = 0

        else:
            i = modSizes.index(max(modSizes))
            modSizes[i] -= 1
            curUnfresh = (curUnfresh + P - i) % P

        
    return str(fresh)


    
    

if __name__ == "__main__":
    main()
