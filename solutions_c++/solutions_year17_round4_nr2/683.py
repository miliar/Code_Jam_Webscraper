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

const int INF = (int)1e+9 + 42;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;

template <typename T> T sqr(T x) { return x * x; }
template <typename T> T abs(T x) { return x < 0? -x : x; }
template <typename T> T gcd(T a, T b) { return b? gcd(b, a % b) : a; }
template <typename T> bool chmin(T &x, const T& y) { if (x > y) { x = y; return true; } return false; }
template <typename T> bool chmax(T &x, const T& y) { if (x < y) { x = y; return true; } return false; }

vector<int> counter;
vector<int> position;

const int MAXN = 1002;
int f[MAXN][MAXN];

int n, c, m, S, T;

int main(int /* argc */, char** /* argv */)
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
#ifdef LOCAL
    assert(freopen("inp", "r", stdin));
    assert(freopen("out", "w", stdout));
#endif
    int tests;
    cin >> tests;
    for (int t = 0; t < tests; ++t, cout << endl) {
        cout << "Case #" << t + 1 << ": ";
        cin >> n >> c >> m;
        position.resize(n);
        for (int i = 0; i < n; ++i) {
            position[i] = 0;
        }
        counter.resize(c);
        for (int i = 0; i < c; ++i) {
            counter[i] = 0;
        }
        for (int i = 0; i < m; ++i) {
            int p, b;
            cin >> p >> b;
            --p;
            --b;
            counter[b] += 1;
            position[p] += 1;
        }
        int answer = *max_element(counter.begin(), counter.end());
        int s = 0;
        for (int i = 0; i < n; ++i) {
            s += position[i];
            answer = max(answer, (s + i) / (i + 1));
        }
        int cost = 0;
        for (int i = 0; i < n; ++i) {
            cost += max(0, position[i] - answer);
        }
        cout << answer << " " << cost;
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
