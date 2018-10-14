f = open('input.txt');
o = open('output.txt', 'w');

T = int(f.readline());

base = set(['Q', 'W', 'E', 'R', 'A', 'S', 'D', 'F']);



casenum = 1;
for line in f:
    strdata = line.split();
    C = int(strdata[0]); #the number of base-pair -> non-base combinations
    combos = strdata[1:C+1];
    D = int(strdata[C+1]); #number of opposing pairs
    opposites = strdata[C+2:C+D+2];
    N = int(strdata[-2]); #length of sequence
    sequence = strdata[-1];
    
    comboPairs = {};
    for letter in base:
        comboPairs[letter] = set([]);
    
    comboDict = {};
    
    for combo in combos:
        comboPairs[combo[0]].add(combo[1]);
        comboPairs[combo[1]].add(combo[0]);
        comboDict[combo[0:2]] = combo[2];
        comboDict[combo[1]+combo[0]] = combo[2];
        
    oppositePairs = {};
    for letter in base:
        oppositePairs[letter] = set([]);
        
    for opposite in opposites:
        oppositePairs[opposite[0]].add(opposite[1]);
        oppositePairs[opposite[1]].add(opposite[0]);
        
    out = [];
    current = set(out);
    for letter in sequence:
        out.append(letter);
        current.add(letter);
        if len(out) == 1:
            continue;
        if out[-2] in base:
            if letter in comboPairs[out[-2]]:
                nonbase = comboDict[out[-2]+out[-1]];
                out.pop();
                out.pop();
                out.append(nonbase);
                current = set(out);
        last = out[-1];
        if last in base:
            for opposite in oppositePairs[last]:
                if opposite in current:
                    out = [];
                    current = set();
                    break;
            
        #print 'current sequence: ' + str(out) + '\n';
    strout = ", ".join(out);
    o.write("Case #"+str(casenum)+": ["+strout+']\n');
        
    casenum += 1;

    
    
f.close();
o.close();