#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
map<ll, ll> cnt;
int main()
{
    ios::sync_with_stdio(false);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; cas++)
    {
        cnt.clear();
        cout << "Case #" << cas << ": ";
        ll n, m;
        cin >> n >> m;
        cnt[n] = 1;
        ll tot = 0;
        ll ans;
        while (tot < m)
        {
            map<ll, ll>::iterator it = cnt.end();
            it--;
            pair <ll, ll> tmp = *it;
            cnt.erase(it);
            cnt[tmp.first >> 1] += tmp.second;
            cnt[(tmp.first - 1) >> 1] += tmp.second;
            tot += tmp.second;
            if (tot >= m){
                ans = tmp.first;
                break;
            }
        }
        cout << (ans >> 1) << ' ' << ((ans - 1) >> 1) << endl;
    }
    return 0;
}
