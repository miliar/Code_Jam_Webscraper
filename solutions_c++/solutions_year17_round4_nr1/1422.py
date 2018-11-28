#include <bits/stdc++.h>
using namespace std;

int dp(vector<int> &x, map<vector<int>, int> &mp, int p) {
    if (mp.find(x) != mp.end()) {
        return mp[x];
    }
    int rt = 0;
    for (int i = 1; i < p; i++) {
        for (int j = i; j < p; j++) {
            x[i - 1]--;
            x[j - 1]--;
            if (x[i - 1] >= 0 && x[j - 1] >= 0) {
                int k = (i + j) % p;
                if (k == 0) {
                    rt = max(rt, 1 + dp(x, mp, p));
                } else {
                    x[k - 1]++;
                    rt = max(rt, dp(x, mp, p));
                    x[k - 1]--;
                }
            }
            x[j - 1]++;
            x[i - 1]++;
        }
    }
    mp[x] = rt;
    return rt;
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int n, p;
        cin >> n >> p;
        vector<int> v(n);
        vector<int> cnt(p - 1);
        int total = 0;
        int ans = 0;
        for (int i = 0; i < n; i++) {
            cin >> v[i];
            total += v[i];
            if (v[i] % p == 0) {
                ans++;
            } else {
                cnt[v[i] % p - 1]++;
            }
        }
        map<vector<int>, int> mp;
        ans += dp(cnt, mp, p);
        if (total % p) {
            ans++;
        }
    
        cout << "Case #" << t << ": " << ans << endl;
    }
}
