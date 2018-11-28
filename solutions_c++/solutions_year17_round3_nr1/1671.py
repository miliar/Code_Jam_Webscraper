#include <cstdio>
#include <algorithm>
#include <vector>
#include <functional>
#include <cmath>
using namespace std;
typedef pair<int, int> pii;
typedef long long ll;
const double PI = 3.141592653589793238;

int n, k;
pii a[1000];

double solve()
{
    double ans = 0;
    sort(a, a + n, greater<pii>());
    for (int i = 0; i <= n - k; i++) {
        vector<ll> v;
        for (int j = i + 1; j < n; j++)
            v.push_back((ll)a[j].first * a[j].second);
        sort(v.begin(), v.end(), greater<ll>());

        ll ri = a[i].first, hi = a[i].second;
        double si = PI * ri * ri + 2 * PI * ri * hi;
        for (int j = 0; j < k - 1; j++)
            si += 2 * PI * v[j];
        ans = max(ans, si);
    }
    /*
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) {
            printf("%lld ", memo[i][j]);
        }
        printf("\n");
    }
    */
    return ans;
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int tc = 1; tc <= T; tc++) {
        scanf("%d%d", &n, &k);
        for (int i = 0; i < n; i++) 
            scanf("%d%d", &a[i].first, &a[i].second);
        double ans = solve();
        printf("Case #%d: %.12f\n", tc, ans);
    }
    return 0;
}
