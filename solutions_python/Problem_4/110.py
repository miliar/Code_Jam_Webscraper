import sys;

fNameBase = "A-large";

fIn = file(fNameBase + ".in");
fOut= file(fNameBase + ".out", "w");

num_tests = int(fIn.readline().strip());

current_test = 1;

while current_test <= num_tests:
    vec_len = int(fIn.readline().strip());
    vecX = fIn.readline().strip().split(' ');
    vecY = fIn.readline().strip().split(' ');

    i = 0;
    while (i < vec_len):
        vecX[i] = int(vecX[i]);
        vecY[i] = int(vecY[i]);
        i += 1;

    vecX.sort(lambda x, y: y - x); # large to small
    vecY.sort(); # small to large
    
    i = 0;
    total = 0;
    while (i < vec_len):
        total += vecX[i] * vecY[i];
        i += 1;

    fOut.write("Case #" + str(current_test) + ": " + str(total) + "\n");
    current_test += 1;


fIn.close();
fOut.close();
