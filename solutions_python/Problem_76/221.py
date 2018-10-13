cin = open("in.txt")
cout = open("out.txt" , "w")
TestCase = cin.readline()
for TestNumber in range(1 , int(TestCase)+1):
    N = cin.readline()
    realsum , xorsum , minval = 0 , 0 , 1000000
    Candy = cin.readline().split()
    for c in Candy:
        c = int(c)
        realsum += c
        xorsum ^= c
        minval = min(minval , c)
    cout.write("Case #" + str(TestNumber) + ": ")
    if xorsum != 0:
        cout.write("NO\n")
    else:
        cout.write(str(realsum - minval) + "\n")
