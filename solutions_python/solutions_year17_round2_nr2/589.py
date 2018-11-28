import sys
import numpy as np

input_file = "B-small-attempt2.in"
output_file = "B-small-attempt2.out"

# key = previous
possible_next = {0: [2, 3, 4],
                 1: [4],
                 2: [0, 4, 5],
                 3: [0],
                 4: [0, 1, 2],
                 5: [2]}

def result_to_candidate(result):
    if result == "R":
        return 0
    elif result == "Y":
        return 1
    elif result == "B":
        return 2
    return -1

def candidate_to_string(cand):
    result = ""
    if cand == 0:
        result = "R"
    elif cand == 1:
        result = "Y"
    elif cand == 2:
        result = "B"
    return result

def solve(tt):
    n, r, o, y, g, b, v = [int(j) for j in input().split(" ")]
    ryb = np.zeros(3)
    result = ""
    previous = -1
    ryb[0] += r + o + v
    ryb[1] += o + y + g
    ryb[2] += g + b + v
    for i in range(n):
        sort_indices = np.argsort(-ryb)
        for j in range(3):
            candidate = sort_indices[j]
            if len(result) != 0:
                start_result = result_to_candidate(result[0])
                if ryb[start_result] == ryb[candidate]:
                    if start_result != previous:
                        candidate = start_result
            if ryb[candidate] == 0:
                return "IMPOSSIBLE"
            if previous == candidate:
                continue
            else:
                result += candidate_to_string(candidate)
                ryb[candidate] -= 1
                previous = candidate
                break
    if result[0] == result[-1]:
        return "IMPOSSIBLE"
    return result

def main():
    t = int(input())
    for tt in range(1, t + 1):
        result = solve(tt)
        print("Case #{}: {}".format(tt, result))

if __name__ == "__main__":
    sys.stdin = open(input_file)
    sys.stdout = open(output_file, 'w+')
    main()























