import heapq, bisect, collections, math

def max_kits(recipe_num, all_packages):
    for i, packages in enumerate(all_packages):
        heapq.heapify(packages)

    res = 0
    while True:
        for i, r in enumerate(recipe_num):
            packages = all_packages[i]
            if not packages:
                return res
            if i == 0:
                serve_low, serve_up = math.ceil(packages[0]/1.1/r), math.floor(packages[0]/0.9/r)
                #print(serve)
                #print(packages[0], serve_low, serve_up)
            pack = heapq.heappop(packages)
            #print('lo, hi', math.ceil(pack/1.1/r), math.floor(pack/0.9/r))
            while math.floor(pack/0.9/r) < serve_low:
                if packages:
                    pack = heapq.heappop(packages)
                else:
                    return res
            if math.ceil(pack/r/1.1) > serve_low:
                if math.ceil(pack/1.1/r) > serve_up:
                    #print('push back')
                    heapq.heappush(packages, pack)
                    break

        else:
            res += 1
        #print(res)

def main():
    with open('/Users/tengg/Downloads/B-large.in') as f:
        t = int(f.readline())
        for i in range(1, t+1):
            n, p = map(int, f.readline().split(' '))
            recipe_num = list(map(int, f.readline().split(' ')))
            all_packages = []
            for _ in range(n):
                all_packages.append(list(map(int, f.readline().split(' '))))
            #print(recipe_num, all_packages)
            print(f"Case #{i}: {max_kits(recipe_num, all_packages)}")

if __name__ == '__main__':
    #print(max_kits([50,100], [[450, 449],[1100,1101]]))
    main()
