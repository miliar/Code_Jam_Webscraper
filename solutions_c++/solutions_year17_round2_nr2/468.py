#include <bits/stdc++.h>

using namespace std;

string f(int a, int n, int R, int Y, int B) {
    int b = B - Y + a;
    int c = R - a - b;
    if (b < 0 || c < 0 || c + 2 * R > n || (n - c) % 2 == 1) {
        return "";
    }
    string s;
    for (int i = 0; i < a; ++i) {
        s += "RY";
    }
    for (int i = 0; i < b; ++i) {
        s += "RB";
    }
    for (int i = 0; i < c; ++i) {
        s += "RBY";
    }
    while (s.size() < n) {
        if (s.empty() || s.back() == 'Y') s += "BY";
        else s += "YB";
    }
    assert(s.size() <= n);
    return s;
}

void solve(int test) {
    cout << "Case #" << test << ": ";
    int n, R, OO, Y, GG, B, VV;
    cin >> n >> R >> OO >> Y >> GG >> B >> VV;
    for (int i = 0; i <= n; ++i) {
        string s = f(i, n, R, Y, B);
        if (!s.empty()) {
            cout << s << '\n';
            return;
        }
    }
    cout << "IMPOSSIBLE\n";
}

signed main() {
    ios_base::sync_with_stdio(false); cin.tie(0);
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        solve(i);
    }
}
