#Pancake Flipping

def to_list(string):
    l = []
    for i in string:
        if i == "+":
            l.append(True)
        elif i == "-":
            l.append(False)
    return l

def main():
    t = int(input())
    cases = []
    for c in range(t):
        temp = input()
        pancakes = []
        cases.append((to_list(temp.split()[0]), int(temp.split()[1])))
    for c in range(len(cases)):
        case = cases[c]
        pancakes, k = case
        count = 0
        
        for p in range(len(pancakes) - k + 1):
            if not pancakes[p]:
                count += 1
                for i in range(p, p+k):
                    pancakes[i] = not pancakes[i]
                    
        all_flipped = True
        for p in range(len(pancakes) - k + 1, len(pancakes)):
            if not pancakes[p]:
                all_flipped = False
                break

        if not all_flipped:
            count = "IMPOSSIBLE"

        print("Case #{0}: {1}".format(c+1, count))
        
main()
