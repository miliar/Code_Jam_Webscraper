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

const int MAXX = 101;
const ll INF = (ll)1e+18;

ll f[MAXX][MAXX][MAXX][MAXX];

ll get(ll hd, ll ad, ll hk, ll ak, ll b, ll d, ll h) {
    if (hd <= 0) {
        return INF;
    }
    if (ad >= hk) {
        return 1;
    }
    ll& result = f[hd][ad][hk][ak];
    if (result != 0) {
        return result;
    }
    result = INF;
    ll opt = INF;
    chmin(opt, get(hd - ak, ad, hk - ad, ak, b, d, h) + 1);
    chmin(opt, get(hd - ak, ad + b, hk, ak, b, d, h) + 1);
    chmin(opt, get(h - ak, ad, hk, ak, b, d, h) + 1);
    chmin(opt, get(min(hd, hd - ak + d), ad, hk, max(0LL, ak - d), b, d, h) + 1);
    result = opt;
    // cout << " " << hd << " " << ad << " " << hk << " " << ak << " " << b << " " << d << " = " << result << endl;
    return result;
}

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
        ll hd, ad, hk, ak, b, d;
        cin >> hd >> ad >> hk >> ak >> b >> d;
        memset(f, 0, sizeof(f));
        ll result = get(hd, ad, hk, ak, b, d, hd);
        if (result >= INF) {
            cout << "IMPOSSIBLE";
        } else {
            cout << result;
        }
    }

    cerr << "Time execute: " << clock() / (double)CLOCKS_PER_SEC << " sec" << endl;
    return 0;
}
