import re
def Lawnmower(lawn):
    row_maxes = [max(x) for x in lawn]
    cols = [[lawn[i][j] for i in range(len(lawn))] for j in range(len(lawn[0]))]
    col_maxes = [max(x) for x in cols]
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            val = lawn[i][j]
            if val != row_maxes[i] and val != col_maxes[j]:
                return "NO"
    return "YES"



def read_game(f):
    dim = re.split(" ",f.readline())
    N,M = int(dim[0]), int(dim[1])    
    lawn = []
    for i in range(N):
        line = f.readline()
        nums = [int(x.strip()) for x in re.split(" ",line)]
        lawn.append(nums)
    return lawn
def main():
    output = []
    with open("input.txt","r") as f:
        trials = f.readline()
        for i in range(int(trials.strip())):
            lawn = read_game(f)
            #f.readline()
            outline = "Case #%d: %s" % (i+1, Lawnmower(lawn))
            print outline
            output.append(outline)
    with open("out.txt","w") as f:
        f.write("\n".join(output))

if __name__ == "__main__":
    main()