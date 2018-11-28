#include <cstdio>
#include <algorithm>
using namespace std;
typedef long long ll;

ll n, d, k[1024], s[1024];

double solve()
{
    double maxt = 0;
    for (int i = 0; i < n; i++) {
        double newt = (double)(d - k[i]) / s[i];
        maxt = max(maxt, newt);
    }
    return d / maxt;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%lld%lld", &d, &n);
        for (int i = 0; i < n; i++)
            scanf("%lld%lld", &k[i], &s[i]);
        double ans = solve();
        printf("Case #%d: %.12f\n", tc, ans);
    }
    return 0;
}
