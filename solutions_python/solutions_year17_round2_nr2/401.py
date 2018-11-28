import heapq, collections

def place_unicorns(unicorns):
    u = ['R','O','Y','G','B','V']
    n, *uc = unicorns
    most_colored = max(uc)
    if most_colored > n/2:
        return "IMPOSSIBLE"
    uc = [(n, u[i]) for i, n in enumerate(uc) if n]
    uc.sort()
    stable = [uc[-1][1]]*uc[-1][0]
    uc.pop()
    ip = 1
    while uc:
        breed_num, color = uc.pop()
        while breed_num:
            stable.insert(ip, color)
            ip = (ip+2) % len(stable)
            breed_num -= 1
    return ''.join(stable)

def main():
    input_file = '/Users/tengg/Downloads/B-small-attempt0.in'
    output_file = input_file+'.out'
    with open(input_file) as f, open(output_file, 'w') as o:
        t = int(f.readline())
        for i in range(1, t+1):
            unicorns = map(int, f.readline().strip().split(' '))
            print(f'Case #{i}:', place_unicorns(unicorns), file=o)

if __name__ == '__main__':
    main()
    #print(place_unicorns([14,6,0,4,0,4,0]))