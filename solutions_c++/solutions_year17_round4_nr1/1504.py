#include <bits/stdc++.h>
using namespace std;
int main() {
    int tc;
    scanf("%d", &tc);
    
    for (int q = 1; q <= tc; q++) {
        int g, pack;
        cin >> g >> pack;
        int grp[105];
        int counter = 0, rem = 0;
        for (int i = 0; i < g; i++) {
            int temp;
            scanf("%d", &temp);
            grp[i] = temp % pack;
            if (grp[i] == 0) counter++;
        }
        
        for (int i = 0; i < g; i++) {
            //printf("%d ", grp[i]);
        }
        for (int i = 0; i < g; i++) {
            for (int j = i+1; j < g; j++) {
                if (grp[i] + grp[j] == pack) {
                    counter += 1;
                    grp[i] = 0;
                    grp[j] = 0;
                }
            }
        }
        sort(grp, grp + g);
        bool f = false;
        for (int i = 0; i < g; i++) {
            if (grp[i]) f = true;
        }
        if (!f) {
            printf("Case #%d: %d\n", q, counter);
            continue;
        }
       // cout << counter << endl;
        if (pack == 2) {
            int c = 0;
            for (int i = 0; i < g; i++) {
                if (grp[i] == 1) {
                    c++;
                }
            }
            if (c > 0) {
                counter += (c-1)/2 + 1;
            }
            
        }
        if (pack == 3) {
            int c = 0, type = 0;
            for (int i = 0; i < g; i++) {
                if (grp[i]) {
                    type = grp[i];
                    c++;
                }
            }
            if (c > 0) {
            if (type == 1) {
                counter += (c-1)/ 3+1;
            }
            else {
                counter += (c-1)/3 + 1;
            }
            }
        }
        if (pack == 4) {
            bool met = false;
            int first = 0, c = 0, d = 0, type = 0, type2 = -1;
            int ca=0,cb=0,cc=0;
            for (int i = 0; i < g; i++) {
                if (grp[i] == 1) {
                    ca++;
                }
                if (grp[i] == 2) {
                    cb++;
                }
                if (grp[i] == 3) {
                    cc++;
                }
            }
            //assert(first != 0);
            if (cb == 1 && cc == 0 && ca == 0) {
                counter += 1;
            }
            else {

                //printf("TEST %d %d %d\n", ca, cb, cc);

                if (ca != 0) {
                    if (cb == 0) {
                        //cout << counter << endl;
                        counter += (ca-1)/ 4+1;
                       // cout << counter << endl;
                    }
                    else {
                        ca -= 2;
                        counter++;
                        if (ca > 0) {
                        counter += (ca-1)/ 4+1;
                        }
                    }
                }
                else if (cc != 0) {
                    if (cb == 0) {
                        counter += (cc-1)/ 4+1;
                    }
                    else {
                        cc -= 2;
                        counter++;
                        if (cc > 0) {
                        counter += (cc-1)/ 4+1;
                        }
                    }
                }
            
            }
        }
        
        
        printf("Case #%d: %d\n", q, counter);
    }
}