from collections import deque
import time

start = time.time()
def flip(pancakes, loc, K):
    flipped = []
    for n,pancake in enumerate(pancakes):
        if loc <= n < loc+K:
            flipped.append(str(1-int(pancake)))
        else:
            flipped.append(pancake)
    return flipped

def heur_cmp(elem):
    return elem[0].count("0")

f = open("C:\Python34\cjq1_sol.txt","w")
f.close()

with open("C:\Python34\cjq1.txt","r") as f:
    for i,line in enumerate(f.readlines()):
        if i>0:
            IMPOSSIBLE = False
            pancakes = line.split(" ")[0]
            pancakes = pancakes.replace("+", "1")
            pancakes = pancakes.replace("-", "0")
            K = int(line.split(" ")[1])

            depth = 0
            tried = set()
            fringe = deque()
            fringe.appendleft([list(pancakes),depth])
            
            # Pop & Check Node
            cur = fringe.popleft()
            if K%2 == 0 and cur[0].count("1")%2 != len(pancakes)%2:
               IMPOSSIBLE = True
            
            while not IMPOSSIBLE and cur[0].count("1") != len(pancakes):
                # Expand Node
                for loc in range(len(cur[0])-K+1):
                    flippy = flip(cur[0], loc, K)
                    if depth == 0:
                        fringe.append([flippy, depth])
                    elif tuple(flippy) not in tried:
                        fringe.append([flippy, depth])
                    
                # Sort
                fringe = deque(sorted(fringe, key=heur_cmp))
                try:
                    cur = fringe.popleft()
                except:
                    IMPOSSIBLE = True
                    break
                tried.add(tuple(cur[0]))
                depth = cur[1] + 1
            answer = depth

            with open("C:\Python34\cjq1_sol.txt","a") as f:
                print("Case #{}: {}".format(i, answer if not IMPOSSIBLE else "IMPOSSIBLE"))
                f.write("Case #{}: {}\n".format(i, answer if not IMPOSSIBLE else "IMPOSSIBLE"))
end = time.time()
print("Time: {}".format(end-start))
