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

int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n, c, m;
        in >> n >> c >> m;
        vvi v(c, vi(n));
        for (int i = 0; i < m; ++i) {
            int p, b;
            in >> p >> b;
            --p; --b;
            v[b][p]++;
        }
        int res = 0, prom = 0;
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < v[0][i]; ++j) {
                ++res;
                bool found = false;
                for (int k = i + 1; k < n; ++k) {
                    if (v[1][k]) {
                        found = true;
                        --v[1][k];
                        break;
                    }
                }
                if (found) continue;
                for (int k = 0; k < i; ++k) {
                    if (v[1][k]) {
                        found = true;
                        --v[1][k];
                        break;
                    }
                }
                if (!found && v[1][i]) {
                    if (i) {
                        prom++;
                        v[1][i]--;
                    }
                }
            }
        }
        for (int i = 0; i < n; ++i)
            res += v[1][i];
        out << "Case #" << test << ": " << res << ' ' << prom << '\n';
    }
    return 0;
}
