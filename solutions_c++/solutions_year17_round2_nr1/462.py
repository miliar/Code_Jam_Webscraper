#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
const int mod = 1e9 + 7;
const int inf = 1e14 + 7;
int read()
{
    int x;
    scanf("%I64d", &x);
    return x;
}
void solve(int test)
{
    int n, m, i, j;
    cin >> m >> n;
    int x, y;
    double ans = inf;
    for(i = 1; i <= n; i ++)
    {
        cin >> x >> y;
        ans = min(ans, 1.0 * m / (1.0 * (m - x) / y));
    }
    cout << "Case #" << test << ": ";
    printf("%.10f\n", ans);
}
main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++)
    {
        solve(i);
    }
}

