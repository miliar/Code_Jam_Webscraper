#include <bits/stdc++.h>
using namespace std;


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        int d, n;
        cin >> d >> n;
        double ans = 0;
        for(int i = 0; i < n; i++)
        {
            int k, s;
            scanf("%d%d", &k, &s);
            ans = max(ans, 1.0 * (d - k) / s);
        }
        ans = d / ans;
        printf("Case #%d: %.8f\n", cas, ans);
    }
    return 0;
}

