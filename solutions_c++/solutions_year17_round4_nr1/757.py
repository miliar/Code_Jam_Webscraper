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
    for (int t = 0; t < T; ++t ) {
        cout << "Case #" << t + 1 << ": ";
        int n, p;
        cin >> n >> p;
        vector<int> a(p, 0);
        int answer = 0;
        for (int i = 0; i < n; ++i) {
            int x;
            cin >> x;
            a[x % p] += 1;
        }
        if (p == 2) {
            answer = (a[1] + 1) / 2 + a[0];
        } else if (p == 3) {
            int d = min(a[1], a[2]);
            answer = a[0] + d;
            a[1] -= d;
            a[2] -= d;
            answer += (a[1] + a[2] + 2) / 3;
        } else if (p == 4) {
            int d = min(a[1], a[3]);
            const int INF = (int)1e+9 + 42;
            answer = INF;
            a[1] -= d;
            a[3] -= d;
            int x = a[1] + a[3];
            for (int i = 0; 2 * i <= a[2]; ++i) {
                int t = a[2] - i;
                if (2 * x < t) {
                    continue;
                }
                // answer = min(answer, a[0] + d + 
            }
        }
        cout << answer << endl;
    }


    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
