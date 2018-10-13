def load_data():
    with open("a-small.txt") as f:
        with open("answer.txt", 'w') as ans:
            T = int(f.readline().split()[0])
            for case in range(T):
                a1 = int(f.readline().split()[0])
                t1 = []
                for row in range(4):
                    t1.append([int(i) for i in f.readline().split()])

                a2 = int(f.readline().split()[0])
                t2 = []
                for row in range(4):
                    t2.append([int(i) for i in f.readline().split()])

                ans.write("Case #{}: {}\n".format(case + 1, solve_one(a1, t1, a2, t2)))


def solve_one(a1, t1, a2, t2):
    s = set(t1[a1 - 1]).intersection(set(t2[a2 - 1]))
    n = len(s)
    if n == 0:
        return "Volunteer cheated!"
    elif n == 1:
        return "{}".format(s.pop())
    elif n > 1:
        return "Bad magician!"
    

def main():
    load_data()

if __name__ == "__main__":
    main()
