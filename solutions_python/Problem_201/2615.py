def get_maximum(l, f):
    items = []
    last = -1

    for item in l:
        if item is not None:
            test = f(item)

            if test > last:
                #New maximum according to comparison function
                last = test
                items = [item]
            elif test == last:
                items.append(item)
    
    return items

def find_largest(stalls):
    """
    Scan the array of tuples the largest min. 
    If there are multiple, scan for largest max. Then return the leftmost.
    """
    maximum_min = get_maximum(stalls, min)

    if len(maximum_min) > 1:
        return get_maximum(maximum_min, max)[0]
    else:
        return maximum_min[0]

if __name__ == "__main__":
    cases = int(input())

    for case in range(1, cases + 1):
        n, k = map(int, input().split(" ", 1))

        #Build our toilets
        stalls = [(x, n-x-1) for x in range(0, n)]

        while k > 0:
            largest = find_largest(stalls)
            largest_index = stalls.index(largest)

            #Every R to the left of the index should be subtracted by R + 1
            for i in range(largest_index - 1, -1, -1):
                t = stalls[i]

                #We'll use None to indicate when we need to stop looping
                #This effectively partitions our list
                if t is None:
                    break

                stalls[i] = (t[0], t[1] - (largest[1] + 1))
            
            #Every L to the right of the index should be subtracted by L + 1
            for i in range(largest_index + 1, len(stalls)):
                t = stalls[i]

                if t is None:
                    break

                stalls[i] = (t[0] - (largest[0] + 1), t[1])

            stalls[largest_index] = None

            if k == 1:
                print("Case #{}: {} {}".format(case, max(largest), min(largest)))

            k = k - 1;
