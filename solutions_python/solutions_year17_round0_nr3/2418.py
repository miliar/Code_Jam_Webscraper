def main():
    output_string = 'Case #{}: {} {}'
    num_cases = int(input())
    first_attempt(num_cases, output_string)

def first_attempt(num_cases, output_string):
    for case in range(1, num_cases + 1):
        n, k = input().split()
        n, k = int(n), int(k)
        stalls = [True] + [False] * n + [True]
        for _ in range(k):
            distances = get_distances(stalls)
            def min_sort_key(x):
                return min(x[1])
            def max_sort_key(x):
                return max(x[1])
            sorted_distances = sorted(distances.items(), key=min_sort_key,
                                      reverse=True)
            possibles = get_possibles(sorted_distances, min)
            possibles = sorted(possibles, key=max_sort_key, reverse=True)
            possibles = get_possibles(possibles, max)

            stalls[possibles[0][0]] = True
        left_distance, right_distance = possibles[-1][1]
        print(output_string.format(case, left_distance, right_distance))

def get_possibles(sequence, sort_function):
    distance = None
    possibles = []
    for item in sequence:
        position, (left_distance, right_distance) = item
        if (distance is None
            or distance == sort_function(left_distance, right_distance)):
            possibles.append(item)
            distance = sort_function(left_distance, right_distance)
            continue
        else:
            # no longer maximal
            break
    return possibles

def get_distances(stalls):
    distances = {}
    j = 0
    for i, stall in enumerate(stalls):
        if stall:
            j = i - 1
            while j > 0 and not stalls[j]:
                distances[j][1] = i - j - 1
                j -= 1
            j = 0
            continue
        else:
            distances[i] = [j, None]
            j += 1
    return distances

if __name__ == '__main__':
    main()
