// (C) Maks, 2016-2017.

#pragma GCC optimize("O3")
#ifdef DEBUG
#define _GLIBCXX_DEBUG
#endif
//#pragma comment(linker, "/STACK:64000000")
#include <algorithm>
#include <array>
#include <bitset>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <cerrno>
#include <cfenv>
#include <fstream>
#include <functional>
#include <iostream>
#include <list>
#include <map>
#include <memory.h>
#include <queue>
#include <random>
#include <string>
#include <set>
#include <sstream>
#include <stack>
#include <tuple>
#include <unordered_map>
#include <unordered_set>
#include <utility>
#include <valarray>
#include <vector>
#include <sys/time.h>
#include <x86intrin.h>

using namespace std;
using i64 = int64_t;
using ll = i64;
using ull = uint64_t;
using D = double;
using LD = long double;

using tiii = tuple<int, int, int>;
using pii = pair<int, int>;
using pil = pair<int, ll>;
using pli = pair<ll, int>;
using pll = pair<ll, ll>;

using vi = vector<int>;
using vl = vector<ll>;
using vpii = vector<pii>;
using vvpii = vector<vector<pii>>;
constexpr int maxmemallocator = 20000000; // bytes / NOT TESTED
template <typename T>
struct n_dimensional_allocator {
  char buffer[maxmemallocator+10];
  T* bufpos;
  typedef T value_type;
  n_dimensional_allocator() noexcept { bufpos = static_cast<T*>(static_cast<void*>(buffer)); }
  template <typename U> n_dimensional_allocator(const n_dimensional_allocator<U>&) noexcept { bufpos = static_cast<T*>(buffer); }
  T* allocate(std::size_t n) {
      T* start = bufpos;
      bufpos += n;
      return start;
  }
  void deallocate(T* p, std::size_t n) { }
};
template <class T, class U>
constexpr bool operator== (const n_dimensional_allocator<T>&, const n_dimensional_allocator<U>&) noexcept {return true;}
template <class T, class U>
constexpr bool operator!= (const n_dimensional_allocator<T>&, const n_dimensional_allocator<U>&) noexcept {return false;}
using vvi = vector<vector<int, n_dimensional_allocator<int>>, n_dimensional_allocator<vector<int>>>;

using si = set<int>;
using spii = set<pii>;
using spli = set<pli>;
template<typename T = int>
using pq = priority_queue<T, std::vector<T>>; // greatest
template<typename T = int>
using rpq = priority_queue<T, std::vector<T>, std::greater<T>>;
using mii = map<int, int>;
using mli = map<ll, int>;

template<typename T>
inline bool inserted(set<T>& s, T&& value) { bool result; std::tie(std::ignore, result) = s.insert(forward<T>(value)); return result; }
#define map_insert(m,f,s)         m.emplace(std::piecewise_construct, std::forward_as_tuple(f), std::forward_as_tuple(s))
#define map_insert2(m,f,s1,s2)    m.emplace(std::piecewise_construct, std::forward_as_tuple(f), std::forward_as_tuple(s1, s2))

template<int N>
using bs = bitset<N>;
template<int N>
using vbs = vector<bitset<N>>;  // XMM registers
using vb = vector<bool>;
using vai = valarray<int>;      // binary search optimization; XMM registers

inline double getUserTime() { timeval tv; gettimeofday(&tv, 0); return tv.tv_sec + tv.tv_usec * 1e-6; }
#define USERTIME()          ({ double result = getUserTime(); fprintf(stderr, "User Time = %.6lf\n", result); \
                            fflush(stderr); result; })
#define TOTALTIME()         ({ double result = (double) clock() / CLOCKS_PER_SEC; \
                            fprintf(stderr, "User+System Time = %.6lf\n", result); fflush(stderr); result; })
#define DOJOB(job)          ({ double __begin = clock(); errno = 0; int result = (job); \
                            fprintf(stderr, "User+System Time = %.6lf\n", ((double) clock() - __begin) / CLOCKS_PER_SEC); \
                            fflush(stderr); result; })

#if ( ( _WIN32 || __WIN32__ ) && __cplusplus < 201103L)
#define LLD "%I64d"
#else
#define LLD "%lld"
#endif
#define fastIO cin.sync_with_stdio(false), cin.tie(nullptr)
#define noFastIO cin.sync_with_stdio(true), cin.tie(cout)

