from sys import stdin

def readline():
    return stdin.readline().split()

# Read # cases    
[T] = [int(i) for i in readline()]

for case in range(T):    
    # Input
    [S_max, shyness] = readline()
    # Pre-processing
    S_max = int(S_max)    
    shyness = [int(digit) for digit in shyness]
    
    # Process
    sum = shyness[0]
    frds_needed = 0
    for shyness_level in range(1, len(shyness)):        
        if sum < shyness_level:
            frds_needed += shyness_level - sum
            sum += shyness_level - sum
        sum += shyness[shyness_level]
            
    print("Case #%d: %d" % (case + 1, frds_needed))
