#include <bits/stdc++.h>
using namespace std;

int kases;
char s[2000];
int n, k, ans;

void flip(int i) {
    for (int j = 0; j < k; ++j)
        s[i + j] = 1 - s[i + j];
}

int main(){
    
    #ifdef ULTMASTER
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    #endif
    scanf("%d", &kases);
    for (int kase = 1; kase <= kases; ++kase) {
        scanf("%s%d", s, &k);
        n = strlen(s);
        for (int i = 0; i < n; ++i) {
            if (s[i] == '+') s[i] = 1;
            else s[i] = 0;
        }
        ans = 0;
        for (int i = 0; i < n - k + 1; ++i)
            if (!s[i]) {
                flip(i);
                ++ans;
            }
        for (int i = 0; i < n; ++i)
            if (!s[i]) ans = -1;
        if (ans == -1)
            printf("Case #%d: IMPOSSIBLE\n", kase);
        else
            printf("Case #%d: %d\n", kase, ans);
    }

    return 0;
}