template<typename T>
void _R(T &x) { cin >> x; }
template<typename T>
void _R(vector<T> &x) { for (int i = 0; i < x.size(); ++i) _R(x[i]); }
template<typename T, size_t N>
void _R(T (&x)[N]) { for (int i = 0; i < N; ++i) { _R(x[i]); } }
void _R(int &x) { scanf("%d", &x); }
void _R(ll &x) { scanf(LLD, &x); }
void _R(double &x) { scanf("%lf", &x); }
void _R(float &x) { scanf("%f", &x); }
void _R(char &x) { scanf(" %c", &x); }
void _R(char *s) { scanf("%s", s); }
void R() {}
template<typename T, size_t N>
void R(T (&a)[N], int n) { for (int i = 0; i < n; ++i) _R(a[i]); }
template<size_t N>
void R(pii (&a)[N], int n) { for (int i = 0; i < n; ++i) { _R(a[i].x); _R(a[i].y); } }
template<size_t N>
void R(tiii (&a)[N], int n) { for (int i = 0; i < n; ++i) { _R(a[i].x); _R(a[i].y); _R(a[i].z); } }
template<typename T, typename... U>
void R( T& head, U&... tail ) {
    _R(head);
    R(tail...);
}
#define DIR(a)                  int a; R(a);
#define DIIR(a, b)              int a, b; R(a, b);
#define DIIIR(a, b, c)          int a, b, c; R(a, b, c);
#define DIILR(a, b, c)          int a, b; ll c; R(a, b, c);

template<typename T>
void _P(const T &x) { cout << x; }
void _P(const int &x) { printf("%d", x); }
void _P(const ll &x) { printf(LLD, x); }
void _P(const double &x) { printf("%lf", x); }
void _P(const float &x) { printf("%f", x); }
void _P(const pii &x) { printf("%d %d", x.first, x.second); }
void _P(const pli &x) { printf("%lld %d", x.first, x.second); }
void _P(const pil &x) { printf("%d %lld", x.first, x.second); }
void _P(const tiii &x) { printf("%d %d %d", get<0>(x), get<1>(x), get<2>(x)); }
template<typename T>
void _P(const vector<T> &x) {
    for (auto i = x.cbegin(); i != x.cend(); i++) {
        if (i != x.cbegin()) putchar(' ');
        _P(*i);
    }
}
template<typename T>
void _P(vector<T> &x) {
    for (int i = 0; i < (int) x.size() - 1; ++i) { _P(x[i]); putchar(' '); }
    if (x.size() >= 1) {
        _P(x[(int) x.size() - 1]);
        puts("");
    }
}
void P() {}
template<typename T, size_t N>
void P(T (&x)[N], int n) {
    for (int i = 0; i < n - 1; ++i) { _P(x[i]); putchar(' '); }
    if (n >= 1) {
        _P(x[n - 1]);
        puts("");
    }
}
template<typename T, typename... U>
void P(const T& head, const U&... tail) {
    _P(head);
    if (sizeof...(tail)) {
        putchar(' ');
        P(tail...);
    } else {
        puts("");
    }
}

template<typename Iter>
void _outIterable(ostream& s, Iter b, Iter e);
template<typename Iter>
void _outMapIterable(ostream& s, Iter b, Iter e);

void _out(ostream &s, const char *st) { s << string(st); }
void _out(ostream& s, int c) { s << c; }
template<typename A, typename B>
void _out(ostream &s, const pair<A,B> &p) { s << "(" << p.first << "," << p.second << ")"; }
template<typename T>
void _out(ostream &s, const vector<T>& c) { _outIterable(s, c.begin(), c.end()); }
template<typename T, size_t N>
void _out(ostream &s, const array<T,N>& c) { _outIterable(s, c.begin(), c.end()); }
template<typename T>
void _out(ostream &s, const set<T>& c) { _outIterable(s, c.begin(), c.end()); }
template<typename A, typename B>
void _out(ostream &s, const map<A,B>& c) { _outMapIterable(s, c.begin(), c.end()); }
template<typename T, size_t N >
void _out(ostream &s, T (&c)[N]) { _outIterable(s, &c[0], &c[N]); }
template<typename T, size_t N >
void _show(T (&c)[N], int n) { _outIterable(cerr, &c[0], &c[0] + n); putchar('\n'); }


template<typename Iter>
void _outIterable(ostream& s, Iter b, Iter e) {
    s << "[";
    for (auto it = b; it != e; ++it) {
        s << (it == b ? "" : ", ");
        _out(s, *it);
    }
    s << "]";
}
template<typename Iter>
void _outMapIterable(ostream& s, Iter b, Iter e) {
    s << "{";
    for (auto it = b; it != e; ++it) {
        s << (it == b ? "" : ", ") << it->first << "=>";
        _out(s, it->second);
    }
    s << "}";
}

