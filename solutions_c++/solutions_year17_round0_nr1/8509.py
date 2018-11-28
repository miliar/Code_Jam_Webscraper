#include <bits/stdc++.h>
using namespace std;
#define int long long
int32_t main() {
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; tt++) {
        string s;
        int k;
        cin >> s;
        cin >> k;
        s = "+" + s + "+";
        //012345678
        //++-+-+---
        int res = 0;
        bool possible = true;
        for (int i = 0; i < k; i++) {
            bool up = false;
            int cnt = 0;
            for (int j = i; j < s.size() - 1; j+=k) {
                if (up) {
                    if (s[j] != s[j+1]) {
                        up = false;
                        res += cnt;
                    } else {
                        cnt++;
                    }
                } else {
                    if (s[j] != s[j+1]) {
                        up = true;
                        cnt = 1;
                    }
                }
            }
            if (up) possible = false;
        }
        cout << "Case #" << tt << ": ";
        if (possible) cout << res << "\n";
        else cout << "IMPOSSIBLE\n";
    }
}
