__author__ = 'duo 11'
File = open("D-small-attempt5.in","r")
#File = open("C-small-attempt1.in","r")
Out = open("D-output.out","w")
T = int(File.readline().replace("\n",''))

Table = [[[1,1], []],
         [[2,1], [2]],
         [[2,2], [2]],
         [[3,1], []],
         [[3,2], [2,3]],
         [[3,3], [3]],
         [[4,1], [2]],
         [[4,2], [2]],
         [[4,3], [2,3,4]],
         [[4,4], [2,4]]]

for z in xrange(T):
    X, R, C = File.readline().replace("\n",'').split(' ')
    X, R, C = int(X), int(R), int(C)

    if X == 1:
        Out.write("Case #" + str(z+1) + ": " + "GABRIEL" + "\n")
    else:
        L = [max(R,C),min(R,C)]
        print L
        for T in Table:
            if T[0] == L:
                if X in T[1]: Out.write("Case #" + str(z+1) + ": " + "GABRIEL" + "\n")
                else: Out.write("Case #" + str(z+1) + ": " + "RICHARD" + "\n")
Out.close()