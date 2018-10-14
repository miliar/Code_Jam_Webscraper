if __name__ == '__main__':
    def getSet(index):
        ls = 0
        rs = 0
        index -= 1
        if index > 0:
            ls = int(index/2)
            rs = index - ls
        return [ls, rs]
    testC = int(input())
    inputN=[]
    for i in range(testC):
        inputN.append(str(input()))
    for i,v in enumerate(inputN):
        N = int(v.split(' ')[0])
        K = int(v.split(' ')[1])
        a_n = []
        for i3 in range(N):
            a_n.append(0)

        t1 = [N]
        LS = 0
        RS = 0
        while K > 0:
            t1.sort()
            pos = t1.pop(-1)
            if pos % 2 == 0:
                m = int(pos / 2)
            else:
                m = int(pos+1 / 2)
            _set = getSet(pos)
            LS = _set[0]
            RS = _set[1]
            t1.append(_set[0])
            t1.append(_set[1])
            K -= 1
            pass
        print("Case #{0}: {1} {2}".format(i + 1, RS, LS))
        pass
