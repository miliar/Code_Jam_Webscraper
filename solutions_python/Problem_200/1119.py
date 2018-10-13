#Tidy Numbers - Problem B
#Google Code Jam - Qualification round 8/4/2017
#Theo Vickery

def main():
    t = int(input())
    n_list = []
    
    for i in range(t):
        n_list.append([int(i) for i in list(input())])
        
    for c in range(1, t + 1):
        n = n_list[c-1]
        tidy = [0] * len(n)

        previous = 0
        step = 0
        i = 0
        carry = False
        while i < len(n):
            if n[i] >= previous:
                tidy[i] = n[i]
                if n[i] > previous:
                    step = i
                previous = tidy[i]
                i += 1
            else:
                tidy[step] = tidy[step] - 1
                for p in range(step + 1, len(tidy)):
                    tidy[p] = 9
                break






        
        print("Case #{}: {}".format(c, int("".join([str(e) for e in tidy]))))

main()
