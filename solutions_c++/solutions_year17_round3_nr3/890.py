#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstddef>
#include <iostream>

using namespace std;

#define MAXN 50

int n, k;
double u;
double p[MAXN];

double solve()
{
    cin >> n >> k;
    cin >> u;
    for (int i = 0; i < n; ++i)
    {
        cin >> p[i];
    }
    sort(p, p + n);

    while (u > 0.0)
    {
        double lp = p[0];
        int diffidx = 1;
        while ((diffidx < n) && (p[diffidx] <= lp))
        {
            ++diffidx;
        }
        if (diffidx == n)
        {
            double add = u / n;
            for (int i = 0; i < n; ++i)
                p[i] += add;
            u = 0.0;
        }
        else
        {
            int count = diffidx;
            double maxadd = p[diffidx] - lp;
            if (count*maxadd <= u)
            {
                double add = maxadd;
                u -= count*add;
                for (int i = 0; i < count; ++i)
                    p[i] += add;
            }
            else
            {
                double add = u / (double)count;
                u = 0.0;
                for (int i = 0; i < count; ++i)
                    p[i] += add;
            }
        }
    }
    double tp = 1.0;
    for (int i = 0; i < n; ++i)
    {
        tp *= p[i];
    }
    return tp;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
    {
        printf("Case #%d: %.6f\n", i, solve());
    }
}
