#include <bits/stdc++.h>

using namespace std;

char s[1024];

void flip(int x) {
    if (s[x] == '+') s[x] = '-';
    else s[x] = '+';
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T, k, len, ans;

    scanf("%d", &T);
    for(int ncase=1; ncase<=T; ncase++) {
        scanf("%s %d", s, &k);
        len = strlen(s);
        ans = 0;

        for(int i=0; i<len; i++) {
            if (s[i] == '-') {
                if (i+k > len) {
                    ans = -1;
                    break;
                }
                for(int j=i; j<i+k; j++) {
                    flip(j);
                }
                ans++;
            }
        }

        if (ans >= 0) printf("Case #%d: %d\n", ncase, ans);
        else printf("Case #%d: IMPOSSIBLE\n", ncase);
    }

    return 0;
}
