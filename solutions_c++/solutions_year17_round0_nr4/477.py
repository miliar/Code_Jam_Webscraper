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
#pragma warning( disable : 4244 4267 4018 4996 4800 )
//#pragma comment( linker, "/stack:10000000" )
using namespace std;
typedef vector<int> vi; typedef vector<vector<int>> vvi; typedef vector<string> vs; typedef vector<double> vd;
typedef vector<vd> vvd; typedef long long ll; typedef vector<ll> vll; typedef vector<vll> vvll; typedef pair<int, int> pii;
#define all(v) begin(v), end(v)

#ifdef LOCAL
ifstream in("d.in");
#else
istream & in = cin;
#endif
//ostream & out = cout;
ofstream out("d.out");
template <class T> void read(T & t) { for (auto & x : t) in >> x; } template <class T> int sz(T const & t) { return (int)t.size(); }

int code(char ch)
{
    switch (ch) {
    case '+': return 1;
    case 'x': return 2;
    case 'o': return 3;
    }
}

char symbol(int code)
{
    switch (code) {
    case 1: return '+';
    case 2: return 'x';
    case 3: return 'o';
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    int ntests; in >> ntests;
    for (int test = 1; test <= ntests; ++test) {
        int n, m; in >> n >> m;
        vvi v(n, vi(n));
        vi row_used(n), col_used(n), d1_used(2 * n - 1), d2_used(2 * n - 1);
        for (int i = 0; i < m; ++i) {
            char ch; int r, c;
            in >> ch >> r >> c;
            --r; --c;
            v[r][c] = code(ch);
            if (v[r][c] & 2) {
                row_used[r] = 1;
                col_used[c] = 1;
            }
            if (v[r][c] & 1) {
                d1_used[r + c] = 1;
                d2_used[r - c + n - 1] = 1;
            }
        }
        vvi vv = v;
        int r =  0;
        for (int c = 0; c < n; ++c) {
            if (!d1_used[r + c] && !d2_used[r - c + n - 1]) {
                vv[r][c] |= 1;
                d1_used[r + c] = 1;
                d2_used[r - c + n - 1] = 1;
            }
            if (!row_used[r] && !col_used[c]) {
                vv[r][c] |= 2;
                row_used[r] = 1;
                col_used[c] = 1;
            }
        }
        for (r = n - 1; r >= 0; --r) {
            for (int c = 0; c < n; ++c) {
                if (!d1_used[r + c] && !d2_used[r - c + n - 1]) {
                    vv[r][c] |= 1;
                    d1_used[r + c] = 1;
                    d2_used[r - c + n - 1] = 1;
                }
                if (!row_used[r] && !col_used[c]) {
                    vv[r][c] |= 2;
                    row_used[r] = 1;
                    col_used[c] = 1;
                }
            }
        }
        int res = 0, cnt = 0;
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {
                res += bool(vv[r][c] & 1) + bool(vv[r][c] & 2);
                if (vv[r][c] != v[r][c])
                    ++cnt;
            }
        }
        out << "Case #" << test << ": " << res << ' ' << cnt << '\n';
        for (int r = 0; r < n; ++r) {
            for (int c = 0; c < n; ++c) {                
                if (vv[r][c] != v[r][c]) {
                    out << symbol(vv[r][c]) << ' ' << r + 1 << ' ' << c + 1 << '\n';
                }
            }
        }
    }
    return 0;
}
