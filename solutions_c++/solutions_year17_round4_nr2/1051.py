#include <bits/stdc++.h>
#define int long long
using namespace std;
const int N = 1123456;
int cnt[1010][1010];
int d[1010];
void solve(int xx)
{
    int n, m, i, j, k, x, y;
    cin >> n >> m >> k;
    for(i = 1; i <= n; i ++) {
        d[i] = 0;
        for(j = 1; j <= m; j ++) {
            cnt[i][j] = 0;
        }
    }
    for(i = 1; i <= k; i ++) {
        cin >> x >> y;
        cnt[x][y] ++;
    }
    int ans = 0;
    for(i = 1; i <= m; i ++) {
        int s = 0;
        for(j = 1; j <= n; j ++)
            s += cnt[j][i];
        if(ans < s)
            ans = s;
    }
    int anss = 0;
    while(1) {
        int id = 0, mx = 0;
        for(int i = 2; i <= n; i ++) {
            int s = 0;
            for(int j = 1; j <= m; j ++) {
                s += cnt[i][j];
            }
            if(s + d[i]> mx) {
                mx = s + d[i];
                id = i;
            }
        }
        int mxx = 1e9;
        int ind = 0;
        for(int i = 1; i < id; i ++) {
            int s = 0;
            for(int j = 1; j <= m; j ++) {
                s += cnt[i][j];
            }
            if(s < mxx + d[i] && s + d[i] + 1 < mx) {
                mxx = s + d[i];
                ind = i;
            }
        }
        if(ind == 0 || ans >= mx)
            break;
        bool ok = 1;
        for(i = 1; i <= m; i ++) {
            if(cnt[id][i] != 0) {
                d[ind] ++;
                cnt[id][i] --;
                ok = 0;
                break;
            }
        }
        if(ok)
            break;
        anss ++;
    }
    for(i = 1; i <= n; i ++) {
        int s = 0;
        for(j = 1; j <= m; j ++)
            s += cnt[i][j];
        if(ans < s + d[i])
            ans = s + d[i];
    }
    cout << "Case #" << xx << ": " << ans << " " << anss << endl;
}
main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++) {
        solve(i);
    }
}
