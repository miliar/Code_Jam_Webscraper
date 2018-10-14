__author__ = 'Adela'


def main():
    t = int(input())

    for i in range(t):
        ans1 = int(input())
        row1 = []
        for r in range(4):
            if ans1 == (r + 1):
                row1 = [int(k) for k in input().split()]
            else:
                input()

        ans2 = int(input())
        row2 = []
        for r in range(4):
            if ans2 == (r + 1):
                row2 = [int(k) for k in input().split()]
            else:
                input()

        common = []
        for r in row1:
            if r in row2:
                common.append(r)

        print("Case #", i + 1, ":", sep='', end=' ')
        if len(common) == 0:
            print("Volunteer cheated!")
        elif len(common) > 1:
            print("Bad magician!")
        else:
            print(common[0])


if __name__ == "__main__":
    main()
