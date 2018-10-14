def solve(lawn):
    transpose = [list(tup) for tup in zip(*lawn)]
    lawn_max = [max(x) for x in lawn]
    transpose_max = [max(x) for x in transpose]
    for i in range(len(lawn)):
        for j in range(len(lawn[i])):
            height = lawn[i][j]
            if height != lawn_max[i] and height != transpose_max[j]:
                return "NO"
    return 'YES'

output=[]
with open('B-large.in','r') as f:
    for z in range(int(f.readline())):
        line = f.readline().split()
        n,m = int(line[0]),int(line[1])
        lawn = []
        for x in range(n):
            line = f.readline().split()
            a = [int(m) for m in line]
            lawn.append(a)
        outline = 'Case #'+str(z+1)+': '+solve(lawn)
        output.append(outline)

with open('B-large.out','w') as f:
    f.write('\n'.join(output))
    
    
