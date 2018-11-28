import sys

def parse(line):
    pancakes = []
    i = 0
    while(i < len(line) and (line[i] == '+' or line[i] == '-')):
        if(line[i] == '+'):
            pancakes.append(1)
        else:
            pancakes.append(0)
        i+=1
    k = int(line[i:])
    return [k, pancakes]


def flip(pancakes, spot, k):
    for i in range(k):
        pancakes[spot+i] = (pancakes[spot+i] + 1) % 2

def flip_all_pancakes(k, pancakes):
    num_flips = 0
    for i in range(len(pancakes)-(k-1)):
        if pancakes[i] == 0:
            flip(pancakes,i,k)
            num_flips +=1
    return num_flips

def get_answer(k, pancakes):
    ans = flip_all_pancakes(k, pancakes)
    for i in pancakes:
        if i == 0:
            return 'IMPOSSIBLE'
    return str(ans)
    
#returns string    
def solution(line):
    to_pass = parse(line)
    return get_answer(to_pass[0],to_pass[1])
    
in_file = sys.argv[1]
in_stream = open(in_file)
lines = in_stream.readlines()

for i in range(1,len(lines)):
    print 'Case #%d: '%i +solution(lines[i])
