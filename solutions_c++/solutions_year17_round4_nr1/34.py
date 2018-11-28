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
int p;
const int maxn = 105;
const int inf = 1e9;
int dp[maxn][maxn][maxn][4];

int rec(int a, int b, int c, int m) {
    if (dp[a][b][c][m] != inf) {
        return dp[a][b][c][m];
    }
    int res = 0;
    if (a) {
        chmax(res, rec(a - 1, b, c, (m + 1) % p) + !m);
    }

    if (b) {
        chmax(res, rec(a, b - 1, c, (m + 2) % p) + !m);
    }

    if (c) {
        chmax(res, rec(a, b, c - 1, (m + 3) % p) + !m);
    }

    return dp[a][b][c][m] = res;
}

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
    for (int tt = 1; tt <= t; tt++) {
        cout << "Case #" << tt << ": ";
        int n;
        cin >> n >> p;
        vector<int> cnt(4);
        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            cnt[x % p]++;
        }

        for (int i = 0; i <= cnt[1]; i++) {
            for (int j = 0; j <= cnt[2]; j++) {
                for (int h = 0; h <= cnt[3]; h++) {
                    for (int k = 0; k < 4; k++) {
                        dp[i][j][h][k] = inf;
                    }
                }
            }
        }

        cout << cnt[0] + rec(cnt[1], cnt[2], cnt[3], 0) << endl;



    }

    return 0;
}