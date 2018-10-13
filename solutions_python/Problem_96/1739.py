import sys

def main():
    infile = sys.argv[1]
    
    ofile = open('b.out', 'w')

    with open(infile, 'r') as file:
        numlines = int(file.readline())
        for i in range(numlines):
            line = map(int, file.readline().split())
            N = line[0]
            S = line[1]
            p = line[2]
            scores = line[3:]
            poss, yes = count(p, scores)
            ofile.write("Case #" + str(i+1) + ": " + str(yes + (S if (S < poss) else poss)) + "\n")
            
def count(p, list):
    c = 0
    h = 0
    for item in list:
        if (item >= p*3-2):
            h += 1
        elif (highscore(item) >= p):
            c += 1
    return c, h
        
def highscore(num):
    if (num == 0):
        return 0
    if (num % 3 == 0):
        return num/3 + 1
    elif (num % 3 == 2):
        return (num-2)/3 + 2
    else:
        return (num-1)/3 + 1
        
if __name__ == "__main__":
    main()