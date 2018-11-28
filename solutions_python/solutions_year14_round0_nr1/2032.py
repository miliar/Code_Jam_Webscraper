from sys import argv

if __name__=="__main__":
    nombre = open(argv[1],'r')
    n = int(nombre.readline())
    for i in range(n):
        r1 = int(nombre.readline())

        for j in range(1,r1):
            nombre.readline()
        l1=(nombre.readline()).strip()

        for j in range(r1,4):
            nombre.readline()

        r2 = int(nombre.readline())

        for j in range(1,r2):
            nombre.readline()
        l2=(nombre.readline()).strip()

        for j in range(r2,4):
            nombre.readline()

        fila1 = l1.split(" ")
        fila2 = l2.split(" ")

        sol = [x for x in fila1 for y in fila2 if x==y]

        length = len(sol)

        if length == 0:
            print("Case #{0}: Volunteer cheated!".format(i+1))
        elif length == 1:
            print("Case #{0}: {1}".format(i+1,sol[0]))
        else:
            print("Case #{0}: Bad magician!".format(i+1))