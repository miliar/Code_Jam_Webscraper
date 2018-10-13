def common(a,b):
    result = []
    for x in a:
        if x in b:
            result.append(x)
    return result

def main():
    for i in range(1,int(raw_input())+1):
        row1 = int(raw_input())
        rows1 = [[],[],[],[]]
        for x in raw_input().split(" "):
            rows1[0].append(int(x))
        for x in raw_input().split(" "):
            rows1[1].append(int(x))
        for x in raw_input().split(" "):
            rows1[2].append(int(x))
        for x in raw_input().split(" "):
            rows1[3].append(int(x))

        row2 = int(raw_input())
        rows2 = [[],[],[],[]]
        for x in raw_input().split(" "):
            rows2[0].append(int(x))
        for x in raw_input().split(" "):
            rows2[1].append(int(x))
        for x in raw_input().split(" "):
            rows2[2].append(int(x))
        for x in raw_input().split(" "):
            rows2[3].append(int(x))

        ans = common(rows1[row1-1],rows2[row2-1])

        output = ""
        if len(ans) == 0:
            output = "Volunteer cheated!"
        elif len(ans) == 1:
            output = str(ans[0])
        else:
            output = "Bad magician!"
        print "Case #"+str(i)+": "+output

if __name__ == '__main__':
    main()