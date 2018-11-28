#Nathan Lenz

def main():
    lines = eval(input())
    for x in range(1, lines+1):
        line = input()
        maxShy, idv = line.split()
        maxShy = eval(maxShy)
        friends = 0
        total = 0
        for i in range(maxShy+1):
            total += int(idv[i])
            while( i+1 > total+friends):
                friends += 1
        print("Case #", x, ": ", friends, sep='')

main()
