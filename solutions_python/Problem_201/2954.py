import math

input_file = "input.txt"

def find_values_for_partition(p):
    if p == 1:
        return 0, 0
    max_stalls = (p)/2
    min_stalls = p - max_stalls - 1
    return max_stalls, min_stalls
    

def find_max_and_min(n, k):
    partition_list = [n]
    min_stalls = 0
    max_stalls = 0
    for i in range(k-1):
        current_partition = partition_list.pop(0)
        max_stalls, min_stalls = find_values_for_partition(current_partition)
        partition_list.append(max_stalls)
        partition_list.append(min_stalls)
        partition_list.sort(reverse = True)

    return find_values_for_partition(partition_list.pop(0))

def main():
    with open(input_file, 'r') as f:
        T = int(f.readline())
        for i in range(T):
            N, K = map(int, f.readline().strip().split(" "))

            max_stalls, min_stalls = find_max_and_min(N, K)
            print "Case #" + str(i + 1) + ": " + str(max_stalls) + " " + str(min_stalls)

main() 


