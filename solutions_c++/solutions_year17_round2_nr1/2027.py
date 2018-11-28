#include <bits/stdc++.h>

using namespace std;

int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, i;
    scanf("%d", &t);
    for(i=1; i<=t; i++)
    {
        double d, x, s, mx = 0;
        int n;
        scanf("%lf %d", &d, &n);
        for(int j=0; j<n; j++)
        {
            scanf("%lf %lf", &x, &s);
            mx = max(mx, (d-x)/s);
        }
        double res = d/mx;
        printf("Case #%d: %0.10lf\n",i, res);
    }
    return 0;
}
