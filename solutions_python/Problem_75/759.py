#! /usr/bin/env python3.0

def add(stack, new_elem, combis, oppos):
    if (combine(stack, new_elem, combis)):
        return
    elif (clear(stack, new_elem, oppos)):
        return
    else:
        stack += [new_elem]

def combine(stack, new_elem, combinations):
    if (stack == []):
        return False
    
    elif ((stack[-1] + new_elem) in combinations.keys()):
        stack += [combinations[stack.pop(-1) + new_elem]]
        return True
    
    # may not occure
    elif ((new_elem + stack[-1]) in combinations.keys()):
        stack += [combinations[new_elem + stack.pop(-1)]]
        return True

def clear(stack, new_elem, oppos):
    if (not stack == []):
        for elem in stack:
            if ((elem+new_elem in oppos) or (new_elem+elem in oppos)):
                while(len(stack) > 0):
                    stack.pop()
                return True
    return False


fic = input()

f = open(fic, "r")
lines = [li.replace("\n", "") for li in f.readlines()][1:]
f.close()


f = open("output.txt", "w")

for i in range(len(lines)):
    elems = lines[i].split(" ")
    
    combs = {e[:2]:e[2] for e in elems[1:int(elems[0])+1]}
    
    opposites = elems[int(elems[0])+2:int(elems[int(elems[0])+1])+int(elems[0])+2]
    ingredients = elems[-1]
    
    stack = []
    
    for ingred in ingredients:
        add(stack, ingred, combs, opposites)
    
    out = "Case #"+str(i+1)+": ["+", ".join(stack)+"]"
    print(out)
    f.write(out+"\n")

f.close()




















