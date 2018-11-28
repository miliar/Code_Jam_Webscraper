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
    int k, n;
    cin >> s >> k;
    n = s.size();
    vector<int> v(n + 1);
    bool fl = false;
    int cnt = 0;
    for (int i = 0; i < n - k + 1; ++i) {
        fl ^= v[i];
        if ((s[i] == '-') ^ fl) {
            v[i + k] ^= true;
            fl ^= true;
            ++cnt;
        }
    }
    for (int i = n - k + 1; i < n; ++i) {
        fl ^= v[i];
        if ((s[i] == '-') ^ fl) {
            cnt = -1;
        }
    }
    if (cnt == -1) {
        cout << "IMPOSSIBLE\n";
    } else {
        cout << cnt << endl;
    }
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