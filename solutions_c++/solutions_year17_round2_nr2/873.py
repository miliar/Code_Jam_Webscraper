#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>
#include <queue>
#include <iomanip>
#include <set>
#include <cmath>
#include <map>

using namespace std;

typedef long long ll;

void hnd(int a, int b, char f, char s) {
    if (a != b) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    for (int i = 0; i < a; ++i) {
        cout << f << s;
    }
    cout << endl;
    return;
}

void ins(vector<char>& s, int b, char ft,  char sc) {
    vector<char> t(b * 2);
    for (int i = 0; i < b; ++i)
        t[2 * i] = ft, t[2 * i + 1] = sc;
    for (int i = 0; i < s.size(); ++i) {
        if (s[i] == sc)
        {
            s.insert(s.begin() + i + 1, t.begin(), t.end());
            return;
        }
    }
}

void solve() {
    int n, r, o, y, g, b, v;
    cin >> n >> r >> o >> y >> g >> b >> v;
    if (n == o + b) {
        hnd(o, b, 'O', 'B');
        return;
    }
    if (n == g + r) {
        hnd(g, r, 'G', 'R');
        return;
    }
    if (n == v + y) {
        hnd(v, y, 'V', 'Y');
        return;
    }
    if (o > 0 && o >= b || g > 0 && g >= r || v > 0 && v >= y) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    vector<pair<int, char> > p;
    p.push_back({r - g, 'R'});
    p.push_back({y - v, 'Y'});
    p.push_back({b - o, 'B'});
    sort(p.rbegin(), p.rend());
    if (p[0].first > p[1].first + p[2].first) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    int n1 = n - 2 * g - 2 * v - 2 * o;
    vector<char> s(n1, '*');
    int i;
    for (i = 0; i < 2 * p[0].first; i += 2) {
        s[i] = p[0].second;
    }
    int cnt = 0;
    --i;
    for (i; i < n1 && cnt < p[1].first; i += 2) {
        s[i] = p[1].second;
        ++cnt;
    }
    i = 1;
    for (i; i < n1 && cnt < p[1].first; i += 2) {
        s[i] = p[1].second;
        ++cnt;
    }
    for (int i = 0; i < n1; ++i) {
        if (s[i] == '*')
            s[i] = p[2].second;
    }
//    for (int i = 0; i < s.size(); ++i) {
//        cout << s[i];
//    }
//    cout << endl;
    ins(s, g, 'G', 'R');
    ins(s, v, 'V', 'Y');
    ins(s, o, 'O', 'B');
    for (int i = 0; i < s.size(); ++i) {
        cout << s[i];
    }
    cout << endl;
}

int main() {
    iostream::sync_with_stdio(false);
    cout.precision(20);
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i)
        cout << "Case #" << i << ": ", solve();
}

