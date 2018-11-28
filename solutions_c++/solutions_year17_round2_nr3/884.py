#include <cctype>
#include <cerrno>
#include <cfloat>
#include <ciso646>
#include <climits>
#include <clocale>
#include <cmath>
#include <csetjmp>
#include <csignal>
#include <cstdarg>
#include <cstddef>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

// C++
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <exception>
#include <fstream>
#include <functional>
#include <iomanip>
#include <ios>
#include <iosfwd>
#include <iostream>
#include <istream>
#include <iterator>
#include <limits>
#include <list>
#include <locale>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <ostream>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <stdexcept>
#include <streambuf>
#include <string>
#include <typeinfo>
#include <utility>
#include <valarray>
#include <vector>

#include <unordered_set>
#include <unordered_map>

using namespace std;

#define all(c) ((c).begin()), ((c).end())
#define dump(c) cerr << "> " << #c << " = " << (c) << endl;
#define iter(c) __typeof((c).begin())
#define tr(i, c) for (iter(c) i = (c).begin(); i != (c).end(); i++)
#define REP(i, a, b) for (int i = a; i < (int)(b); i++)
#define rep(i, n) REP(i, 0, n)
#define mp make_pair
#define fst first
#define snd second
#define pb push_back
#define debug(fmt, ...) \
        fprintf( stderr, \
                  fmt "\n", \
                  ##__VA_ARGS__ \
        )

typedef unsigned int uint;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<vi> vvi;
typedef vector<long double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

const int INF = 1 << 30;
const double EPS = 1e-10;

double zero(double d) {
    return abs(d) < EPS ? 0.0 : d;
}

template<class T>
bool chmax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
bool chmin(T &a, const T &b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}

#define UNIQUE(v) v.erase( unique(v.begin(), v.end()), v.end() );

template<typename T1, typename T2>
ostream &operator<<(ostream &os, const pair<T1, T2> &p) {
    return os << '(' << p.first << ',' << p.second << ')';
}

template<typename T>
ostream &operator<<(ostream &os, const vector<T> &a) {
    os << '[';
    rep(i, a.size()) os << (i ? " " : "") << a[i];
    return os << ']';
}

string toString(int i) {
    stringstream ss;
    ss << i;
    return ss.str();
}

const int MOD = 1000000007;

// a^k
ll fpow(ll a, ll k, int M) {
    ll res = 1ll;
    ll x = a;
    while (k != 0) {
        if ((k & 1) == 1)
            res = (res * x) % M;
        x = (x * x) % M;
        k >>= 1;
    }
    return res;
}

struct prepare {
    prepare() {
        cout.setf(ios::fixed, ios::floatfield);
        cout.precision(8);
        ios_base::sync_with_stdio(false);
    }
} _prepare;


void solve() {

    const ll INF = 1ll << 50;

    int N, Q;
    cin >> N >> Q;

    vector<pii> hou(N);
    rep(i, N) {
        cin >> hou[i].first >> hou[i].second;
    }

    vi d(N, 0);
    rep(i, N) {
        rep(j, N) {
            int t;
            cin >> t;
            if(i == j - 1) {
                d[i] = t;
            }
        }
    }

    int st = 0, en = N;
    rep(i, Q) {
        int s, e;
        cin >> s >> e;
    }


//    cout << d << endl;

    vll acc(N, 0);
    REP(i, 1, N) {
        acc[i] += d[i-1] + acc[i-1];
    }

//    cout << acc << endl;

    vvd dp(N+1, vd(N+1, INF));
    dp[1][0] = (long double)d[0] / hou[0].second;
    rep(i, N) {
        rep(j, i) {
            if(dp[i][j] == INF)
                continue;

//            cout << "run: "<< acc[i] - acc[j] << endl;
            int remd = hou[j].first - (acc[i] - acc[j]);
//            cout << remd << endl;

            // not change
            if(remd > d[i]) {
                chmin(dp[i+1][j], dp[i][j] + (long double)d[i] / hou[j].second);
            }
            // change
            chmin(dp[i+1][i], dp[i][j] + (long double)d[i] / hou[i].second);
        }
    }

    long double ans = INF;
    rep(i, N) {
        chmin(ans, dp[N][i]);
    }

    cout << ans;
}

int main() {
    int T;
    cin >> T;
    rep(_t, T) {
        cout << "Case #" << (_t + 1) << ": ";
        solve();
        cout << endl;
    }
    return 0;
}

