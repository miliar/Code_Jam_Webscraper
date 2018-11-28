#include <bits/stdc++.h>

using namespace std;

char str[1010];

void flip(int x, int k) {
    for(int i=x; i<x+k; ++i) {
        if(str[i] == '-') str[i] = '+';
        else str[i] = '-';
    }
}

void solve() {
    scanf("%s", str);
    int k;
    scanf("%d", &k);
    int len = strlen(str);
    int ans = 0;
    for(int i=0; i<=len-k; ++i) {
        if(str[i] == '-') {
            flip(i, k);
            ++ ans;
        }
    }
    for(int i=len-k+1; i<len; ++i) {
        if(str[i] == '-') {
            puts("IMPOSSIBLE");
            return;
        }
    }
    printf("%d\n", ans);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    int T;
    scanf("%d", &T);
    int cas = 0;
    while(T--) {
        printf("Case #%d: ", ++cas);
        solve();
    }

    return 0;
}
