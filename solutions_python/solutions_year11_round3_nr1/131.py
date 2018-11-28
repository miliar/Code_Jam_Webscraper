
failed = False

def fail():
    global failed
    failed = True
    print "Impossible"

with open('A.in', 'r') as fin:
    lines = fin.readlines()

T = int(lines[0])
nextline = 1

for t in range(T):
    failed = False
    print "Case #{0}:".format(t+1)
    line = lines[nextline]
    nextline+=1
    bits = line.split()
    R = int(bits[0])
    C = int(bits[1])
    picture = []
    for r in range(R):
        picture.append(list(lines[nextline].strip()))
        nextline+=1
    for r in range(R):
        if failed:
            break
        for c in range(C):
            if failed:
                break
            if picture[r][c] == '#':
                # Try to replace a 2x2 square
                picture[r][c] = '/'
                if r >= R-1 or c >= C-1:
                    fail()
                elif picture[r+1][c] == '.' or picture[r][c+1] == '.' or picture[r+1][c+1] == '.':
                    fail()
                else:
                    picture[r+1][c] = '\\'
                    picture[r][c+1] = '\\'
                    picture[r+1][c+1] = '/'
    if not failed:
        answer = ''
        for r in range(R):
            answer = answer + ''.join(picture[r])
            if r < R - 1:
                answer += '\n'
        print answer
                    
                    
