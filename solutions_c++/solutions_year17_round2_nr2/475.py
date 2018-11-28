#include <bits/stdc++.h>
using namespace std;

#define all(x) begin(x), end(x)
#define task "B-small-attempt1"
#define fi first
#define se second

#define BestMistake

typedef long long ll;
typedef long double ld;

const int INF = 0x3c3c3c3c;
const ll LINF = 0x3c3c3c3c3c3c3c3cL;

void solve() {
    int n;

    string colors = "ROYGBV";
    cin >> n;

    vector<int> a(7);
    for (int i = 0; i < 6; i++) {
        cin >> a[i];
    }
    for (int i = 1; i < 6; i += 2) {
    //    assert(!a[i]);
    }
    int mx = *max_element(begin(a), end(a));
    if (mx * 2 > n) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    string ans;
    int prev = 6;
    for (int i = 0; i < n; i++) {
        int x = a[prev];
        a[prev] = 0;
        int mx_i = max_element(begin(a), end(a)) - begin(a);
        a[prev] = x;
        ans.push_back(colors[mx_i]);
        assert(a[mx_i]);
        a[mx_i]--;
        prev = mx_i;
    }
    if (ans[n - 1] == ans[0]) {
        swap(ans[n - 1], ans[n - 2]);
    }
    cout << ans << endl;
    for (int i = 0; i < n; i++) {
        assert(ans[i] != ans[(i + 1) % n]);
    }


}

int main() {
#ifdef BestMistake
    freopen(task".in", "r", stdin);
    freopen(task".out", "w", stdout);
#endif
    cin.tie(0);
    int tests;
    cin >> tests;
    for (int test = 1; test <= tests; test++) {
        cout << "Case #" << test << ": ";
        solve();
    }
    return 0;
}