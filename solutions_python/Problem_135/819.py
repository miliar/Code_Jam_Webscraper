def solve(r1, a1, r2, a2):
    l1, l2 = a1[r1 - 1], a2[r2 - 1]
    l3 = list(set(l1) & set(l2))
    if l3 == []:
        return "Volunteer cheated!"
    elif len(l3) > 1:
        return "Bad magician!"
    else:
        return str(l3[0])

def main():
    t = int(raw_input())
    for i in range(1, t+1):
        r1 = int(raw_input())
        a1 = [[int(x) for x in raw_input().split()] for j in range(4)]
        r2 = int(raw_input())
        a2 = [[int(x) for x in raw_input().split()] for j in range(4)]
        print("Case #{}: {}".format(i, solve(r1, a1, r2, a2)))

if __name__ == "__main__":
    main()
