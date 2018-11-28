//
// Created by Evgeny Savinov on 09/01/2017.
//

#include <bits/stdc++.h>

#define clr(x) memset((x), 0, sizeof(x))
#define all(x) (x).begin(), (x).end()
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define forn(i, n) for(int i = 0; i < (int)(n); ++i)
#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; --i)
#define for1(i, n) for(int i = 1; i <= (int)(n); ++i)


using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
//typedef pair<long long, long long> pii;
typedef vector<long long> vll;
typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef int itn;
typedef unsigned int uint;

const ld PI = 3.1415926535897932384626433832795L;

template<class T>
bool uin(T &, const T &);

template<class T>
bool uax(T &, const T &);

template<class T>
T gcd(T, T);

template<class T>
T lcm(T, T);

template<class _T>
inline string tostr(const _T &);

template<typename T>
void input(T &);

class range {
    using type = long long;
public:
    class iterator {
        friend class range;

    public:
        using difference_type = range::type;
        using value_type = range::type;
        using pointer = const range::type *;
        using reference = const range::type &;
        using iterator_category = std::random_access_iterator_tag;

        value_type operator*() const { return i_; }

        const iterator &operator++() {
            ++i_;
            return *this;
        }

        iterator operator++(int) {
            iterator copy(*this);
            ++i_;
            return copy;
        }

        const iterator &operator--() {
            --i_;
            return *this;
        }

        iterator operator--(int) {
            iterator copy(*this);
            --i_;
            return copy;
        }

        difference_type operator-(const iterator &other) const { return i_ - other.i_; }

        iterator operator+(const difference_type &delta) const { return iterator(i_ + delta); }

        iterator &operator+=(const difference_type &delta) {
            i_ += delta;
            return *this;
        }

        iterator operator-(const difference_type &delta) const { return iterator(i_ - delta); }

        iterator &operator-=(const difference_type &delta) {
            i_ -= delta;
            return *this;
        }

        bool operator==(const iterator &other) const { return i_ == other.i_; }

        bool operator!=(const iterator &other) const { return i_ != other.i_; }

    protected:
        iterator(const value_type &start) : i_(start) {}

    private:
        value_type i_;
    };

    iterator begin() const { return begin_; }

    iterator end() const { return end_; }

    range(const type &begin, const type &end) : begin_(begin), end_(end) {}

    range(const type &end) : begin_(0), end_(end) {}

private:
    iterator begin_;
    iterator end_;
};

template<typename T = long long>
T nxt();

bool checkp(long long);

template<typename T>
T pw(T a, T n, T p);

template<typename T>
T inv(T a, T p);

template<class _T>
_T sqr(const _T &x);

class range;

mt19937_64 gen;

int TTT;

ll mod = 1000000007;


void pre() {

}

const int N = 100000;

struct minCostFlow {
    struct edge {
        int from, to;
        long long cap, flow, cost;
    };


    vector <edge> edges;
    vector<int> g[N];
    int vsize;

    int p[N];
    char used[N];
    long long dist[N];
    long long pi[N];


    void addEdge(int from, int to, long long cap, long long cost) {
        g[from].pb(edges.size());
        edges.push_back(edge{from, to, cap, 0, cost});
        g[to].pb(edges.size());
        edges.pb(edge{to, from, 0, 0, -cost});
    }


    bool fb(int s, int t) {
        memset(p, 0xff, vsize * sizeof(int));
        memset(dist, 0x3f, vsize * sizeof(long long));
        memset(used, 0, vsize * sizeof(char));
        dist[s] = 0;

        priority_queue<pair <long long, int> > q;
        q.push(mp(0, s));
        while (!q.empty()) {
            auto z = q.top();
            q.pop();
            if (dist[z.y] != -z.x) continue;
            int v = z.y;
            for (int ed : g[v]) {
                edge &e = edges[ed];
                int to = e.to;
                long long len = e.cost;
                if (e.cap > e.flow && dist[to] > dist[v] + len + pi[to] - pi[v]) {
                    dist[to] = dist[v] + len + pi[to] - pi[v];
                    p[to] = ed;
                    q.push(mp(-dist[to
                    ], to));
                }
            }
        }

        assert(p[t] != -1);
        return p[t] != -1;
    }

    long long cost;
    long long flow;

    long long pushFlow(int s, int t, long long need) {
        long long addFlow = need;
        for (int cur = t, e = p[cur]; cur != s; cur = edges[e].from, e = p[cur]) {
            addFlow = min(addFlow, edges[e].cap - edges[e].flow);
        }
        cost += (dist[t] - pi[t]) * addFlow;
        flow += addFlow;
        for (int cur = t, e = p[cur]; cur != s; cur = edges[e].from, e = p[cur]) {
            edges[e].flow += addFlow;
            edges[e ^ 1].flow -= addFlow;
        }
        for (int i = 0; i < vsize; ++i) {
            pi[i] -= dist[i];
            assert(pi[i] >= LLONG_MIN / 2);
        }
//        ll m = *min_element(pi, pi + vsize);
//        for (int i = 0; i < vsize; ++i) {
//            pi[i] -= m;
//        }
        return addFlow;
    }

