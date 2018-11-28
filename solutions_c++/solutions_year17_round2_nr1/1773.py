#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large(1).in", "r", stdin);
    //freopen("output.txt", "w", stdout);
    int t, k, n, i, j;
    double d, p, q, x, y;
    scanf("%d", &t);
    for(k = 1; k <= t; k++)
    {
        scanf("%lf %d", &d, &n);
        x = 1000000000000000LL;
        for(i = 0; i < n; i++)
        {
            scanf("%lf %lf", &p, &q);
            x = min(x, d*q/(d-p));
        }
        printf("Case #%d: %.10lf\n", k, x);
    }
    return 0;
}
