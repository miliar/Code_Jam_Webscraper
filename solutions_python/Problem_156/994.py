def partition(pancake):
    for i in range(2, pancake//2 + 1):
        yield pancake - i, i

def infinite_house_pancakes(pancakes):
    max_pancakes = max(pancakes)
    count_max_pancakes = pancakes.count(max_pancakes)
    if count_max_pancakes >= max_pancakes:
        return max_pancakes
    result = max_pancakes
    pancakes = [x for x in pancakes if x != max_pancakes]
    for a, b in partition(max_pancakes):
        new_pancakes = pancakes[:]
        new_pancakes.extend([a, b] * count_max_pancakes)
        tmp = infinite_house_pancakes(new_pancakes)
        if tmp < result:
            result = tmp
    result += count_max_pancakes
    if result >= max_pancakes:
        return max_pancakes
    return result

def main():
    T = int(raw_input())
    for t_i in range(T):
        D = int(raw_input())
        pancakes = map(int, raw_input().split(' '))

        print ('Case #{t_i}: {answer}'.format(t_i=t_i+1, answer=infinite_house_pancakes(pancakes)))

if __name__ == '__main__':
    main()
