#include <bits/stdc++.h>

#define DEBUG 1

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef unsigned int uint;
typedef unsigned short ushort;
typedef pair<int, int> PII;

#define MAX_INT (int)0x7fffffff
#define MIN_INT (int)0x80000000
#define MAX_UINT (uint)0xffffffff

#define TTi template<typename T> inline
TTi T SQR(T x) { return x * x; }

#define CONCAT3_NX(x, y, z) x ## y ## z
#define CONCAT3(x, y, z) CONCAT3_NX(x, y, z)
#define VAR(name) CONCAT3(__tmpvar__, name, __LINE__)
#define TYPE(x) __typeof(x)

#define FOR(i, s, n)  for (TYPE(n) i=(s),   VAR(end)=(n);  i <  VAR(end);  i++)
#define RFOR(i, s, n) for (TYPE(n) i=(n)-1, VAR(end)=(s);  i >= VAR(end);  i--)
#define FORN(i, n)    FOR(i, 0, n)
#define RFORN(i, n)   RFOR(i, 0, n)
#define FOREACH(i, v) for (auto& i: v)

#define SC() scanf("\n")
#define SC1(fmt, a) scanf(fmt, &a)
#define SC2(fmt, a, b) scanf(fmt, &a, &b)
#define SC3(fmt, a, b, c) scanf(fmt, &a, &b, &c)
#define SCi(a) scanf("%d", &a)
#define SCii(a,b) scanf("%d%d", &a, &b)
#define SCiii(a,b,c) scanf("%d%d%d", &a, &b, &c)
#define fLL "%lld"
#define SCl(a) scanf(fLL, &a)
#define SCll(a,b) scanf(fLL fLL, &a, &b)
#define SClll(a,b,c) scanf(fLL fLL fLL, &a, &b, &c)
#define SCs(s, n) {scanf("%s", s); n = strlen(s);}
#define SCc(s) scanf("%c", &c)

#define MP make_pair
#define PB push_back
#define WHOLE(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define POPST(stack) (stack).top();(stack).pop();
#define POPQ(queue) (queue).front();(queue).pop();
#define CONTAINS(v, x) (find(WHOLE(v), (x)) != v.end())
#define SORT(v) (sort(WHOLE(v)))

#define LIMIT(x, lim) {if (x > lim) x = lim;}
TTi void UPDATE_MIN(T &x, T y) {if (y < x) {x = y;}}
TTi void UPDATE_MAX(T &x, T y) {if (x < y) {x = y;}}
TTi int ARGMAX(T cont) { return max_element(cont.begin(), cont.end()) - cont.begin(); }
TTi int ARGMIN(T cont) { return min_element(cont.begin(), cont.end()) - cont.begin(); }

TTi int hamming(T x) {return __builtin_popcountll((long long)x);}
int hamming(int x) {return __builtin_popcount(x);}
int hamming(long x) {return __builtin_popcountl(x);}
int hamming(long long x) {return __builtin_popcountll(x);}

vector<string> split(const string& s, char c) {
    vector<string> v; stringstream ss(s); string x;
    while (getline(ss, x, c)) v.emplace_back(x); return move(v);
}
template<typename T, typename... Args>
inline string arrStr(T arr, int n) {
    stringstream s; s << "[";
    FORN(i, n - 1) s << arr[i] << ",";
    s << arr[n - 1] << "]";
    return s.str();
}

// #ifndef ONLINE_JUDGE
#ifdef JUDGE_LOCAL
    #define EPR(args...)   if (DEBUG) {fprintf(stderr, args);}
    #define EARR(arr, n)   if (DEBUG) {FORN(i, n) fprintf(stderr, "%d, ", arr[i]);}
    #define EVEC(arr)      if (DEBUG) {FORN(i, arr.size()) fprintf(stderr, "%d, ", arr[i]);}
    #define EVARS(args...) if (DEBUG) { __evars_begin(__LINE__); __evars(split(#args, ',').begin(), args);}

    inline void __evars_begin(int line) { cerr << "#" << line << ": "; }
    inline void __evars(vector<string>::iterator it) { cerr << endl; }
    TTi void __evars_out_var(vector<T> val) { cerr << arrStr(val, val.size()); }
    TTi void __evars_out_var(T* val) { cerr << arrStr(val, 10); }
    TTi void __evars_out_var(T val) { cerr << val; }
    template<typename T, typename... Args>
    inline void __evars(vector<string>::iterator it, T a, Args... args) {
        cerr << it->substr((*it)[0] == ' ', it->length()) << "=";
        __evars_out_var(a);
        cerr << "; ";
        __evars(++it, args...);
    }
#else
    #define EPR(args...) 1
    #define EARR(args...) 1
    #define EVEC(args...) 1
    #define EVARS(args...) 1
#endif

