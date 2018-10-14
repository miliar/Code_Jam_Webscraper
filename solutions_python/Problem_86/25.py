input = open('C-small-attempt0.in','r');
output = open('output.txt','w');

nrTestCases = int(input.readline());

line = input.readline().strip('\n');
case = 1;
while line != '':
    print "Case #%d" % case
    # N, L and H
    values = line.split(' ');
    low = int(values[1]);
    high = int(values[2]);

    line = input.readline().strip('\n');
    frequencies = line.split(' ');
    frequencies = [int(freq) for freq in frequencies]
    imprFreq = -1;
    for i in range(low, high + 1):
        print i
        allZero = True;
        for freq in frequencies:
            if (i % freq) != 0 and (freq % i):
                allZero = False;
                break;
        
        if allZero == True:
            imprFreq = i;
            break;
    
    print imprFreq, allZero
    if imprFreq > -1:
        output.write('Case #%d: %d\n' % (case, imprFreq));
    else:
            output.write('Case #%d: NO\n' % case);

    case += 1;
    line = input.readline().strip('\n');
