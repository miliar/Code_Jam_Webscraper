#include <bits/stdc++.h>
#define ll long long
using namespace std;

string s;

string ans;

int n;

bool was[111][111][2];

bool dp[111][111][2];

bool solve(int id, int prev, bool flag) {
    if (id == n)
        return true;
    if (was[id][prev][flag])
        return dp[id][prev][flag];
    was[id][prev][flag] = true;
    int up = flag ? s[id] - '0' : 9;
    for (int i = up; i >= prev; --i) {
        if (solve(id + 1, i, flag & (i == up))) {
            cerr << id << " " << i << "\n";
            ans.push_back('0' + i);
            return dp[id][prev][flag] = true;
        }
    }
    return dp[id][prev][flag] = false;
}

int main() {
#ifdef LOCAL
    freopen("xxx.in", "r", stdin);
    freopen("xxx.out", "w", stdout);
#endif
    int t;
    cin >> t;
    for (int tt = 0; tt < t; ++tt) {
        cin >> s;
        n = (int)s.size();
        memset(was, 0, sizeof was);
        ans.clear();
        solve(0, 0, true);
        while ((int)ans.size() > 1 && ans.back() == '0')
            ans.pop_back();
        reverse(ans.begin(), ans.end());
        cout << "Case #" << tt + 1 << ": " << ans << "\n";
    }
    return 0;
}