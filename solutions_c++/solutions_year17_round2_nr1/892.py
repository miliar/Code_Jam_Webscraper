#include <cstdio>
#include <algorithm>
using namespace std;
int main()
{
    freopen("ain.txt", "r", stdin);
    freopen("aout2.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int z = 0; z < t; ++z)
    {
        double d;
        int n;
        scanf("%lf%d", &d, &n);
        double mxTime = 0;
        for (int i = 0; i < n; i++)
        {
            double k, s;
            scanf("%lf%lf", &k, &s);
            mxTime = max(mxTime,
                         (d-k)/s);

        }
        printf("Case #%d: %.7lf\n", z+1, d/mxTime);
    }
    return 0;
}
