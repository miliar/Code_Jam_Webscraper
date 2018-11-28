#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long ull;
typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;

int t, n, x, p, cnt[5];
int dp[5][500000];

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    ios_base::sync_with_stdio(false);

    cin >> t;
    for (int ttt = 1; ttt <= t; ++ttt) {
        cin >> n >> p;
        cnt[0] = cnt[1] = cnt[2] = cnt[3] = 0;
        for (int i = 0; i < n; ++i) {
            cin >> x;
            ++cnt[x % p];
        }
        int ans = cnt[0];
        cnt[0] = 0;
        if (p == 2)
            ans += cnt[1] / 2, cnt[1] %= 2;
        else if (p == 3) {
            int x = min(cnt[1], cnt[2]);
            ans += x;
            cnt[1] -= x;
            cnt[2] -= x;
        } else {
            int x = min(cnt[1], cnt[3]);
            ans += x;
            cnt[1] -= x;
            cnt[3] -= x;
            ans += cnt[2] / 2, cnt[2] %= 2;
        }
        vector<int> v;
        for (int i = 0; i < p; ++i)
            while (cnt[i]--)
                v.push_back(i);
        int mn = 0;
        do {
            int cur = 0;
            int rem = 0;
            for (int i = 0; i < v.size(); ++i) {
                if (rem == 0)
                    ++cur;
                (rem += v[i]) %= p;
            }
            mn = max(mn, cur);
        } while (next_permutation(v.begin(), v.end()));
        ans += mn;
        cout << "Case #" << ttt << ": " << ans << endl;
    }

    return 0;
}
