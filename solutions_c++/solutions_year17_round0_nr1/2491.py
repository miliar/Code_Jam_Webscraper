#include <iostream>
#include <vector>
#include <iterator>

using namespace std;

int makeShell(vector<bool> &v, int &iBegin, int k) {
    size_t n = v.size();
    while (iBegin < n && v[iBegin]) {
        iBegin++;
    }
    if (iBegin == n) {
        return 1;
    }
    if (n - iBegin < k) {
        return 0;
    }
    for (int j = iBegin; j - iBegin < k; j++) {
        v[j] = !v[j];
    }
    return 2;
}

void solve() {
    size_t s;
    string str;
    cin >> str;
    s = str.size();
    vector<bool> v(s);
    for (int i = 0; i < s; i++) {
        v[i] = str[i] == '+';
    }
    int k;
    cin >> k;
    int id = 0;
    int ret;
    int ans = 0;
    while ((ret = makeShell(v, id, k)) != 1) {
        ans++;
        if (ret == 0) {
            cout << "IMPOSSIBLE" << "\n";
            return;
        }
    }
    cout << ans << "\n";
}

int main() {
    int ttt;
    cin >> ttt;
    for (int tt = 0; tt < ttt; tt++) {
        cout << "Case #" << tt + 1 << ": ";
        solve();
    }
}