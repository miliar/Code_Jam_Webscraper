def ispalin(N):
    temp = N;
    reverseN = 0;
    while temp != 0:
        reverseN = reverseN*10 + temp%10;
        temp /= 10;

    return N == reverseN

fo = open("C-small-attempt0.in","r")
fout = open("smalloutput.txt","wb")

T = int(fo.readline());     # no. of test cases

for case in range(T):
    limitstring = fo.readline();
    limits = limitstring[0:len(limitstring)-1].split(" ");
    A = int(limits[0]);
    B = int(limits[1]);

    low = int(A**0.5);
    if low**2 < A:
        low += 1;
    high = int(B**0.5);

    counter = 0;
    for i in range(low, high+1):
        if ispalin(i) and ispalin(i**2):
            counter += 1;

    # Output
    output_str = "Case #" + str(case+1) + ": " + str(counter) + "\n";
    fout.write(output_str)

    
fo.close();
fout.close();
