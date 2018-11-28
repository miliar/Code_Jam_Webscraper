#include <bits/stdc++.h>
using namespace std;

using lli = int64_t;

void solve(int t)
{
    lli n, k; cin >> n >> k;

    lli ans_ma = 0, ans_mi = 0;

    map<lli, lli> mp = {{n, 1}};

    for(auto it = mp.rbegin(); k > 0 && it != mp.rend(); ++it)
    {
        lli x = it->first;
        lli cnt = it->second;

        k -= cnt;

        if(x && x % 2 == 0)
        {
            lli a = x / 2;
            lli b = a - 1;

            ans_ma = a;
            ans_mi = b;

            mp[a] += cnt;
            mp[b] += cnt;
        }
        else
        if(x)
        {
            lli a = x / 2;

            ans_ma = a;
            ans_mi = a;

            mp[a] += cnt * 2;
        }
    }

    cout << "Case #" << t << ": " << ans_ma << ' ' << ans_mi << '\n';
}

int main()
{
    ios_base::sync_with_stdio(0);

    int t; cin >> t;

    for(int i = 1; i <= t; i++) solve(i);
    
    return 0;
}
