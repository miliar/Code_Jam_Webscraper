#include <bits/stdc++.h>

using namespace std;
typedef long long li;

void solve() {
    li n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;

    string cs = "RYB";
    li counts[3] = {r, y, b};

    string ans;
    if (max({r, y, b}) > n / 2 and n > 2) {
        ans = "IMPOSSIBLE";
    } else {
        ans = "";
        if (r * y * b) {
            while (n--) {
                bool ok = false;
                auto insert = [&](int pos, int cid) {
                    ans = ans.substr(0, pos) + string(1, cs[cid]) + ans.substr(pos);
                    counts[cid]--;
                    ok = true;
                    return;
                };
                for (int i = 0; i < 3; ++i) {
                    if (not counts[i]) {
                        continue;
                    }
                    if (ans == "") {
                        insert(0, i);
                        goto done;
                    } else {
                        for (int pos = 0; pos < ans.size(); ++pos) {
                            if (ans[pos] != cs[i] and cs[i] != ans[(pos -1 + ans.size()) % ans.size()]) {
                                insert(pos, i);
                                goto done;
                            }
                        }
                    }
                }
                done:
                if (not ok) {
                    ans = "IMPOSSIBLE";
                    break;
                }
            }
        } else {
            for (int i = 0; i < n / 2; ++i) {
                for (int j = 0; j < 3; ++j) {
                    if (counts[j]) {
                        ans.push_back(cs[j]);
                    }
                }
            }
        }
    }

    static int casenum = 1;
    cout.precision(16);
    cout << "Case #" << casenum << ": " << ans << endl;
    casenum += 1;
}

int main() {
    li t;
    cin >> t;
    while (t--) {
        solve();
    }
    return 0;
}