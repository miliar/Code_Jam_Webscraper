#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
using namespace std;
const double pi = acos(-1);
struct pancake {
    double r, h, s;
} p[1005];
bool cmp1(const pancake& lhs, const pancake& rhs)
{
    return lhs.r < rhs.r;
}
bool cmp2(const pancake& lhs, const pancake& rhs)
{
    return lhs.s > rhs.s;
}
int main()
{
    int T;
    int n, k;
    scanf("%d", &T);
    for (int cases = 1; cases <= T; cases++) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) {
            scanf("%lf%lf", &p[i].r, &p[i].h);
            p[i].s = 2 * pi * p[i].r * p[i].h;
        }
        sort(p, p + n, cmp1);
        double ans = 0;
        for (int i = k - 1; i < n; i++) {
            double tmp = pi * p[i].r * p[i].r + p[i].s;
            sort(p, p + i, cmp2);
            for (int j = 0; j < k - 1; j++) {
                tmp += p[j].s;
            }
            ans = max(ans, tmp);
        }
        printf("Case #%d: %.15f\n", cases, ans);
    }
    return 0;
}
