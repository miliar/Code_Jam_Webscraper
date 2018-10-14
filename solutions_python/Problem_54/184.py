def gcd (a, b):
    if a == 0 or b == 0:
        return a+b;
    if a > b:
        return gcd (a % b, b);
    return gcd (a, b % a);

f1 = open ("input.txt", "r");
f2 = open ("output.txt", "w");
t = int(f1.readline());
for i in range (0, t):
    m = f1.readline();
    a = m.split(" ");
    for j in range (1, int(a[0])):
        a[j] = int (a[j]) - int (a[j+1]);
        if a[j] < 0:
            a[j] *= -1;
    r = a[1];
    for j in range (2, int (a[0])):
        if not (a[j] == 0):
            r = gcd (r, int(a[j]))
    y = 0;
    if not (int(a[int(a[0])]) % r == 0):
        y = r - (int(a[int(a[0])]) % r);
    y = "Case #" + str(i + 1) + ": " + str(y) + "\n";
    f2.write(y);
        
