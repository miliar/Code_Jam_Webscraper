#include <iostream>
#include <cstdio>
#include <string>
#include <string.h>
#include <queue>
#include <math.h>
#include <cmath>
#include <map>
#include <set>
#include <vector>
#include <algorithm>
#include <bitset>
#include <list>
#include <ctype.h>
#include <cassert>
#include <stack>
#include <fstream>
#include <unordered_map>
#include <unordered_set>
#include <ctime>
#include <functional>
#include <ctime>
#include <limits>
#include <tuple>
#include <complex>
#include <numeric>
#include <future>

using namespace std;

#define snd second
#define fst first
#define mp make_pair
#define ll long long
#define ull unsigned long long
#define ld long double
#define pb push_back
#define left _left
#define right _right

const ld pi = acos(-1.0);

template<typename T>
T abs(T x) {
    return x > 0 ? x : -x;
}

template<typename T>
T sqr(T x) {
    return x * x;
}

template<typename T>
bool chmin(T &x, T y) {
    if (x > y) {
        x = y;
        return true;
    }
    return false;
}

template<typename T>
bool chmax(T &x, T y) {
    if (x < y) {
        x = y;
        return true;
    }
    return false;
}

template<typename U, typename V>
ostream &operator<<(ostream &s, const pair<U, V> &x) {
    s << "(" << x.fst << ", " << x.snd << ")";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const vector<U> &x) {
    s << "[";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "]";
    return s;
}

template<typename U>
ostream &operator<<(ostream &s, const set<U> &x) {
    s << "{";
    bool was = false;
    for (auto it : x) {
        if (was) {
            s << ", ";
        }
        was = true;
        s << it;
    }
    s << "}";
    return s;
}

template<int sz>
ostream operator<<(ostream &s, const bitset<sz> &x) {
    for (int i = 0; i < sz; i++) {
        s << x[i];
    }
    return s;
}


//--------------------------------------------------------------------------

const int maxn = 105;
const ll inf = 1e18;
ll e[maxn], d[maxn];
ll g[maxn][maxn];
ld g2[maxn][maxn];

int main() {

    srand(0);

#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#else
    //freopen("brackets.in", "r", stdin);
    //freopen("brackets.out", "w", stdout);
#endif

    int t;
    cin >> t;
    cout.precision(10);
    for (int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ":";
        int n, q;
        cin >> n >> q;
        for (int i = 1; i <= n; i++) {
            cin >> e[i] >> d[i];
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                cin >> g[i][j];
                if (g[i][j] == -1) {
                    g[i][j] = inf;
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for (int h = 1; h <= n; h++) {
                    chmin(g[j][h], g[j][i] + g[i][h]);
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                g2[i][j] = inf;
            }

            for (int j = 1; j <= n; j++) {
                if (g[i][j] <= e[i]) {
                    g2[i][j] = g[i][j] * 1. / d[i];
                }
            }
        }

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                for (int h = 1; h <= n; h++) {
                    chmin(g2[j][h], g2[j][i] + g2[i][h]);
                }
            }
        }

        for (int i = 0; i < q; i++) {
            int u, v;
            cin >> u >> v;
            cout << fixed << " " << g2[u][v];
        }
        cout << endl;
    }


    return 0;
}
