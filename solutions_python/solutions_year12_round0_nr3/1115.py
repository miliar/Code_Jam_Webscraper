def main():
    f = open('C-small-attempt1.in','r')
    f2 = open('output','w')
    list1, list2 =[], []
    l = 0
    f.readline()
    for line in f:
        line = line.strip()
        list1 = line.split()
        A = int(list1[0])
        B = int(list1[1])
        result = 0
        for x in range(A,B+1):
            y = str(x)
            j = len(str(x))
            list2 = []
            for i in range(0,j):
                z = y[j-i:] + y[0:j-i]
                if (int(z) <= B) & (int(z) >= A) & (int(z) > int(y)):
                    if z not in list2:
                        list2.append(z)
            result = result + len(list2)
        l += 1
        f2.write('Case #%d: '%l + str(result) +'\n')
    f.close()
    f2.close()

if __name__=="__main__":main()
