#include <bits/stdc++.h>

#define fst first
#define snd second

using namespace::std;

const int maxn = 1e3 + 5;
int n, k, dir[maxn], f[maxn];
char s[maxn];

void solve() {
    scanf("%s%d", s, &k);
    n = strlen(s);
    for (int i = 0; i < n; i++) {
        if (s[i] == '-') dir[i] = 1;
        else dir[i] = 0;
        f[i] = 0;
    }
    int res = 0, sum = 0;
    for (int i = 0; i + k <= n; i++) {
        if ((dir[i] + sum) % 2) {
            res++; f[i] = 1;
        }
        sum += f[i];
        if (i - k + 1 >= 0) sum -= f[i-k+1];
    }
    for (int i = n - k + 1; i < n; i++) {
        if ((dir[i] + sum) % 2) {
            puts("IMPOSSIBLE"); return;
        }
        if (i - k + 1 >= 0) sum -= f[i-k+1];
    }
    printf("%d\n", res);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int t; scanf("%d", &t);
    for (int Case = 1; Case <= t; Case++) {
        printf("Case #%d: ", Case);
        solve();
    }
    return 0;
}