template<typename T>
void _show(T&& head) { _out(cerr, head); putchar('\n'); }
template<typename T, typename... Args>
void _show(T&& head, Args&&... tail ) {
    _out(cerr, head);
    fprintf(stderr, ", ");
    _show(tail...);
    putchar('\n');
}
#define show(...) do { fprintf(stderr, "%s:%d - \"%s\" - ", __PRETTY_FUNCTION__, __LINE__, #__VA_ARGS__); _show(__VA_ARGS__); } while (0)
#define ashow(a,n) do { fprintf(stderr, "%s:%d - ", __PRETTY_FUNCTION__, __LINE__); _show(a, n); } while (0)

template<typename T>
constexpr T pi = T(3.1415926535897932385);
const int dx[] = {-1, 0, 1,  0};
const int dy[] = { 0, 1, 0, -1};
const int dxKing[] = {-1, -1, 0, 1, 1,  1,  0, -1};
const int dyKing[] = { 0,  1, 1, 1, 0, -1, -1, -1};
const int dxKn[] = {-2, -1, 1, 2,  2,  1, -1, -2};
const int dyKn[] = { 1,  2, 2, 1, -1, -2, -2, -1};
#define INF_9                   ((int)1e9)
#define INF2_9                  ((int)2e9)
#define INF_18                  ((i64)1e18)
#define INF_3f                  0x3f3f3f3f
#define INF_3fLL                0x3f3f3f3f3f3f3f3fLL
#define BRUTE_FORCE_THRESHOLD   1000
#define INFINT                  (~0U>>1)
#define INFINTLL                (~0ULL>>1)
#define MOD9                    ((int)1e9+9)
#define MOD7                    ((int)1e9+7)
#define EPS                     1e-9

// macros with side effects
#define TESTS               int __testId; R(__testId); while (__testId-- > 0)
#define DFS(u, proc, stepinto, postproc)        bool u[maxn+3]; int proc(int v) { u[v] = true; int res = 0; \
                                                for (auto& to : g[v]) { if (!u[to]) { stepinto; } } postproc; return res; }
#define RUG(m)                                  for (int i = 0; i < m; ++i) { int x, y; \
                                                    scanf("%d %d", &x, &y); g[x].push_back(y); g[y].push_back(x); }
#define RUGL(m)                                 for (int i = 0; i < m; ++i) { int x, y; ll z; \
                                                    scanf("%d %d %lld", &x, &y, &z); g[x].emplace_back(y, z); g[y].emplace_back(x, z); }
#define RDG(m)                                  for (int i = 0; i < m; ++i) { int x, y; \
                                                    scanf("%d %d", &x, &y); g[x].push_back(y); }
#define RDGL(m)                                 for (int i = 0; i < m; ++i) { int x, y; ll z; \
                                                    scanf("%d %d %lld", &x, &y, &z); g[x].emplace_back(y, z); }
#define FOR(i,a,b)          for (int i = a; i < b; ++i)
#define FORA(v,a)           for (auto& v : a)
#define RR(i,b)             FOR(i, 0, b)
#define MS(a,p)             memset((a), (p), sizeof a)
#define SZ(a)               ((int) (a).size())
#define SZe(a,x)            ((int) (a).size() == (x))
#define SZl(a,x)            ((int) (a).size() < (x))
#define ALL(a)              (a).begin(), (a).end()
#define RALL(a)             (a).rbegin(), (a).rend()
#define UNQ(a)              (a).resize(unique(all(a)) - (a).begin())
#define PB                  push_back
#define EB                  emplace_back
#define APPEND(to,from)     (to).insert(end(to), begin(from), end(from))
#define PREPEND(to,from)    (to).insert(begin(to), begin(from), end(from))
#define EM                  emplace
#define PU                  push
#define PO(q)               (q).pop()
#define TO(q)               (q).top()
#define EP(a)               ((a).empty())
#define x                   first
#define y                   second
#define prev                prev28
#define next                next28
#define HP(x, y)            hypot((x), (y))
#define POW(x, y)           pow((double) (x), (y))
#define bitcount(x)         __builtin_popcountll(x)
#define BIT(x, i)           (((x)>>(i))&1)
#define pow2(x)             (1LL<<(x))
#define pow2_(x)            (2LL<<(x))
#define ISPOW2(x)           ((x) != 0 && ((x)&((x) - 1)) == 0)
inline ll rightmostPow2(ll x) { return x ^ (x & (x - 1)); }
inline ll leftmostPow2(ll n) { n = n | (n >> 1); n = n | (n >> 2); n = n | (n >> 4); n = n | (n >> 8); n = n | (n >> 16); n = n | (n >> 32); return (n + 1) >> 1; }
#define G                   vector<int> g[maxn+3];
#define GD                  vector<pil> g[maxn+3];
#define RG(g,m)             for (int i = 0; i < (m); i++) { int u, v; scanf("%d%d", &u, &v); u--, v--; (g)[u].push_back(v); (g)[v].push_back(u); }
#define VS(a,n,m)           vector<string> a{n, string{m, "X"}}

