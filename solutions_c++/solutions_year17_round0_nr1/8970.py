#include<bits/stdc++.h>
#define tr(x) cout << #x << " " << x << endl
using namespace std;

const int inf = (int) 1e8;

int t, n, k;

char s[1005];
int  a[1005];

bool read() {
    if (scanf("%s %d", s, &k) < 2) {
        return false;
    }
    n = strlen(s);
    for (int i = 0; i < n; i++) {
        a[i] = (s[i] == '+');
    }
    return true;
}

void solve() {
    int ans = 0;
    for (int i = 0; i < n - k + 1; i++) {
        if (!a[i]) {
            ++ans;
            for (int j = i; j < i + k; j++) {
                a[j] ^= 1;
            }
        }
    }
    bool can = true;
    for (int i = 0; i < n; i++) {
        can &= (a[i] == 1);
    }
    if (can) {
        printf("%d\n", ans);
    }
    else {
        printf("IMPOSSIBLE\n");
    }
}

int main() {
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++) {
        read();
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}

