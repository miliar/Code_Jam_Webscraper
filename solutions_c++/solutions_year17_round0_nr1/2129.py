#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

const int N = 1005;

char s[N];
int a[N];

void solve(int nt) {
    int k;
    scanf("%s", s);
    scanf("%d", &k);
    printf("Case #%d: ", nt);
    int ans = 0;
    int n = strlen(s);
    for (int i = 0; i < n; i++) a[i] = 0;
    int now = 0;
    for (int i = 0; i+k-1 < n; i++) {
        now ^= a[i];
        int tmp = ((s[i] == '+')?1:0)^now;
        if (tmp == 0) {
            ans++;
            now ^= 1;
            a[i+k] ^= 1;
        }
    }
    for (int i = n-k+1; i < n; i++) {
        now ^= a[i];
        int tmp = ((s[i] == '+')?1:0)^now;
        if (tmp == 0) {
            printf("IMPOSSIBLE\n"); return;
        }
    }

    printf("%d\n", ans);
}

int main() {
    int ct;
    scanf("%d", &ct);

    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
