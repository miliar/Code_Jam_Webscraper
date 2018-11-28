#include <bits/stdc++.h>

using namespace std;

#define int int64_t

void solve()
{
    int n, p;
    cin >> n >> p;
    int g[n];
    int cnt[p] = {0};
    for(auto &it: g)
    {
        cin >> it;
        it %= p;
        cnt[it]++;
    }
    if(p == 2)
    {
        cout << cnt[0] + (cnt[1] + 1) / 2 << endl;
        return;
    }
    if(p == 3)
    {
        cout << cnt[0] + min(cnt[1], cnt[2]) + (abs(cnt[1] - cnt[2]) + 2) / 3 << endl;
        return;
    }
}

signed main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;
    for(int z = 1; z <= t; z++)
    {
        cout << "Case #" << z << ": ";
        solve();
    }
}
