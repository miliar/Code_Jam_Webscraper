#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int tt;
    scanf("%d", &tt);
    for (int ti = 1; ti <= tt; ti++)
    {
        int n;
        double d, ans = 1e20;
        scanf("%lf%d", &d, &n);
        for (int i = 1; i <= n; i++)
        {
            double k, s;
            scanf("%lf%lf", &k, &s);
            ans = min(ans, k * s / (d - k) + s);
        }
        printf("Case #%d: %.7f\n", ti, ans);
    }
    return 0;
}