#define Abs(x)              ((x) < 0 ? -(x) : (x))
#define Max(a,b)            ((a) > (b) ? (a) : (b))
inline double reldiff(double a, double b) { double c = Abs(a), d = Abs(b); d = Max(c, d); return d == 0.0 ? 0.0 : Abs(a - b) / d; }
inline bool eq(double a, double b) { return reldiff(a, b) <= 1e-8; }
inline bool le(double a, double b) { return !eq(a,b) && a < b; }
inline bool mo(double a, double b) { return !eq(a,b) && a > b; }
inline int ro(double x) { return (int)(x < 0 ? x - 0.5 : x + 0.5); }
inline int ro(double x, double precision) { return (int)(x >= 0 ? x / precision + 0.5 : x / precision - 0.5) * precision; }
template<typename T>
inline T sqr(T a){ return a * a; }

std::default_random_engine random_engine(0x13131313);
template<class T>
inline T randint(T L, T R) { return std::uniform_int_distribution<T>(L, R)(random_engine); }

template<class T>
T gcd(T a, T b) { return a ? gcd (b % a, a) : b; }
//__gcd
template<class T>
T lcm(T a, T b) { return a / gcd (a, b) * b; }

inline void inc(int& a, int b, int p) { a += b; if (a >= p) a -= p; }
inline void dec(int& a, int b, int p) { a -= b; if (a < 0) a += p; }
inline int mul(int a, int b, int p) { return (ll) a * b % p; }
template<typename T>
inline bool mx(T& a, T b) { if (a < b) { a = b; return true; } return false; }
template<typename T>
inline bool mn(T& a, T b) { if (b < a) { a = b; return true; } return false; }

inline bool iisctr(pii a, pii b) { return (a.x < b.y && a.x > b.x) && (a.y > b.y); }
bool iisct(pii a, pii b) { if (a.x > a.y) swap(a.x, a.y); if (b.x > b.y) swap(b.x, b.y); return iisctr(a, b) || iisctr(b, a); }

//#undef show
//#define show(...)
// ---
constexpr int maxn =            200000;
constexpr int sqrn =            500;
constexpr int logn =            19;
constexpr int A =               26; // alphabet

struct Evnt {
    double xx;
    int ind;
    Evnt() {}
    Evnt(double xx_, int ind_, bool opening) : xx(xx_), ind(ind_ + 1) { if (opening) xx = -xx_; }
    bool operator<=(const Evnt& rhs) const { return tie(xx, ind) <= tie(rhs.xx, rhs.ind); }
};
constexpr int maxnev =          maxn * 2;   // for events
//Evnt evs[maxnev+2];
/*
template<typename U>
void sortr(U& a) { sort(begin(a), end(a), std::greater<U::value_type>()); }
template<typename T, size_t N>
void sortr(T (&a)[N], int n) { sort(&a[0], &a[n], std::greater<T>()); }
*/


int T;
int k, n;
char s[maxn+2];
int a[maxn+2];
int res;

int solve(int testId) {

    scanf("%d", &T);
    FOR(t,1, T+1) {
        res=0;
        scanf("%s %d", &s[0], &k);
        n=strlen(s);
        //puts(s);
        FOR(j,0,n) {
            a[j] = s[j]=='+';
            //printf("t %d %d %d\n",j,a[j],s[j]);
        }

        FOR(j,0,n-k+1) {
            //printf("t %d %d\n",j,a[j]);
            if (!a[j]) {
                FOR(u,j,j+k) {
                    a[u]=1-a[u];
                }
                res++;
                //printf("%d %d\n",j,res);
            }
        }
        FOR(u,n-k+1,n) {
            if (!a[u]) { res=-1; break; }
        }

        if (res==-1)
            printf("Case #%d: IMPOSSIBLE\n", t);
        else
            printf("Case #%d: %d\n", t, res);
    }


    fflush(stdout);
    return EXIT_SUCCESS;
}

int main() {
    fastIO;
    #ifdef LOCAL
        int numTests = 3;
        RR(i, numTests) {
            int exitStatus = DOJOB(solve(i));
            if (exitStatus != EXIT_SUCCESS) return exitStatus;
        }
        return EXIT_SUCCESS;
    #else
        return solve(0);
    #endif
}
