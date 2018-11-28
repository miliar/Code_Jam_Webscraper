#include <bits/stdc++.h>

using namespace std;

const long double pi = 3.14159265358979323846L;

typedef long long LL;

const int N = 1005;

int r[N], h[N], vt[N];

inline bool cmp(int i, int j) {
    return r[i] < r[j];
}

void solve(int nt) {
    int n, k;
    scanf("%d%d", &n, &k);

    LL ans = 0;

    for (int i = 0; i < n; i++) {
        scanf("%d%d", r+i, h+i);
        vt[i] = i;
    }

    sort(vt, vt+n, cmp);

    multiset<LL> ms;
    LL now = 0;
    for (int i = 0; i < n; i++) {
        LL tmp = LL(r[vt[i]])*h[vt[i]]*2;
        now += tmp;
        LL res = now + LL(r[vt[i]]) * r[vt[i]];
        if (ms.size() >= k) res -= *(ms.begin());
        ans = max(ans, res);
        ms.insert(tmp);
        while (ms.size() > k) {
            now -= *(ms.begin());
            ms.erase(ms.begin());
        }
    }

    long double res = ans;
    res = res * pi;

    printf("Case #%d: %.10Lf\n", nt, res);
}

int main() {
    int ct;
    scanf("%d", &ct);
    for (int nt = 1; nt <= ct; nt++) {
        solve(nt);
        fprintf(stderr, "Case %d done.\n", nt);
    }
}
