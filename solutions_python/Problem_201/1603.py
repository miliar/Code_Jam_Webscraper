import sys
import math

def main():
    total = int(sys.stdin.readline())
    for i in range(total):
        line = sys.stdin.readline()
        length, step = map(lambda x: int(x), line.rstrip().split(' '))
        result = find_space(length, step)
        print ('Case #{}: {} {}'.format(i + 1, result[0], result[1]))
        
    
def find_space(length, step):
    level = math.floor(math.log(step, 2))
    level_nodes = math.pow(2, level)
    
    # find total number of nodes in previous level
    prev_total_nodes = level_nodes - 1
    
    # compute target level
    level_sum = length - prev_total_nodes
    base = int(level_sum / level_nodes)
    remainder = int(level_sum % level_nodes)
    
    step -= prev_total_nodes
    node = (base + 1) if (step <= remainder) else (base)
    
    half = int(node / 2)
    if node == 1:
        return (0, 0)
    elif node % 2 == 0:
        return (half, half - 1)
    else:
        return (half, half)
    
if __name__ == '__main__':
  main()