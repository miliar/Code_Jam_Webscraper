def flip(symbol):
    if symbol == '+':
        return '-'
    return '+'

def main():  
    T = int(input())

    for i in range(0,T):
        line = str(input()).split(" ")
        S = line[0]
        k = int(line[1])

        flips = 0
        for j in range(0, len(S)-(k-1)):
            if S[j] == '+':
                continue                      
            else:     
                flips = flips + 1
                for position in range(j, j+k):
                    S = S[:position] + flip(S[position]) + S[position+1:]

        if '-' in S:
            print("Case #" + str(i+1) + ": IMPOSSIBLE")
        else:
            print("Case #" + str(i+1) + ": " + str(flips))

if __name__ == "__main__":
    main()
