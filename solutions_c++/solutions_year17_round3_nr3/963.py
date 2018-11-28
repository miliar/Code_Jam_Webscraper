#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
using namespace std;
#define N 55
double p[N];
double u;
int n, k;

double get()
{
    double ans = 1;
    for (int i = 1; i < n; ++i)
    {
        double d = (p[i] - p[i - 1]) * i;
        if (d <= u)
            u -= d;
        else
        {
            d = p[i - 1] + u / i;
            for (int j = 0; j < i; ++j)
                ans *= d;
            for (int j = i; j < n; ++j)
                ans *= p[j];
            return ans;
        }
    }
    double d = p[n - 1] + u / n;
    for (int j = 0; j < n; ++j)
        ans *= d;
    return ans;
}

void solve()
{
    scanf("%d%d", &n, &k);
    scanf("%lf", &u);
    for (int i = 0; i < n; ++i)
        scanf("%lf", &p[i]);
    sort(p, p + n);
    printf("%.7f\n", get());
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