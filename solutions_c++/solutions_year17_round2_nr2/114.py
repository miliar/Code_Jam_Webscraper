#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <iostream>
#include <cassert>
#include <cmath>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <cstdlib>

using namespace std;

#define TASKNAME ""

void solve(int test_number);

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    cout.setf(ios::fixed);
    cout.precision(9);
    cerr.setf(ios::fixed);
    cerr.precision(3);
#ifdef LOCAL
    freopen("test.in", "r", stdin);
    freopen("test.out", "w", stdout);
#else
#endif
    int n = 1;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        solve(i);
    }
}

const int MAX_N = 1005; // TODO

int n;
int r, o, y, g, b, v;

void read_input() {
    cin >> n;
    cin >> r >> o >> y >> g >> b >> v;
}

void init() {
    // memset(a, -1, sizeof(a));
}

void output(int test_number) {
    cout << "Case #" << test_number << ": ";
}

string replace(string s, char c, string rep) {
    for (int i = 0; i < s.size(); i++) {
        if (s[i] == c) {
            return s.substr(0, i) + rep + s.substr(i + 1);
        }
    }
    return s;
}

string solve(int r, int b, int y) {
    char col[4] = "RBY";
    pair<int, int> c[3] = {make_pair(r, 0), make_pair(b, 1), make_pair(y, 2)};
    sort(c, c + 3);
    reverse(c, c + 3);
    string s[MAX_N];
    int idx = 0;
    for (int i = 0; i < c[1].first; i++) {
        s[idx] += col[c[1].second];
        idx = (idx + 1) % c[0].first;
    }
    for (int i = 0; i < c[2].first; i++) {
        s[idx] += col[c[2].second];
        idx = (idx + 1) % c[0].first;
    }
    string ans;
    for (int i = 0; i < c[0].first; i++) {
        ans += col[c[0].second];
        ans += s[i];
    }
    for (int i = 0; i < ans.size(); i++) {
        if (ans[i] == ans[(i + 1) % ans.size()]) {
            return "IMPOSSIBLE";
        }
    }
    return ans;
}

void solve(int test_number) {
    read_input();
    init();

    output(test_number);
    if (g > r || o > b || v > y) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if (g && g == r) {
        if (n - g - r) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 0; i < g; i++) {
                cout << "GR";
            }
            cout << endl;
        }
        return;
    }
    if (o && o == b) {
        if (n - o - b) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 0; i < o; i++) {
                cout << "OB";
            }
            cout << endl;
        }
        return;
    }
    if (v && v == y) {
        if (n - y - v) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            for (int i = 0; i < y; i++) {
                cout << "YV";
            }
            cout << endl;
        }
        return;
    }
    r -= g;
    b -= o;
    y -= v;
    string rep_r = "R";
    string rep_b = "B";
    string rep_y = "Y";
    for (int i = 0; i < g; i++) {
        rep_r += "GR";
    }
    for (int i = 0; i < o; i++) {
        rep_b += "OB";
    }
    for (int i= 0; i < v; i++) {
        rep_y += "VY";
    }
    string ans = solve(r, b, y);
    if (ans != "IMPOSSIBLE") {
        ans = replace(ans, 'R', rep_r);
        ans = replace(ans, 'B', rep_b);
        ans = replace(ans, 'Y', rep_y);
    }
    cout << ans << endl;
}
