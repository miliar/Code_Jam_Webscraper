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
        string s;
        cin >> s;
        int n = s.size();
        for (int i = 0; i + 1 < n; ++i) {
            if (s[i] > s[i + 1]) {
                while (i && s[i - 1] == s[i]) {
                    --i;
                }
                for (s[i++]--; i < n; ++i) {
                    s[i] = '9';
                }
                break;
            }
        }
        if (s[0] == '0') {
            s.erase(s.begin());
        }
        cout << s;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
