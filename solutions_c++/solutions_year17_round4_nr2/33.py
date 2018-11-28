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
ll foo(int n, int x, vector<ll> a) {
    vector<ll> cnt(n);
    for (auto x : a) {
        assert(x < n && 0 <= x);
        cnt[x]++;
    }

    ll ans = 0;
    int c = 0;
    for (int i = n - 1; i >= 0; i--) {
        if (cnt[i] > x) {
            ans += cnt[i] - x;
            c += cnt[i] - x;
        } else {
            c -= min<int>(c, x - cnt[i]);
        }
    }
    if (c) {
        return -1;
    } else {
        return ans;
    }
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

        int n, m, c;
        cin >> n >> c >> m;

        map<int,int> cnt;
        vector<ll> a;
        int lo = 0;
        for (int i = 0; i < m; i++) {
            int x, b;
            cin >> x >> b;
            x--;
            a.pb(x);
            cnt[b]++;
            chmax(lo, cnt[b]);
        }
        lo--;

        int hi = m + 1;
        assert(foo(n, hi, a) != -1);
        while (hi - lo > 1) {
            int mid = (lo + hi) >> 1;
            if (foo(n, mid, a) != -1) {
                hi = mid;
            } else {
                lo = mid;
            }
        }

        cout << hi << " " << foo(n, hi, a) << endl;
    }

    return 0;
}