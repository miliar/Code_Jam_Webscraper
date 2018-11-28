"ProblemC Code"

import heapq # import heapq module


def main():
    t = input()
    for i in range(1,t+1):
        n,k = [int(s) for s in raw_input().split(" ")]
        
        consequtive_open = (1,n)
        gap = n
        heap = []
        value = (-gap, 1, n) # negative gap means a large gap has better priority
        heapq.heappush(heap, value)

        for j in range(k):
            gap,left_free,right_free = heapq.heappop(heap)
            new_stall = (right_free - left_free)//2 + left_free # person j goes to this stall
            LS = new_stall - left_free
            RS = right_free - new_stall

            # now add the two new consequtive free stalls to the heap
            left_gap = (new_stall-1) - left_free - 1
            right_gap = right_free - (new_stall+1) - 1
            left_value = (-left_gap, left_free, new_stall-1)
            right_value = (-right_gap, new_stall+1, right_free)
            heapq.heappush(heap, left_value)
            heapq.heappush(heap, right_value)

        print("Case #{}: {} {}".format(i,max(LS,RS),min(LS,RS)))


main()