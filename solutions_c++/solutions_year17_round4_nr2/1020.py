#include <algorithm>
#include <iostream>
#include <cmath>
#include <vector>
#include <map>
#include <cassert>
#include <string>
using namespace std;

#define forn(i, n) for (int i = 0; i < int(n); ++i)
#define forv(i, v) forn(i, (v).size())
#define all(v) v.begin(), v.end()
#define pb push_back
#define mp make_pair


pair<int, int> findRides(int n, const vector<int>& a, const vector<int>& b) {
    if (n == 1) {
        return mp(a.size() + b.size(), 0);
    }
    vector<pair<int, int>> c;
    forn(i, max(a.size(), b.size())) {
        pair<int, int> p(i < a.size() ? a[i] : 0, i < b.size() ? b[i] : 0);
        c.pb(p);
    }
    while (true) {
        int i = 0;
        while (i < c.size() && c[i].first != c[i].second) ++i;
        if (i == c.size()) break;
        int j = 0;
        while (j < c.size()) {
            if (c[i].first != c[j].first && c[i].first != c[j].second) {
                swap(c[i].first, c[j].first);
                break;
            }
            ++j;
        }
        if (j == c.size()) break;
    }
    int nr = c.size();
    int np = 0;
    for (const auto p : c) {
        if (p.first == p.second) {
            if (p.first == 1) ++nr;
            else ++np;
        }
    }
    return mp(nr, np);
}

int main() {
    ios_base::sync_with_stdio(false);
    int numTests;
    cin >> numTests;
    //cout.precision(10);
    //cout << fixed;
    forn(tId, numTests) {
        cerr << tId << endl;
        int n, c, m;
        cin >> n >> c >> m;
        vector<int> a, b;
        forn(i, m) {
            int p, id;
            cin >> p >> id;
            if (id == 1) a.pb(p);
            else b.pb(p);
        }
        auto ans = findRides(n, a, b);
        cout << "Case #" << tId + 1 << ": " << ans.first << " " << ans.second << endl;
    }
    return 0;
}
