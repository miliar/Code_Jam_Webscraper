#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, i, j, d, n, k, v;
    double res, ans;
    for(scanf("%d", &T), j = 1; j <= T; ++j){
        scanf("%d %d", &d, &n);
        ans = 0;
        for(i = 1; i <= n; ++i){
            scanf("%d %d", &k, &v);
            res = (double)(d - k) / v;
            ans = fmax(ans, res);
        }
        printf("Case #%d: %.6f\n", j, d / ans);
    }
    return 0;
}
