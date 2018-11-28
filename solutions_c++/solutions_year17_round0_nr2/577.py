#include <bits/stdc++.h>

using namespace std;

char S[20];

int main() {

    // freopen("B-large.in", "r", stdin);
    // freopen("B-large.out", "w", stdout);

    int T, l, k = 0, i, j, ok;

    scanf("%d", &T);
    while(T--) {
        printf("Case #%d: ", ++k);
        scanf("%s", S);
        l = strlen(S);
        if (l == 1) {
            puts(S);
        } else {
            i = 0;
            do {
                ok = 1;
                for(;i<l-1;i++) {
                    if (S[i] > S[i+1]) {
                        for(j=i;j>=0&&S[j]=='0';j--)
                            S[j] = '9';
                        S[j]--;
                        for(j=i+1;j<l;j++)
                            S[j] = '9';
                        ok = 0;
                        break;
                    }
                }
                for(i=0;i<l&&S[i]=='0';i++);
            } while(!ok);
            puts(S+i);
        }
    }

    return 0;
}
