from collections import deque
b = 1452


def rot_num(num):
    tup = []
    for i in range(1, len(str(num))):
        chain = str(num)
        rotate_chain = deque(chain)
        rotate_chain.rotate(-i)
        c = int(''.join(map(str, rotate_chain)))
        tup.append(c)        
    return tup

f = open('C:/Users/SACHIN/Desktop/C-small-attempt0.in', 'r')
g = open('C:/Users/SACHIN/Desktop/ouput.txt', 'w')
inp = f.readlines()

for i in range(1, len(inp)):
    line = inp[i].split()
    A = int(line[0])
    B = int(line[1])
    count = 0
    for j in range (A, B + 1):
        tup = rot_num(j)
        m = j
        for k in range(len(tup)):            
            if (tup[k] >= A and tup[k] <= B and tup[k] < m):
                count += 1
    output_str = "Case #" + str(i) + ": " + str (count) + "\n"
    g.write(output_str)       
