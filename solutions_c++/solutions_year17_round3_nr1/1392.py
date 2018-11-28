#include <bits/stdc++.h>
using namespace std;

const double PI = acos(-1.0);
const int MAXN = 1010;
struct PLATE {
    int r, h;
    double s_ce;
};
PLATE p[MAXN];

int n, k;

int cmp(PLATE a, PLATE b) {
    return a.s_ce > b.s_ce;
}

double solve() {
    sort(p, p + n, cmp);
    double ans = 0.0;
    for(int i = 0; i < n; i++) { // maxr
        int maxr = p[i].r, cnt = 1;
        double s = PI * p[i].r * p[i].r + p[i].s_ce;
        for(int j = 0; j < n; j++) { // greedy
            if(cnt == k) break;
            if(j == i || p[j].r > maxr) continue;
            s += p[j].s_ce;
            cnt++;
        }
        ans = max(ans, s);
    }
    return ans;
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, cse = 1;
    scanf("%d", &T);
    while(T--) {
        scanf("%d%d", &n, &k);
        for(int i = 0; i < n; i++) {
            scanf("%d%d", &p[i].r, &p[i].h);
            p[i].s_ce = 2.0 * PI * p[i].r * p[i].h;
        }
        printf("Case #%d: %.9f\n", cse++, solve());
    }
    return 0;
}
