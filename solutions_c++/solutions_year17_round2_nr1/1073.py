#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int d, n;

void solve()
{
    scanf("%d%d", &d, &n);
    double ans = 0;
    for (int i = 0; i < n; ++i)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        // a + b * t = d
        double t = double(d - a) / b;
        ans = max(ans, t);
    }
    printf("%.7f\n", d / ans);
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