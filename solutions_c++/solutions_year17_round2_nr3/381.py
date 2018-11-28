#include <bits/stdc++.h>

#define ford(i, n) for(int i = (int)(n) - 1; i >= 0; i--)
#define forn(i, n) for(int i = 0; i < (int)(n); i++)
#define for1(i, n) for(int i = 1; i <= (int)(n); i++)
#define all(x) (x).begin(), (x).end()
#define clr(x) memset((x), 0, sizeof((x)));
#define pb push_back
#define mp make_pair
#define x first
#define y second

using namespace std;
typedef long double ld;
typedef long long ll;
typedef pair<int, int> PII;
typedef pair<ll, ll> pii;
typedef vector<int> vi;
typedef long long i64;
typedef unsigned long long ull;

mt19937_64 gen;

template<class T>
bool remin(T &a, const T &b) {
    if (a > b) {
        a = b;
        return true;
    }
    return false;
}

template<class T>
bool remax(T &a, const T &b) {
    if (a < b) {
        a = b;
        return true;
    }
    return false;
}

int nxt() {
    int x;
    scanf("%" PRId32, &x);
    return x;
}

ll nxtll() {
    ll x;
    scanf("%" PRId64, &x);
    return x;
}

ll gcd(ll a, ll b) {
    a = abs(a);
    b = abs(b);
    while (b) {
        a %= b;
        swap(a, b);
    }
    return a;
}

struct Q {
    ll n, d;
    Q(ll a = 0): n(a), d(1) {}
    Q(ll nn, ll dd) : n(nn), d(dd) {
        norm();
    }
    void norm() {
        ll g = gcd(abs(n), abs(d));
        n /= g;
        d /= g;
        if (d < 0) {
            n *= -1;
            d *= -1;
        }
    }
    Q operator + (const Q &r) const {
        return Q(n * r.d + d * r.n, d * r.d);
    }
    Q operator - (const Q &r) const {
        return Q(n * r.d - d * r.n, d * r.d);
    }
    Q operator * (const Q &r) const {
        return Q(n * r.n, d * r.d);
    }
    Q operator / (const Q &r) const {
        return Q(n * r.d, d * r.n);
    }
    ll value(const Q &r) const {
        return n * r.d - d * r.n;
    }
    bool operator < (const Q &r) const {
        return value(r) < 0;
    }
    bool operator != (const Q &r) const {
        return value(r) != 0;
    }
    bool operator > (const Q &r) const {
        return value(r) > 0;
    }
    bool operator >= (const Q &r) const {
        return value(r) >= 0;
    }
    bool operator <= (const Q &r) const {
        return value(r) <= 0;
    }
    bool operator == (const Q &r) const {
        return value(r) == 0;
    }
};

ostream &operator<<(ostream &os, const Q &p) {
    return os << p.n << "/" << p.d;
}

struct pt {
    double x, y;

    pt() = default;

    pt(ld x, ld y) : x(x), y(y) {}

    inline pt operator-(const pt &r) const {
        return pt(x - r.x, y - r.y);
    }

    inline pt operator+(const pt &r) const {
        return pt(x + r.x, y + r.y);
    }

    inline pt operator*(const ld &r) const {
        return pt(x * r, y * r);
    }

    inline pt operator -() const {
        return pt(-x, -y);
    }

    inline ld sqlen() const {
        return fabsl(x * x + y * y);
    }
};

ostream &operator<<(ostream &os, const pt &p) {
    return os << "(" << p.x << "," << p.y << ")";
}

ostream &operator<<(ostream &os, const pii &p) {
    return os << "(" << p.x << "," << p.y << ")";
}

pii operator - (const pii &l, const pii &r) {
    return pii(l.x - r.x, l.y - r.y);
}

inline double cross(const pt &l, const pt &r) {
    return l.x * r.y - l.y * r.x;
}

inline double dot(const pt &l, const pt &r) {
    return l.x * r.x + l.y * r.y;
}


ll pwmod(ll a, ll n, ll mod) {
    ll ret = 1;
    while (n) {
        if (n & 1) ret = ret * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return ret;
}

template<typename T>
inline T sqr(T x) {
    return x * x;
}


inline bool is_prime(ull x) {
    for (ull i = 2; i * i <= x; ++i) {
        if (x % i == 0) {
            return false;
        }
    }
    return true;
}

void solve() {
    int n = nxt();
    int q = nxt();
    vector<ll> e(n);
    vector<ll> s(n);
    forn(i, n) {
        e[i] = nxt();
        s[i] = nxt();
    }

    vector<vector<ll> > d(n, vector<ll>(n, 0));
    forn(i, n) {
        forn(j, n) {
            d[i][j] = nxt();
        }
    }
    forn(i, n) {
        d[i][i] = 0;
    }

    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                if (d[i][k] == -1 || d[k][j] == -1) continue;
                if (d[i][j] == -1 || d[i][j] > d[i][k] + d[k][j]) {
                    d[i][j] = d[i][k] + d[k][j];
                }
            }
        }
    }
//    cout << endl;
//    forn(i, n) {
//        forn(j, n) {
//            cout << d[i][j] << " ";
//        }
//        cout << endl;
//    }
//    cout << endl;


    vector<vector<double> > dist(n, vector<double>(n, 1e50));
    forn(i, n) {
        forn(j, n) {
            if (d[i][j] == -1) continue;
            if (d[i][j] > e[i]) continue;
            dist[i][j] = d[i][j] / (double)s[i];
        }
    }

//    forn(i, n) {
//        forn(j, n) {
//            cout << dist[i][j] << " ";
//        }
//        cout << endl;
//    }
//    cout << endl;

    forn(i, n) {
        dist[i][i] = 0;
    }

    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }
    cout << setprecision(10) << fixed;
    forn(i, q) {
        int s = nxt() - 1;
        int t = nxt() - 1;
        cout << dist[s][t] << " ";
    }
    cout << "\n";
}

void prepare() {

}

int main() {
#ifdef LOCAL
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(false);
    cin.tie(0);

    prepare();

    int t = 1;
//    cin >> t;
    t = nxt();
    forn(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}
