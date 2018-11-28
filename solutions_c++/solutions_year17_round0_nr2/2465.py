#include <iostream>
#include <vector>
#include <iterator>
#include <sstream>

using namespace std;

void solve() {
    long long x;
    cin >> x;
    ostringstream os;
    os << x;
    string s = os.str();
    auto n = s.size();
    vector<int> v(n);
    for (int i = 0; i < n; i++) {
        v[i] = s[i] - '0';
    }
    int imax = -1;
    for (int i1 = 0; i1 < n; i1++) {
        if (i1 > 0 && v[i1] < v[i1 - 1]) {
            break;
        }
        if (i1 == n - 1 || v[i1 + 1] >= v[i1] + 1) {
            imax = i1;
        }
    }
    int i2 = imax + 1;
    if (i2 < n) {
        v[i2]--;
    }
    for (int i = i2 + 1; i < n; i++) {
        v[i] = 9;
    }
    long long ans = 0;
    for (int i = 0; i < n; i++) {
        ans = ans * 10 + v[i];
    }
    cout << ans << '\n';
}

int main() {
    int ttt;
    cin >> ttt;
    for (int tt = 0; tt < ttt; tt++) {
        cout << "Case #" << tt + 1 << ": ";
        solve();
    }
}