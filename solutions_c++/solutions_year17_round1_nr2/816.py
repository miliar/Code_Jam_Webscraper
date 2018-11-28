#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdlib>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <vector>
using namespace std;
typedef vector<int> vi; typedef vector<vector<int>> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in("b.in");
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("b.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

struct max_matching {
    max_matching(vvi const & c) : c(c), left(c.size(), -1), right(c[0].size(), -1), size(0) {
        for (bool t = true; t; ) {
            mark = vi(c[0].size());
            t = false;
            for (int i = 0, n = c.size(); i < n; ++i) if (left[i] == -1)
                if (search(i))
                    size++, t = true;
        }
    }

    bool search(int k) {
        for (int i = 0, n = c[0].size(); i < n; ++i) if (c[k][i] && !mark[i]) {
            mark[i] = true;
            if (right[i] == -1 || search(right[i])) {
                right[i] = k; left[k] = i;
                return true;
            }
        }

        return false;
    }

    vvi const & c;
    vi mark, left, right;
    int size;
};


int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 1; test <= ntests; ++test) {        
        int n, p; in >> n >> p;
        vi r(n);
        for (int & x : r) in >> x;
        vvi q(n, vi(p));
        for (vi & v : q)
            for (int & x : v)
                in >> x;
        int res = 0;
        if (n == 1) {            
            for (int i = 0; i < p; ++i) {
                int x = q[0][i] / r[0];
                if (x > 0 && 10 * q[0][i] >= 9 * x * r[0] && 10 * q[0][i] <= 11 * x * r[0]) {
                    ++res;
                    continue;
                }
                ++x;
                if (10 * q[0][i] >= 9 * x * r[0] && 10 * q[0][i] <= 11 * x * r[0])
                    ++res;
            }
        } else {
            vector<vector<pii>> w(n, vector<pii>(p));
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j < p; ++j) {
                    int h = 10 * q[i][j] / (9 * r[i]);
                    int l = (10 * q[i][j] - 1) / (11 * r[i]) + 1;
                    w[i][j] = make_pair(l, h);
                }
                sort(all(w[i]));
            }
            vi cur(n);
            for (;;) {
                int l = 0, h = 1e9;
                int minh;
                for (int i = 0; i < n; ++i) {
                    if (cur[i] >= p) goto done;
                    l = max(l, w[i][cur[i]].first);
                    if (h > w[i][cur[i]].second) {
                        h = w[i][cur[i]].second;
                        minh = i;
                    }
                }
                if (l <= h) {
                    ++res;
                    for (int i = 0; i < n; ++i)
                        ++cur[i];
                } else
                    ++cur[minh];
            }            
        }
        done: out << "Case #" << test << ": " << res << '\n';
    }
    return 0;
}
