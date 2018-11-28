#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>

using namespace std;

const int maxn = 50 + 5;
const double eps = 1e-10;

double p[maxn];

double dcmp(double x)
{
    if(fabs(x) < eps) return 0;
    return x > 0 ? 1 : -1;
}

bool check(int n, double mid, double u)
{
    for(int i = 1; i <= n; ++i)
    {
        if(dcmp(p[i] - mid) < 0)
        {
            double delt = mid - p[i];
            if(dcmp(delt - u) > 0) return false;
            u -= delt;
        }
    }
    return true;
}

int main()
{
    freopen("C-small-1-attempt0.in", "r", stdin);
    freopen("answer.out", "w", stdout);
    int T, cas = 0;
    scanf("%d", &T);
    while(T--)
    {
        int n, m;
        double u;
        scanf("%d%d%lf", &n, &m, &u);
        for(int i = 1; i <= n; ++i) scanf("%lf", &p[i]);
        double l = 0, r = 1;
        for(int i = 0; i < 100; ++i)
        {
            double mid = (l + r) / 2;
            if(check(n, mid, u)) l = mid;
            else r = mid;
        }
        printf("Case #%d: ", ++cas);
        double ans = 1;
        for(int i = 1; i <= n; ++i) ans *= max(p[i], l);
        printf("%.10f\n", ans);
    }
    return 0;
}
