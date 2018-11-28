/* string coder = "Balajiganapathi S"; // Never give up!  */

//#define LOCAL
#ifdef LOCAL
#   define TRACE
//#   define TEST
#else
#   define NDEBUG
//#   define FAST
#endif

#include<bits/stdc++.h>

using namespace std;

/* aliases */
using vi  = vector<int>;
using pi  = pair<int, int>;
using ll  = long long int;

/* shortcut macros */
#define mp              make_pair
#define fi              first
#define se              second
#define mt              make_tuple
#define gt(t, i)        get<i>(t)
#define all(x)          (x).begin(), (x).end()
#define ini(a, v)       memset(a, v, sizeof(a))
#define rep(i, s, n)    for(int i = (s), _##i = (n); i <= _##i; ++i)
#define re(i, s, n)     rep(i, (s), (n) - 1)
#define fo(i, n)        re(i, 0, n)
#define si(x)           (int((x).size()))
#define is1(mask,i)     (((mask) >> i) & 1)

/* trace macro */
#ifdef TRACE
#   define trace(v...)  {cerr << __func__ << ":" << __LINE__ << ": " ;_dt(#v, v);}
#else
#   define trace(...)
#endif

#ifdef TRACE
pi _gp(string s) {
    pi r(0, si(s) - 1);
    int p = 0, s1 = 0, s2 = 0, start = 1;
    fo(i, si(s)) {
        int x = (s1 | s2);
        if(s[i] == ' ' && start) {
            ++r.fi;
        } else {
            start = 0;
            if(s[i] == ',' && !p && !x) {
                r.se = i - 1;
                return r;
            }
            if(x && s[i] == '\\') ++i;
            else if(!x && s[i] == '(') ++p;
            else if(!x && s[i] == ')') --p;
            else if(!s2 && s[i] == '\'') s1 ^= 1;
            else if(!s1 && s[i] == '"') s2 ^= 1;
        }
    }
    return r;
}

template<typename H> void _dt(string u, H&& v) {
    pi p = _gp(u);
    cerr << u.substr(p.fi, p.se - p.fi + 1) << " = " << forward<H>(v) << " |" << endl;
}

template<typename H, typename ...T> void _dt(string u, H&& v, T&&... r) {
    pi p = _gp(u);
    cerr << u.substr(p.fi, p.se - p.fi + 1) << " = " << forward<H>(v) << " | ";
    _dt(u.substr(p.se + 2), forward<T>(r)...);
}

template<typename T> 
ostream &operator <<(ostream &o, vector<T> v) { // print a vector
    o << "[";
    fo(i, si(v) - 1) o << v[i] << ", ";
    if(si(v)) o << v.back();
    o << "]";
    return o;
}

template<typename T1, typename T2> 
ostream &operator <<(ostream &o, map<T1, T2> m) { // print a map
    o << "{";
    for(auto &p: m) {
        o << " (" << p.fi << " -> " << p.se << ")";
    }
    o << " }";
    return o;
}

template<typename T> 
ostream &operator <<(ostream &o, set<T> s) { // print a set
    o << "{";
    bool first = true;
    for(auto &entry: s) {
        if(!first) o << ", ";
         
        o << entry;
        first = false;
    }
    o << "}";
    return o;
}

template <size_t n, typename... T>
typename enable_if<(n >= sizeof...(T))>::type
    print_tuple(ostream&, const tuple<T...>&) {} 

template <size_t n, typename... T>
typename enable_if<(n < sizeof...(T))>::type
    print_tuple(ostream& os, const tuple<T...>& tup) {
    if (n != 0)
        os << ", ";
    os << get<n>(tup);
    print_tuple<n+1>(os, tup);
}

template <typename... T>
ostream& operator<<(ostream& os, const tuple<T...>& tup) { // print a tuple
    os << "("; print_tuple<0>(os, tup); return os << ")"; } template <typename T1, typename T2>
ostream& operator<<(ostream& os, const pair<T1, T2>& p) { // print a pair
    return os << "(" << p.fi << ", " << p.se << ")";
}
#endif
    
/* util functions */
template<typename T1, typename T2, typename T3>
T1 modpow(T1 _a, T2 p, T3 mod) {
    assert(p >= 0);
    ll ret = 1, a = _a;

#ifndef FAST
    if(a < 0) {
        a %= mod;
        a += mod;
    } 

    if(a >= mod) {
        a %= mod;
    }
#endif

    for(; p > 0; p /= 2) {
        if(p & 1) ret = ret * a % mod;
        a = a * a % mod;
    }

    return ret;
}

#define x1 _asdfzx1
#define y1 _ysfdzy1

/* constants */
constexpr int dx[] = {-1, 0, 1, 0, 1, 1, -1, -1};
constexpr int dy[] = {0, -1, 0, 1, 1, -1, 1, -1};
constexpr auto PI  = 3.14159265358979323846L;
constexpr auto oo  = numeric_limits<int>::max() / 2 - 2;
constexpr auto eps = 1e-6;
constexpr auto mod = 1000000007;

/* code */
constexpr int mx_n = 102, mx_p = 4, mx_t = 102;
int p, n, g[mx_n];
int dp[mx_p][mx_n][mx_n][mx_n][mx_n];
//int vis[mx_p][mx_n][mx_n][mx_n][mx_n], mark;
int cnt[mx_p];

int solve(int r, int g0, int g1, int g2, int g3) {
    if(g0 + g1 + g2 + g3 == 0) return 0;
    int &ret = dp[r][g0][g1][g2][g3];
    if(ret != -1) return ret;
    //if(vis[r][g0][g1][g2][g3] == mark) return ret;
    //vis[r][g0][g1][g2][g3] = mark;
    ret = 0;

    int g[] = {g0, g1, g2, g3};
    fo(i, p) if(g[i]) {
        --g[i];
        int nr = (r - i + p) % p;
        ret = max(ret, (r == 0? 1: 0) + solve(nr, g[0], g[1], g[2], g[3]));
        ++g[i];
    }
    //trace(r, g0, g1, g2, g3, ret);

    return ret;
}

tuple<int, int, int, int, int, int> queries[mx_t];

int ans[mx_t];

int main() {
    int t;
#ifndef TEST
    cin >> t;
#else
    t = 100;
#endif
    fo(tt, t) {
#ifndef TEST
        cin >> n >> p;
        ini(cnt, 0);
        fo(i, n) {
            cin >> g[i];
            ++cnt[g[i] % p];
        }
#else
        n = 100; p = rand() % 4 + 1;
        fo(i, 4) cnt[i] = rand() % 100;
#endif
        queries[tt] = mt(p, cnt[0], cnt[1], cnt[2], cnt[3], tt);
    }
    sort(queries, queries + t);
    int lastp = 0;
    fo(tt, t) {
        trace(tt, queries[tt]);
        int idx;
        tie(p, cnt[0], cnt[1], cnt[2], cnt[3], idx) = queries[tt];
        if(lastp != p) ini(dp, -1);
        ans[idx] = solve(0, cnt[0], cnt[1], cnt[2], cnt[3]);
    }

    rep(kase, 1, t) {
        cout << "Case #" << kase << ": " << ans[kase-1] << endl;
    }
    
    
	return 0;
}

