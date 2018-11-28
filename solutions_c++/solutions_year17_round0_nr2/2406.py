#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <set>

using namespace std;

typedef long long ll;

void solve() {
    string s;
    cin >> s;
    bool fl = true;
    for (int i = 1; i < s.size(); ++i) {
        fl &= s[i - 1] <= s[i];
    }
    if (fl) {
        cout << s << endl;
        return;
    }
    int i;
    for (i = 1; i < s.size(); ++i) {
        if (s[i] < s[i - 1])
            break;
    }
    for (i; i < s.size(); ++i)
        s[i] = s[i - 1];
    if (s.back() == '1') {
        for (int i = 1; i < s.size(); ++i) {
            cout << '9';
        }
        cout << endl;
        return;
    }
    i = s.size() - 1;
    while (i > 0 && s[i - 1] == s[i])
        --i;
    --s[i];
    for (i = i + 1; i < s.size(); ++i)
        s[i] = '9';
    cout << s << endl;
}

int main() {
//    freopen("sum.in", "r", stdin);
//    freopen("sum.out", "w", stdout);
    ios_base::sync_with_stdio(false);
    cout.precision(20);
//    cin.tie(0);
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
}