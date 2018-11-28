#include <bits/stdc++.h>
using namespace std;

using i64 = long long;

map<i64, i64> mp;
i64 n;

int main() {
    freopen("dat.in", "r", stdin);
    freopen("dat.out", "w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0), cout.tie(0);
    int tsk;
    i64 x, k, s, mn, mx;

    cin >> tsk;
    for (int t = 1; t <= tsk; ++t) {
        cin >> n >> k;

        mp.clear();
        mp[n] = 1;
        while (k > 0) {
            auto it = mp.end(); --it;

            if ((it->first) % 2)
                mp[(it->first) / 2]+= (it->second) * 2;
            else {
                mp[(it->first) / 2]+= (it->second);
                mp[(it->first - 1) / 2]+= (it->second); }

            mn = (it->first - 1) / 2;
            mx = (it->first) / 2;
            k-= it->second;

            mp.erase(it); }

        cout << "Case #" << t << ": " << mx << ' ' << mn << '\n'; }

    return 0; }
