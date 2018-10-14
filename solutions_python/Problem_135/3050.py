def run():
    T=int(input())
    test_case=1
    while test_case<=T :
        g1=int(input())
        for i in range(1,5):
            if i == g1:
                row1={int(i) for i in input().split(' ')}
            else:
                temp=input()
        g2=int(input())
        for i in range(1,5):
            if i == g2:
                row2={int(i) for i in input().split(' ')}
            else:
                temp=input()
        intersect=row1&row2
        if len(intersect) == 1:
            print("Case #%d: %d" % (test_case, intersect.pop()))
        elif len(intersect) > 1:
            print("Case #%d: Bad magician!" % (test_case))
        elif len(intersect) == 0:
            print("Case #%d: Volunteer cheated!" % (test_case))
        test_case+=1

if __name__ == "__main__":
    run()
