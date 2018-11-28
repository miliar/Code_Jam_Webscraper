#include <iostream>
#include <cstdio>
#include <cassert>
#include <ctime>
#include <cmath>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <iomanip>
#include <numeric>

using namespace std;

#define fst first
#define snd second

#ifdef LOCAL
#define dbg(x) cerr << #x " = " << x << endl;
#include "pretty_print.h"
#else
#define dbg(x)
#endif

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }
template <typename T> T gcd(T a, T b) { return b? gcd(b, a % b) : a; }
template <typename T> bool chmin(T &x, const T& y) { if (x > y) { x = y; return true; } return false; }
template <typename T> bool chmax(T &x, const T& y) { if (x < y) { x = y; return true; } return false; }

int main(int /* argc */, char** /* argv */)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifdef LOCAL
    assert(freopen("inp", "r", stdin));
    assert(freopen("out", "w", stdout));
#endif
    int T;
    cin >> T;
    for (int t = 0; t < T; cout << endl, ++t) {
        cout << "Case #" << t + 1 << ": ";
        int n, m;
        cin >> n >> m;
        vector <int> a(n);
        for (int i = 0; i < n; ++i) {
            cin >> a[i];
        }

        vector <vector <int>> b(n, vector <int> (m));
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                cin >> b[i][j];
            }
            sort(b[i].begin(), b[i].end());
        }

        vector <int> k(n);
        for (int i = 0; i < n; ++i) {
            k[i] = 0;
        }

        int answer = 0;
        bool ok = true;
        const ld EPS = 1e-10;
        while (ok) {
            ll mi, ma, index;
            for (int i = 0; i < n; ++i) {
                ll kmi = b[i][k[i]] / (a[i] * (ld)0.9) + EPS; //  k <= ...
                ll kma = b[i][k[i]] / (a[i] * (ld)1.1) + 1 - EPS; //  ... <= k
                if (i == 0 || kmi < mi) {
                    mi = kmi;
                    index = i;
                }
                if (i == 0 || ma < kma) {
                    ma = kma;
                }
            }
            if (ma <= mi) {
                answer += 1;
                for (int i = 0; i < n; ++i) {
                    ok &= ++k[i] < m;
                }
            } else {
                ok &= ++k[index] < m;
            }
        }
        cout << answer;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
