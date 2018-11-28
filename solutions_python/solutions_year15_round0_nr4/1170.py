if __name__ == "__main__":
    fin = open("d.in", 'r')
    fout = open("d.out", 'wb')
    
    T = int(fin.readline())
    for i in range(1, T+1):
        items = fin.readline().split()
        X = int(items[0])
        R = int(items[1])
        C = int(items[2])
        
        if X == 1:
            fout.write("Case #%d: %s\n" %(i, "GABRIEL"))
        elif X == 2:
            if R * C % 2 == 0:
                fout.write("Case #%d: %s\n" %(i, "GABRIEL"))
            else:
                fout.write("Case #%d: %s\n" %(i, "RICHARD"))
        elif X == 3:
            if R * C % 3 != 0 or R * C == 3:
                fout.write("Case #%d: %s\n" %(i, "RICHARD"))
            else:
                fout.write("Case #%d: %s\n" %(i, "GABRIEL"))
        elif X == 4:
            if R * C == 4 or R * C == 8 or R * C % 4 != 0:
                fout.write("Case #%d: %s\n" %(i, "RICHARD"))
            else:
                fout.write("Case #%d: %s\n" %(i, "GABRIEL"))
    fin.close()
    fout.close()
