#usage: python c.py < input_file > output_file
import sys

def count_matches(line,line_offset,target,target_offset):
    if target_offset >= len(target): return 1;
    
    count = 0;
    for index in range(line_offset, len(line) - (len(target) - target_offset)):
        if line[index] == target[target_offset]:
            count = count + count_matches(line,index+1,target,target_offset+1)
    
    return count;

num_lines = int(sys.stdin.readline())
for case in range(1,num_lines+1):
    count = count_matches(sys.stdin.readline(),0,"welcome to code jam",0)
    answer = str(count)[-4:]
    while len(answer) < 4:
        answer = '0' + answer;
    print "Case #{0}: {1}".format(case,answer)
