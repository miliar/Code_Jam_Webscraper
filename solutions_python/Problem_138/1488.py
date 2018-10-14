#!/usr/bin/python3

def greater_index(nele,w):
    for k in range(len(w)):
        if w[k] > nele:
            return k;
    return -1;

def main():
    t = int(input());

    for i in range(t):
        n = int(input());
        wn_original = input().split();
        wk_original = input().split();
        for k in range(n):
            wn_original[k] = float(wn_original[k]);
            wk_original[k] = float(wk_original[k]);
        wn_original.sort();
        wk_original.sort();
#         print(wn_original);
#         print(wk_original);

        out_dwar = 0;
        out_war = 0;

        ### War
        wn = wn_original[:];
        wk = wk_original[:];
        j = 0;
        while wn:
#             print('wn:',wn,'wk:',wk);
            next_bigger_index = -1;
            next_bigger_index = greater_index(wn[0],wk);
            if next_bigger_index != -1:
                # There is something bigger that Ken will use
                wn.remove(wn[0]);
                wk.remove(wk[next_bigger_index]);
            else:
                out_war += 1;  #Naomi's Score
                wn.remove(wn[0]);
                wk.remove(wk[0]);
            j+=1;

        ### Deceitful War
        wn = wn_original[:];
        wk = wk_original[:];
        while wn and wn[-1] > wk[-1]:
            wn.pop();
            wk.pop();
            out_dwar += 1;

        while wn:
            if wn[0] > wk[-1]:
                out_dwar += 1;
            wn = wn[1:];
            wk.pop();
            while wn and wn[-1] > wk[-1]:
                wn.pop();
                wk.pop();
                out_dwar += 1;


#         print(wn,wk,n);
        print('Case #%d: %d %d'%(i+1,out_dwar, out_war), sep='');
    return 0;

if __name__ == '__main__':
    main();
