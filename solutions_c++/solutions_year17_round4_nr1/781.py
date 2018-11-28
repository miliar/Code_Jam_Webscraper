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
#pragma warning(disable : 4244 4267 4018 4996 4800)
//#pragma comment( linker, "/stack:10000000" )
using namespace std; 
typedef vector<int> vi; typedef vector<vi> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in( "a.in" );
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("a.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n, p; in >> n >> p;
        vi g(n); read(g);
        vi r(p);
        for (auto x : g)
            r[x % p]++;
        int res = 0;
        if (p == 2) {
            res = r[0] + (r[1] + 1) / 2;
        }
        else if (p == 3) {
            int t = min(r[1], r[2]);
            int cur = r[0] + t;
            int x = 0;
            for (int j = 0; j < r[1] - t; ++j) {
                if (x == 0) ++cur;
                x = (x + 1) % 3;
            }
            for (int j = 0; j < r[2] - t; ++j) {
                if (x == 0) ++cur;
                x = (x + 2) % 3;
            }
            res = max(res, cur);
        }
        else {
            int t = min(r[1], r[3]);
            int cur = r[0] + t + (r[2] + 1) / 2;
            int x = (r[2] & 1) ? 2 : 0;
            for (int j = 0; j < r[1] - t; ++j) {
                if (x == 0) ++cur;
                x = (x + 1) % 4;
            }
            for (int j = 0; j < r[3] - t; ++j) {
                if (x == 0) ++cur;
                x = (x + 3) % 4;
            }
            res = max(res, cur);
        }
        out << "Case #" << test << ": " << res << '\n';
    }
    return 0;
}
