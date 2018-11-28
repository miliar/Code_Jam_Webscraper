from sys import stdin, stdout

def solve(s):
    start = int(s.split()[0])
    end = int(s.split()[1])
    count = 0

    for i in range(start, end, 1):
        for j in range(i+1, end+1, 1):
            if (str(j)*2).find(str(i)) >= 0:
                count += 1
    return count
        

line_count = int(stdin.readline())
for i in range(line_count):
    print("Case #"+str(i+1)+": "+str(solve(stdin.readline()[:-1])))
