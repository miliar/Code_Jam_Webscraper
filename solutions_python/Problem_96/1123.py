def main():
    f = open('B-large.in','r')
    f2 = open('output','w')
    list1 =[]
    i = 0
    f.readline()
    for line in f:
        line = line.strip()
        list1 = line.split()
        N = int(list1[0])
        S = int(list1[1])
        p = int(list1[2])
        result = 0
        for x in list1[3:]:
            qou = int(x) // 3
            rem = int(x) % 3
            if qou >= p:
                result += 1
            elif int(x) >= p:
                if rem == 0:
                    if S > 0:
                        if (qou+1) >= p:
                            result += 1
                            S -= 1
                elif rem == 1:
                    if (qou + 1) >= p:
                        result += 1
                else:
                    if (qou + 1) >= p:
                        result += 1
                    else:
                        if S > 0:
                            if (qou+2) >= p:
                                result += 1
                                S -= 1
        i += 1
        f2.write('Case #%d: '%i + str(result) +'\n')
    f.close()
    f2.close()




if __name__=="__main__":main()
