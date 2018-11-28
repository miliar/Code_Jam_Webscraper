from heapq import heappush, heappop


def stalls(n, k):
    """
    n is the number of stalls
    k is the number of people
    """

    # Use a dictionary to index gap sets by size
    gap_counts = {n: 1}

    # Maintain a max heap (min heap of negated values) to allow quickly accessing the largest gap
    gap_heap = [-n]

    # Place people into gaps until none left, then return rs and ls for the last person
    while True:
        # Get the largest gap, and count of gaps of that size
        gap = -heappop(gap_heap)
        count = gap_counts.pop(gap, 0)

        # Calculate the new gaps created when placing a person into the middle stall of the gap
        ls = (gap-1)//2
        rs = gap//2

        # If the gap can fit the remaining people in line, then done
        if count >= k:
            return rs, ls  # rs >= ls by definition, no need to compare before returning
        else:
            # If there are still people in line, remove the people that have now entered stalls
            k -= count

            # Add the new gaps created to the heap and dictionary
            for new_gap in rs, ls:
                if new_gap in gap_counts:
                    gap_counts[new_gap] += count
                else:
                    heappush(gap_heap, -new_gap)
                    gap_counts[new_gap] = count


if __name__ == '__main__':
    input()
    case = 0
    while True:
        try:
            n, k = map(int, input().split(' '))
        except:
            break
        max_lsrs, min_lsrs = stalls(n, k)
        case += 1
        print('Case #{}: {} {}'.format(case, max_lsrs, min_lsrs))
