def flip(x):
    if x == "+":
        return "-"
    return "+"

def main():
    T = input()
    for x in range(1, T+1):
        inp = raw_input().split(" ")
        cakes = list(inp[0])
        flipper_size = int(inp[1])
        flips = 0
        flag = True

        for y in range(0, len(cakes) - flipper_size + 1):
            if cakes[y] == "-":
                flips += 1
                for z in range(y, y+ flipper_size):
                    cakes[z] = flip(cakes[z])

        for y in range(0, len(cakes)):
            if cakes[y] == "-":
                flag = False
                break

        print "Case #" + str(x) + ":",
        if(flag == True):
            print flips
        else:
            print "IMPOSSIBLE"

        # Final scan...
main()
