#include <bits/stdc++.h>

using namespace std;

typedef long long LL;

int tang = 0;

int cnt[100], f[105][105][105], dd[105][105][105];

int p;

int getans(int a1, int a2, int a3) {
    if (a1 == 0 && a2 == 0 && a3 == 0) return 0;
    if (dd[a1][a2][a3] >= tang) return f[a1][a2][a3];
    int a[4];
    a[1] = a1; a[2] = a2; a[3] = a3;
    int ans = 0;
    for (int i = 1; i < p; i++) {
        if (a[i] > 0) {
            a[i]--;
            int tmp = a[1] * 1 + a[2] * 2 + a[3] * 3;
            if (tmp % p == 0) tmp = 1; else tmp = 0;
            ans = max(ans, getans(a[1],a[2],a[3])+tmp);
            a[i]++;
        }
    }
    dd[a1][a2][a3] = tang;
    return (f[a1][a2][a3] = ans);
}

void solve(int nt) {
    int n;
    scanf("%d%d", &n, &p);

    for (int i = 0; i < 4; i++) cnt[i] = 0;

    for (int i = 0; i < n; i++) {
        int a;
        scanf("%d", &a);
        cnt[a%p]++;
    }

    tang++;

    printf("Case #%d: %d\n", nt, getans(cnt[1],cnt[2],cnt[3])+cnt[0]);
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}