#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 1005
typedef long long ll;
const double pi = acos(-1.);
struct arr
{
    ll x, y;
    bool operator<(const arr &i) const
    {
        return x * y > i.x * i.y;
    }
} a[N];
int n, k;

void solve()
{
    scanf("%d%d", &n, &k);
    for (int i = 0; i < n; ++i)
        scanf("%lld%lld", &a[i].x, &a[i].y);
    sort(a, a + n);
    double ans = 0;
    for (int i = 0; i < n; ++i)
    {
        double s = 2 * pi * a[i].x * a[i].y;
        int kk = 1;
        if (kk < k)
            for (int j = 0; j < n; ++j)
                if (j != i && a[j].x <= a[i].x)
                {
                    s += 2 * pi * a[j].x * a[j].y;
                    ++kk;
                    if (kk == k)
                        break;
                }
        s += pi * a[i].x * a[i].x;
        if (kk == k)
            ans = max(ans, s);
    }
    printf("%.9f\n", ans);
}

int main()
{
    int t;
    freopen("1.txt", "r", stdin);
    freopen("2.txt", "w", stdout);
    scanf("%d", &t);
    for (int tt = 1; tt <= t; ++tt)
    {
        printf("Case #%d: ", tt);
        solve();
    }
    return 0;
}