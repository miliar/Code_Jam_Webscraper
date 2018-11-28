


def rotate(number):
    num = number[1:] + number[0]
    return num

#
#Case #1: 0
#Case #2: 3
#Case #3: 156
#Case #4: 287
def solve(line):
    count = 0
    hits = dict()
    (A, B) = line.split(' ')
    A = int(A)
    B = int(B)
    for x in range(A, B + 1):
        val = str(x)
        for i in range(len(val)):
            val = rotate(val)
            rot=int(val)
            if rot >= A and rot <= B and not x==rot  and (x,rot) not in hits:
                hits[(x,rot)] = 1
                hits[(rot,x)] = 1
                count += 1
    return count
    
    
            
if __name__ == '__main__':
    file = open('input.txt')
    i = 1
    lines = file.readlines()
    lines = lines[1:]
    for line in lines:
        line = line.strip('\n')
        output = solve(line)
        print "Case #" + str(i) + ": " + str(output)
        i += 1
    pass
