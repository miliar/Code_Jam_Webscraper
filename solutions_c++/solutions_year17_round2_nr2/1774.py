#include <bits/stdc++.h>

using namespace std;

const long double inf = 1e18;

void solve() {
    int n;
    cin >> n;
    int r, o, y, g, b, v;
    cin >> r >> o >> y >> g >> b >> v;
    pair<int, char> a[3] = {{r, 'R'}, {y, 'Y'}, {b, 'B'}};
    sort(a, a + 3);
    string s1 = "";
    for (int i = 0; i < a[1].first; ++i) {
        s1 += a[1].second;
        if (i < a[0].first)
            s1 += a[0].second;
    }
    string s2 = "";
    reverse(s1.begin(), s1.end());
    for (int i = 0; i < max(a[2].first, (int)s1.size()); ++i) {
        if (i < a[2].first)
            s2 += a[2].second;
        if (i < s1.size())
            s2 += s1[i];
    }
    bool ok = true;
    for (int i = 0; i < s2.size(); ++i) {
        char nxt = (i + 1 == s2.size())? s2[0] : s2[i + 1];
        if (s2[i] == nxt)
            ok = false;
    }
    if (ok)
        cout << s2;
    else cout << "IMPOSSIBLE";

}

int main() {
#ifdef __APPLE__
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif

    int t = 1;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cerr << "Case #" << i << " is working\n";
        cout << "Case #" << i << ": ";
        solve();
        cout << "\n";
        cerr << "Case #" << i << " is done\n";
    }

    return 0;
}

