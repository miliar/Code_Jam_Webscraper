def is_in_bounds(req_m, pack_m):
    if req_mp * 90 <= pack_m * 100 <= req_m * 110:
        return True
    return False

def get_bounds(req_m, pack_m):
    # we need to find the lowest and highest number
    # of servings we could service with this pack
    def binary_search(left, right, req, pack):
        mid = (left + right) / 2
        if right - left <= 1:
            return mid
        if mid * req < pack:
            return binary_search(mid, right, req, pack)
        else:
            return binary_search(left, mid, req, pack)
    right = binary_search(0, 10 ** 7, req_m * 90, pack_m * 100) + 1
    left = max(binary_search(0, 10 ** 7, req_m * 110, pack_m * 100) - 1, 0)
#    print left, right
    while pack_m * 100 > left * req_m * 110:
        left += 1
    while pack_m * 100 < right * req_m * 90:
        right -= 1
    if left == 0 and right == 0 or left > right:
        return None
    return (left, right)

def get_bounds_intersect(b1, b2):
    l1, r1 = b1
    l2, r2 = b2
    if l1 > r2 or l2 > r1:
        return None
    return (max(l1, l2), min(r1, r2))

def solve(n, p, reqs, packages):
    # convert packages to # of servings
    # by ingredient
    servings = []
    nodes = {}
    visited = set()
    for item in range(n):
        package_servings = []
        for pi, pack in enumerate(packages[item]):
            package_servings.append(get_bounds(reqs[item], pack))
            nodes[(item, pi)] = True
        servings.append(package_servings)
#    print servings

    # try to make it from one end to the other
    def find_paths():
        def recur(ing, curr_serv, curr_path):
#            print visited
#            print ing, curr_serv, curr_path
            if ing == len(servings) - 1:
                return curr_path
            for pi, pack in enumerate(servings[ing + 1]):
                if not pack:
                    continue
#                print curr_serv, pack
                inter = get_bounds_intersect(curr_serv, pack)
                if inter:
                    tup = (ing + 1, pi)
                    if tup in visited:
                        continue
                    visited.add(tup)
#                    print 'tup', tup
                    curr_path.append(tup)
                    path = recur(ing + 1, pack, curr_path)
                    if len(path) > 0:
                        return path
                    visited.remove(tup)
                    curr_path.pop()
            return []
        count = 0
        for xi, serv in enumerate(servings[0]):
            if not serv:
                continue
            path = recur(0, serv, [(0, xi)])
            if len(path) == len(servings):
                count += 1
            for x in path:
                visited.add(x)
        return count
    return find_paths()

#print get_bounds(5, 1)
#print get_bounds(5, 50)
#print get_bounds(5, 23553)
#print get_bounds_intersect((1, 3), (5, 6))
#print get_bounds_intersect((5, 6), (1, 3))
#print get_bounds(500, 1500)

t = input()
for i in range(1, t + 1):
    n, p = map(int, raw_input().strip().split())
    reqs = map(int, raw_input().strip().split())
    packages = []
    for _ in range(n):
        packages.append(map(int, raw_input().strip().split()))
        packages[-1].sort()
    print 'Case #{}: {}'.format(i, solve(n, p, reqs, packages))

