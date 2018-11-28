#include <cstdio>
#include <cstddef>
#include <iostream>
#include <limits>

using namespace std;

double solve()
{
    double d;
    size_t n;
    cin >> d >> n;
    double maxTime = 0.0;
    for (size_t i = 0; i < n; ++i)
    {
        double k, s;
        cin >> k >> s;
        double t = (d - k) / s;
        if (t > maxTime)
            maxTime = t;
    }
    return d/maxTime;
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