template<class T> inline string TOSTR(const T & x) { stringstream ss; ss << x; return ss.str(); }
#define DIE(args...) {printf(args);exit(0);}
inline void DIER(char *res, char *dbg=NULL) {
    fprintf(stderr, "[!] die reason %s\n", dbg);
    puts(res);
    exit(0);
}
inline void PR(void) {}
inline void PR(int x) {printf("%d", x);}
inline void PR(LL x) {printf("%lld", x);}
inline void PR(size_t x) {printf("%llu", (ULL)x);}
inline void PR(const char * s) {printf("%s", s);}
inline void PR(double f) {printf("%.10f", f);}
inline void PR(long double f) {printf("%.10f", (double)f);}
TTi void PR(vector<T> &vec) {auto sz = vec.size();for(auto x:vec){PR(x);(--sz)?putc(0x20,stdout):0;}}
TTi void PRS(T x) {PR(x);putc(0x20,stdout);}
TTi void PRN(T x) {PR(x);putc(0x0a,stdout);}
void PRN(void) {putc(0x0a,stdout);}

struct pairhash {
    template <typename T, typename U>
    std::size_t operator() (const std::pair<T, U> &x) const {
        return std::hash<T>()(x.first) ^ std::hash<U>()(x.second);
    }
};

const int MOD = 1000 * 1000 * 1000 + 7;
const double PI = 3.1415926535897932384626433832795l;

TTi T gcd(T a, T b) {
    return a ? gcd(b % a, a) : b;
}

inline void addto(int &a, int b) {
    a += b;
    if (a >= MOD) a -= MOD;
}
inline int add(int a, int b) {
    a += b;
    if (a >= MOD) a -= MOD;
    return a;
}
inline void subto(int &a, int b) {
    a -= b;
    if (a < 0) a += MOD;
    if (a >= MOD) a -= MOD;
}
inline int sub(int a, int b) {
    a -= b;
    if (a < 0) a += MOD;
    if (a >= MOD) a -= MOD;
    return a;
}
inline void multo(int &a, int b) {
    a = (long long)a * b % MOD;
}
inline int mul(int a, int b) {
    return (long long)a * b % MOD;
}
inline int mulmod(int a, int b, int mod) {
    return (long long)a * b % mod;
}
inline int powmod(int a, int e, int mod) {
    int x;
    for(x = 1; e > 0; e >>= 1) {
        if (e & 1)
            x = mulmod(x, a, mod);
        a = mulmod(a, a, mod);
    }
    return x;
}
inline int invmod_prime(int a, int mod) {
    return powmod(a, mod - 2, mod);
}
inline LL invmod_LL(LL p){
    LL q = p;
    for(LL a = p*p; a != 1; a*=a) q*=a;
    return q;
}


// -----------------------------------------------------------------
// CODE
// -----------------------------------------------------------------

#define MAXN 123

int N, M, K, L, E, Q;
int fuel[MAXN];
int spd[MAXN];
LL dist0[MAXN][MAXN];
LL d[MAXN][MAXN];
double ans[MAXN][MAXN] = {};
vector<int> reachable[MAXN];

LL INF = 1ll << 62;

void rundp(int s) {
    priority_queue<pair<double, int>> pq;
    pq.push({0.0, s});
    while (pq.size() > 0) {
        // EVARS(pq.size());
        double t;
        int v;
        tie(t, v) = pq.top();
        t = -t;
        pq.pop();
        if (t > ans[s][v]) continue;
        int f = fuel[v];
        int sp = spd[v];
        FOREACH(u, reachable[v]) {
            if (d[v][u] <= f) {
                double t2 = t + d[v][u] / (double)sp;
                if (t2 < ans[s][u]) {
                    ans[s][u] = t2;
                    pq.push({-t2, u});
                    // EVARS(s, u, t, t2, ans[s][u]);
                }
            }
            else {
                break;
            }
        }
    }
}

void process() {
    FORN(k, N) FORN(i, N) FORN(j, N)
        if (d[i][k] != INF && d[k][j] != INF && d[i][k] + d[k][j] < d[i][j])
            d[i][j] = d[i][k] + d[k][j];

    // FORN(i, N) {
    //     FORN(j, N) {
    //         EVARS(i, j, d[i][j]);
    //     }
    //     EPR("\n");
    // }

    FORN(s, N) {
        FORN(y, N) {
            reachable[s].push_back(y);
        }
        sort(WHOLE(reachable[s]), [&](int i, int j) {
            return d[s][i] < d[s][j];
        });
    }

    FORN(s, N) {
        // EVARS(s);
        FORN(y, N) ans[s][y] = 1e15;
        rundp(s);
        // FORN(y, N) EVARS(s, y, ans[s][y]);
    }
}

double query(int s, int t) {
    return ans[s][t];
}

int main() {
    ios_base::sync_with_stdio(0);

    int T; SCi(T);
    FOR(t, 1, T + 1) {
        SCii(N, Q);
        FORN(i, N) {
            SCii(fuel[i], spd[i]);
        }
        FORN(x, N) {
        FORN(y, N) {
            SCl(dist0[x][y]);
            if (dist0[x][y] == -1) dist0[x][y] = INF;
            d[x][y] = dist0[x][y];
            // EVARS(x, y, d[x][y]);
        }}

        process();

        printf("Case #%d:", t);
        FORN(i, Q) {
            int s, t;
            SCii(s, t);
            s--;t--;
            printf(" %.7f", query(s, t));
        }
        printf("\n");
    }

    return 0;
}