    long long inf = 0x3f3f3f3f3f3f3f3fll;
    bool check() {
        memset(p, 0xff, vsize * sizeof(int));
        memset(pi, 0, vsize * sizeof(long long));
        int x = -1;

        for (int i = 0; i < vsize; ++i) {
            x = -1;
            for (int j = 0; j < (int)edges.size(); ++j) {
                const edge & e = edges[j];
                if (e.flow < e.cap && pi[e.from] + e.cost < pi[e.to]) {
                    pi[e.to] = max(-inf, pi[e.from] + e.cost);
                    p[e.to] = j;
                    x = e.to;
                }
            }
        }
        return x == -1;
    }

    void calcMinCostFlow(int s, int t, long long needFlow) {
        while (needFlow && fb(s, t)) {
            needFlow -= pushFlow(s, t, needFlow);
        }
    }

    minCostFlow(int vertices) {
        flow = 0;
        vsize = vertices;
        cost = 0;
        memset(pi, 0, vsize * sizeof(long long));
    }
};

void solve(int test) {
    int n = nxt();
    int customers = nxt();
    int tickets = nxt();

    vector <vector <int> > cnt_c(customers);

    vector <int> delta(n);

    forn(i, tickets) {
        int pos = nxt() - 1;
        int buyer = nxt() - 1;
        cnt_c[buyer].push_back(pos);
        delta[pos]++;
    }


    int L = 0;
    forn(i, customers) {
        L = max(L, (int)cnt_c[i].size());
    }


    int R = tickets;

    while (L < R) {
        int M = (L + R) / 2;

        int rem = 0;

        ford(i, n) {
            rem += delta[i];
            rem = max(rem - M, 0);
        }

        if (rem > 0) {
            L = M + 1;
        } else {
            R = M;
        }
    }

    int rem = 0;
    int ans = 0;
    ford(i, n) {
        int r = L;
        int s = min(r, delta[i]);
        r -= s;
        delta[i] -= s;

        ans += delta[i];
        rem += delta[i];
        rem -= s;
        if (rem < 0) rem = 0;
    }


    cout << "Case #" << test << ": ";
    cout << L << " " << ans << "\n";
}

int main(int argc, char **argv) {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#else
    #define fname "sequence"
    //freopen(fname".in", "r", stdin);
    //freopen(fname".out", "w", stdout);
#endif
    pre();
    ::TTT = nxt();
#ifdef LOCAL
#else
#endif

    for (int test = 1; test <= ::TTT; ++test) {
        solve(test);
    }

#ifdef LOCAL
    cerr << "Time elapsed: " << 1.0 * clock() / CLOCKS_PER_SEC * 1000 << " ms." << endl;
#endif
    return 0;
}


template<typename T>
T gcd(T x, T y) {
    while (y > 0) {
        x %= y;
        swap(x, y);
    }
    return x;
}

template<class T>
T lcm(T a, T b) {
    return a / gcd(a, b) * b;
}


template<class _T>
inline _T sqr(const _T &x) {
    return x * x;
}

template<class _T>
inline string tostr(const _T &a) {
    ostringstream os("");
    os << a;
    return os.str();
}


template<typename T>
inline void input(T &a) {
    static int ed;
    a = 0;
    while (!isdigit(ed = getchar()) && ed != '-') {}
    char neg = 0;
    if (ed == '-') {
        neg = 1;
        ed = getchar();
    }
    while (isdigit(ed)) {
        a = 10 * a + ed - '0';
        ed = getchar();
    }
    if (neg) a = -a;
}

template<typename T = long long>
inline T nxt() {
    T res;
    input(res);
    return res;
}

void myassert(bool v) {
    assert(v);
//cout << "FAIL\n";
//exit(0);
}

mt19937 generator;

bool checkp(long long v) {
    if (v < 2) return false;
    for (long long i = 2; i * i <= v; ++i) {
        if (v % i == 0) {
            return false;
        }
    }
    return true;
}

template<typename T>
T pw(T a, T n, T m) {
    T res = 1;
    while (n) {
        if (n & 1) {
            res = res * a % m;
        }
        a = a * a % m;
        n >>= 1;
    }
    return res;
}

template<typename T>
T inv(T a, T p) {
    T res = 1;
    while (a > 1) {
        res = res * (p - p / a) % p;
        a = p % a;
    }
    return res;
}


template<class T>
bool uin(T &a, const T &b) {
    if (b < a) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
bool uax(T &a, const T &b) {
    if (b > a) {
        a = b;
        return true;
    }
    return false;
}