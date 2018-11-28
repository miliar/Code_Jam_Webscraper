#include <cstdio>
#include <cmath>
#include <algorithm>

int main()
{
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {

        int d, n;
        scanf("%d%d", &d, &n);
        double maxTime = 0;
        for (int i = 0; i < n; ++i) {
            int u, s;
            scanf("%d%d", &u, &s);
            double time = (d-u)/(double)s;
            maxTime = std::max(maxTime, time);
        }

        printf("Case #%d: %.7lf\n", t, d / maxTime);

    }
    return 0;
}