import sys


def max_min(num):
    if num % 2:
        ans = num / 2
        return(ans, ans)
    else:
        ans = num / 2
        return (ans, ans - 1)
    
    
def solve(line):
    N = int(line[0])
    K = int(line[1])
    count = 1
    if K == 1:
        return max_min(N)
    start = max_min(N)
    big = max(start)
    num_big = 1
    small = min(start)
    num_small = 1
    if K == 1:
        return max_min(N)
    while True:
        # start with big
        count += num_big
        if count >= K:
            return max_min(big)
        count += num_small
        if count >= K:
            return max_min(small)

        new_big_nums = max_min(big)
        big = max(new_big_nums)
        new_small_nums = max_min(small)
        small = min(new_small_nums)

        new_big_num = 0
        new_small_num = 0
        if new_big_nums[0] == new_big_nums[1]:
            new_big_num += 2 * num_big
        else:
            new_big_num += num_big
            new_small_num  += num_big

        if small == big:
            new_big_num += 2 * num_small
        else:
            if new_small_nums[0] == new_small_nums[1]:
                new_small_num += 2 * num_small
            else:
                new_small_num += num_small
                new_big_num += num_small

        num_big = new_big_num
        num_small = new_small_num
    
        
        
        
        
    

#in_file = open("input.txt", 'r')
#in_file = open("C-small-1-attempt0.in", 'r')
#in_file = open("C-small-2-attempt0.in", 'r')
in_file = open("C-large.in", 'r')

out_file = open("output.txt", 'w')
    
size = int(in_file.readline())

case = 1

while case <= size:
    line = in_file.readline().strip().split()

    sol = solve(line)

    answer = "Case #" + str(case) + ": " + str(sol[0]) + " " + str(sol[1]) + "\n" 
    out_file.write(answer)
    case += 1

in_file.close()
out_file.close()

