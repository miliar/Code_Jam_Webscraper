import math
inFile = open("A-small-attempt1.in");
outFile = open("output.txt", 'w');

T = inFile.readline();
for count in range(1, int(T)+1):
    temp = inFile.readline().split(" ");
    r = int(temp[0]);
    v = int(temp[1]);
    result = 1 + 0.25 * ( math.sqrt(4*r**2 - 4*r + 8*v + 1) - 2*r - 3);
    print result
    outFile.write('Case #' + str(count) + ': ' + str(int(math.floor(result))) + '\n');
outFile.close();
inFile.close();
