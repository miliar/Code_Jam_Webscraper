#include <bits/stdc++.h>

using namespace std;

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T, len;
    char n[32];

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%s", n);
        len = strlen(n);

        bool nines = false;
        for(int i=1; i<len; i++) {
            if (n[i] < n[i-1]) {
                if (n[i-1] == '1') {
                    nines = true;
                }
                else {
                    for(int j=i-1; j>=0; j--) {
                        if (j==0 || n[j]!=n[j-1]) {
                            n[j]--;
                            for(int k=j+1; k<len; k++) {
                                n[k] = '9';
                            }
                            break;
                        }
                    }
                }
                break;
            }
        }

        if (nines) {
            printf("Case #%d: ", ncase);
            for(int i=1; i<len; i++) printf("9");
            printf("\n");
        }
        else {
            printf("Case #%d: %s\n", ncase, n);
        }
    }

    return 0;
}
