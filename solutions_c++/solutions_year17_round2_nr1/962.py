#include <bits/stdc++.h>
using namespace std;

int d;
long long x[2], v[2];

bool will_meet()
{
    if (v[0] <= v[1])
        return false;

    return x[0] * (v[0] - v[1]) + v[0] * (x[1] - x[0]) < (v[0] - v[1]) * d;
}

int main()
{
    int t;
    scanf ("%d", &t);

    for (int test=1; test<=t; test++)
    {
        int n;
        scanf ("%d%d", &d, &n);

        for (int i=0; i<n; i++)
            scanf ("%lld%lld", x + i, v + i);

        if (n == 2 and x[1] < x[0])
            swap(x[0], x[1]), swap(v[0], v[1]);

        if (n == 1)
            x[1] = d, v[1] = 0;

        int i = will_meet() ? 1 : 0;

        long double res = v[i] * d;
        res /= (d - x[i]);
        printf("Case #%d: %.8Lf\n", test, res);
    }
    
    return 0;
}