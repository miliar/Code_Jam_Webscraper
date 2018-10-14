if __name__ == "__main__":
    fin = open("a.in", 'r')
    fout = open("a.out", 'wb')
    
    T = int(fin.readline())
    #import ipdb; ipdb.set_trace()
    for i in range(1, T+1):
        input = fin.readline().split()
        smax = int(input[0])
        audi = input[1]
        
        need = 0
        cul = 0
        
        for j in range(smax+1):
            if cul >= j:
                cul += int(audi[j])
            elif int(audi[j]) > 0:
                need += j - cul
                cul += need + int(audi[j])
        fout.write("Case #%d: %d\n" %(i, need))
    fin.close()
    fout.close()
