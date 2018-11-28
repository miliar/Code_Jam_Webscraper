#include <iostream>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <set>
#include <vector>
#include <map>
#include <queue>
#include <string>

using namespace std;

#define DEBUG

int T, k;
string s;

bool isOk(const char c, const int cnt) {
    return (c == '+' && cnt % 2 == 0) || (c == '-' && cnt % 2 == 1);
}

void solve() {
    cin >> s >> k;

    int ans = 0;
    bool imp = false;
    vector <int> cnt(s.size() + 1, 0);

    int curr = 0;
    for (int i = 0; i < s.size(); ++i) {
        curr += cnt[i];

        if (i + k <= s.size()) {
            if (!isOk(s[i], curr)) {
                ++curr;
                ++ans;
                --cnt[i + k];
            }
        } else {
            imp |= !isOk(s[i], curr);
        }
    }

    if (imp) {
        cout << "IMPOSSIBLE";
    } else {
        cout << ans;
    }
}

int main() {
    ios::sync_with_stdio(false);

    #ifdef DEBUG
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    #endif

    cin >> T;

    for (int t = 1; t <= T; ++t) {
        cout << "Case #" << t << ": ";
        solve();
        cout << endl;
    }

    return 0;
}