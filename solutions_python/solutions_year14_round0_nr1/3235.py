'''
Created on Apr 12, 2014

@author: Ved

Code Jam 2014 Qualifying round problem A
'''


def main():
    f = open('A-small-attempt2.in', 'r');
    T = int(f.readline());
    g = open('A_small.out', 'w');
    
    for case in range(T):
        row1 = int(f.readline());
        M1 = [];
        for i in range(4):
            K = f.readline().split();
            if len(K) == 0:
                break;
            M1.append(map(int, K));
        row2 = int(f.readline());
        M2 = [];
        for i in range(4):
            K = f.readline().split();
            M2.append(map(int, K));

        t = set(M1[row1-1]);
        
        r = M2[row2-1];
        possibles = [];
        
        for e in r:
            if e in t:
                possibles.append(e);
            
        if len(possibles) == 0:
            g.write("Case #%s: Volunteer cheated!" % str(case+1));
        elif len(possibles) >= 2:
            g.write("Case #%s: Bad magician!" % str(case+1));
        else:
            g.write("Case #%s: %s" % (str(case+1), str(possibles[0])));
            
        if case < T-1:
            g.write("\n");

    f.close();
    g.close();



if __name__ == "__main__":
    main();