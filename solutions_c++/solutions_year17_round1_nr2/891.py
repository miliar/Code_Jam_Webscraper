#include <cstdio>
#include <cstring>
#include <cmath>
#include <set>
#include <algorithm>
using namespace std;
#define MAXN 53
#define MAXM 5003
int n, p;
int a[MAXN];
struct LR {
    int l, r;
    bool operator< (const LR &x)const
    {
        return l < x.l || (l == x.l && r < x.r);
    }
} b[MAXN][MAXN];
int main()
{
    int T;
    scanf("%d", &T);
    for (int Ti = 1; Ti <= T; ++Ti) {
        scanf("%d%d", &n, &p);
        for (int i = 0; i < n; ++i)
            scanf("%d", &a[i]);
        int mx = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < p; ++j) {
                double t;
                scanf("%lf", &t);
                t /= a[i];
                b[i][j].r = floor(t / 0.9);
                b[i][j].l = ceil(t / 1.1);
                mx = max(mx, b[i][j].r);
            }
        }
        int ans = 0;
        multiset<int> f[MAXN];
        for (int i = 1; i <= mx; ++i) {
            int ms = 100000;
            for (int j = 0; j < n; ++j) {
                while (f[j].size() && *f[j].rbegin() < i)
                    f[j].erase(--f[j].end());
                for (int k = 0; k < p; ++k)
                    if (b[j][k].l <= b[j][k].r && b[j][k].l == i)
                        f[j].insert(b[j][k].r);
                ms = min(ms, (int)f[j].size());
            }
            if (ms != 0) {
                ans += ms;
                for (int j = 0; j < n; ++j)
                    for (int k = 0; k < ms; ++k)
                        f[j].erase(f[j].begin());
            }
        }
        printf("Case #%d: %d\n", Ti, ans);
    }
    return 0;
}
