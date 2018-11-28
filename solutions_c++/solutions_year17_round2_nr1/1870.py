#include <iostream>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

int n, d, A[1050], B[1050];

bool can(double x)
{
    double t = 1.0 * d / x;
    for(int i = 0;i < n;++i)
    {
        double t1 = 1.0 * (d - A[i]) / (1.0 * B[i]);
        if(t < t1)      return false;
    }
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("sout.out", "w", stdout);

    int t, c = 0;
    scanf("%d", &t);
    while(t--)
    {
        ++c;
        scanf("%d%d", &d, &n);
        for(int i = 0;i < n;++i)
            scanf("%d%d", A + i, B + i);

        double lo = 0, hi = 1e20;
        for(int i = 0;i < 350;++i)
        {
            double mid = (lo + hi) / 2.0;
            if(can(mid))
                lo = mid;
            else
                hi = mid;
        }
        printf("Case #%d: %.7f\n", c, lo);
    }
    return 0;
}
