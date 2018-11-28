#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
int a[N];
int cnt[N];
void solve(int x)
{
    int n, m, i, j;
    cin >> n >> m;
    for(j = 0; j <= m; j ++)
        cnt[j] = 0;
    for(i = 1; i <= n; i ++)
    {
        cin >> a[i];
        cnt[a[i] % m] ++;
    }
    if(m == 2)
    {
        cout << "Case #" << x << ": " << cnt[0] + cnt[1] / 2 + ((cnt[1] % 2 == 1)) << endl;
    }
    if(m == 3)
    {
        int ans = cnt[0];
        int t = min(cnt[1], cnt[2]);
        ans += t;
        cnt[1] -= t;
        cnt[2] -= t;
        ans += cnt[1] / 3;
        ans += cnt[2] / 3;
        if((cnt[1] % 3 != 0 || cnt[2] % 3 != 0))
            ans ++;
        cout << "Case #" << x << ": " << ans  << endl;
    }
}
main()
{
    freopen("A-small-attempt5.in", "r", stdin);
    freopen("A-small-attempt5.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++) {
        solve(i);
    }
}
