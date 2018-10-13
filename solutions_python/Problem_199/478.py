T = int(input())
combos = {}
import sys
sys.setrecursionlimit(5000)
def flipping(origFaces, s):
    minFlips = 0
    faces = list(origFaces)
    #print(faces)
    if tuple([tuple(origFaces),s]) in combos:
        minFlips = combos[tuple([tuple(origFaces),s])]
    elif faces == list("+"*s):
        minFlips = 0
    elif faces == list("-"*s):
        minFlips = 1
    else:
        if len(faces) >= s:
            if faces[0] == "+":
                curFlips = flipping(faces[1:], s)
                if curFlips != -1:
                    minFlips = curFlips
                else:
                    minFlips = -1
            else:
                for y in range(s):
                    if faces[y] == "+":
                        faces[y] = "-"
                    else:
                        faces[y] = "+"
                curFlips = flipping(faces[1:], s)
                if curFlips != -1:
                    minFlips = curFlips + 1
                else:
                    minFlips = -1
        else:
            minFlips = -1
    combos[tuple([tuple(origFaces),s])] = minFlips
    return minFlips
for x in range(T):
    pancakes, s = list(raw_input().split(" "))
    pancakes = list(pancakes)
    s = int(s)
    theFlips = str(flipping(pancakes, s))
    if theFlips != "-1":
        print("Case #"+str(x+1)+": "+theFlips)
    else:
        print("Case #"+str(x+1)+": IMPOSSIBLE")
#print(combos)
