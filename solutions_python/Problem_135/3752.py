def main():
    f = open('A-small-attempt0.in', 'r')
    f2 = open('a.out', 'w')
    t = int(f.readline())
    c = 1
    while(t > 0):
        r1 = int(f.readline()) - 1
        a = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        for i in range(4):
            s = f.readline()
            arr = s.split()
            a[i][0] = int(arr[0])
            a[i][1] = int(arr[1])
            a[i][2] = int(arr[2])
            a[i][3] = int(arr[3])

        r2 = int(f.readline()) - 1
        b = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        for i in range(4):
            s = f.readline()
            arr = s.split()
            b[i][0] = int(arr[0])
            b[i][1] = int(arr[1])
            b[i][2] = int(arr[2])
            b[i][3] = int(arr[3])
        count = 0
        for i in range(4):
            if a[r1][i] in b[r2]:
                ans = a[r1][i]
                count += 1

        if(count == 1):
            f2.write('Case #'+str(c)+': '+str(ans)+'\n')
        elif(count == 0):
            f2.write('Case #'+str(c)+': Volunteer cheated!\n')
        elif(count > 0):
            f2.write('Case #'+str(c)+': Bad magician!\n')
        c += 1
        t -= 1
    f2.close()
    f.close()
if __name__ == '__main__':
    main()
