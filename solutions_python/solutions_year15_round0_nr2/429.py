from math import ceil, floor

# (current_size, target_size)
split_costs = {
    (2, 1): 1,

    (3, 1): 2, # 1 1 1
    (3, 2): 1, # 2 1

    (4, 1): 3, # 1 1 1 1
    (4, 2): 1, # 2 2
    (4, 3): 1, # 3 1

    (5, 1): 4, # 1 1 1 1 1
    (5, 2): 2, # 2 2 1
    (5, 3): 1, # 3 2
    (5, 4): 1, # 4 1

    (6, 1): 5, # 1 1 1 1 1 1
    (6, 2): 2, # 2 2 2
    (6, 3): 1, # 3 3
    (6, 4): 1, # 4 2
    (6, 5): 1, # 5 1

    (7, 1): 6, # 1 1 1 1 1 1 1
    (7, 2): 3, # 2 2 2 1
    (7, 3): 2, # 3 3 1
    (7, 4): 1, # 4 3
    (7, 5): 1, # 5 2
    (7, 6): 1, # 6 1

    (8, 1): 7, # 1 1 1 1 1 1 1 1
    (8, 2): 3, # 2 2 2 2
    (8, 3): 2, # 3 3 2
    (8, 4): 1, # 4 4
    (8, 5): 1, # 5 3
    (8, 6): 1, # 6 2
    (8, 7): 1, # 7 1

    (9, 1): 8, # 1 1 1 1 1 1 1 1 1
    (9, 2): 4, # 2 2 2 2 1
    (9, 3): 2, # 3 3 3
    (9, 4): 2, # 4 4 1
    (9, 5): 1, # 5 4
    (9, 6): 1, # 6 3
    (9, 7): 1, # 7 2
    (9, 8): 1, # 8 1
}

def compute_split_cost(size, target_size):
    if size <= target_size:
        return 0

    remainder = size % target_size
    if remainder > 0:
        return size // target_size
    else:
        return (size // target_size) - 1

def test_new_split():
    for size in range(2, 9 + 1):
        for target_size in range(1, size):
            if compute_split_cost(size, target_size) != split_costs[(size, target_size)]:
                print("Failed: {0}, {1}".format(size, target_size))
            else:
                print("Passed: {0}, {1}".format(size, target_size))
    exit()

if __name__ == "__main__":
    #test_new_split()
    with open("input.txt", "r") as input, open("output.txt", "w") as output:
        T = int(input.readline())
        for t in range(T):
            D = int(input.readline())
            tokens = input.readline().split(" ")

            pancake_counts = {}
            for i in range(len(tokens)):
                pancake_size = int(tokens[i])
                if pancake_size in pancake_counts:
                    pancake_counts[pancake_size] += 1
                else:
                    pancake_counts[pancake_size] = 1
            best_cost = max(pancake_counts.keys())
            for cutoff in range(1, max(pancake_counts.keys())):
                candidate_cost = 0
                for size, count in pancake_counts.items():
                    candidate_cost += (compute_split_cost(size, cutoff) * count)
                candidate_cost += cutoff
                best_cost = min(candidate_cost, best_cost)
            print("Case #{0}: {1}".format(t + 1, best_cost), file=output)