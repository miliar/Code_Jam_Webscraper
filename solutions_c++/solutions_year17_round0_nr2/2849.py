#include <bits/stdc++.h>

using namespace std;

string solve(string s) {
    string ans;
    for (int cur = 0; cur < s.size(); ++cur) {
        if (cur == 0 || s[cur] > s[cur - 1]) {
            ans = s;
            ans[cur]--;
            fill(ans.begin() + cur + 1, ans.end(), '9');
    //        cout << ans << "\n";
        }
        if (cur + 1 == s.size()) {
            ans = s;
        }
        if (!(cur + 1 < s.size() && s[cur + 1] >= s[cur])) {
            break;
        }
    }
    if (ans.front() == '0') {
        ans.erase(ans.begin());
    }
    return ans;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int tt = 1; tt <= t; ++tt) {
        string n;
        cin >> n;
        cout << "Case #" << tt << ": " << solve(n) << "\n";
    }
    return 0;
}
