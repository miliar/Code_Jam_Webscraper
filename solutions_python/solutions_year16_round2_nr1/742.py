def digits():
    f=open("input2.in","r")
    file = open("digits.txt", "w")
    t=f.readline()
    t=int(t)
    for k in range(t):
        s=f.readline()
        r=[]
        s=list(s)
        while "Z" in s:
            s.remove('Z')
            s.remove('E')
            s.remove('R')
            s.remove('O')
            r=r+[0]
        while "X" in s:
            s.remove('S')
            s.remove('I')
            s.remove('X')
            r=r+[6]
        while "G" in s:
            s.remove('E')
            s.remove('I')
            s.remove('G')
            s.remove('H')
            s.remove('T')
            r=r+[8]
        while "S" in s:
            s.remove('S')
            s.remove('E')
            s.remove('V')
            s.remove('E')
            s.remove('N')
            r=r+[7]
        while "V" in s:
            s.remove('F')
            s.remove('I')
            s.remove('V')
            s.remove('E')
            r=r+[5]
        while "I" in s:
            s.remove('N')
            s.remove('I')
            s.remove('N')
            s.remove('E')
            r=r+[9]
        while "N" in s:
            s.remove('O')
            s.remove('N')
            s.remove('E')
            r=r+[1]
        while "W" in s:
            s.remove('T')
            s.remove('W')
            s.remove('O')
            r=r+[2]
        while "T" in s:
            s.remove('T')
            s.remove('H')
            s.remove('R')
            s.remove('E')
            s.remove('E')
            r=r+[3]
        while "F" in s:
            s.remove('F')
            s.remove('O')
            s.remove('U')
            s.remove('R')
            r=r+[4]
        r.sort()
        u=""
        for i in r:
            u=u+str(i)
        file.write("Case #")
        file.write(str(k+1))
        file.write(": ")
        file.write(u)
        file.write("\n")