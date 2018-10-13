def gcd(a, b):
    if (a == 0):
        return b;
    return gcd(b % a, a);

fi = open("input.txt", "r");
fo = open("output.txt", "w");
C = int(fi.readline());
for i in range (1, C+1):
    a = fi.readline();
    t = a.split(" ");
    N = int(t[0]);
    for j in range (1, N):
        t[j] = int(t[j + 1]) - int(t[j]);
        if (t[j] < 0):
            t[j] *= -1;
    for l in range (2, N):
        if not(t[l] == 0):
            t[1] = gcd(t[1]%t[l],t[l]);
    answer = int(t[N]) % int(t[1]);
    if (answer > 0):
        answer = int(t[1]) - answer;
    fo.write("Case #" + str(i) + ": " + str(answer) + "\n");

    
