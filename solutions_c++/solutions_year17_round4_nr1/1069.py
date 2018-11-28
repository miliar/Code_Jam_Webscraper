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

//mt19937_64 gen;

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
    double vald(const Q &r) const {
        return n * 1.0 * r.d - d * 1.0 * r.n;
    }
    bool operator < (const Q &r) const {
        double vv = vald(r);
        if (vv < -1e10) {
            return true;
        }
        if (vv > 1e10) {
            return false;
        }
        return value(r) < 0;
    }
    bool operator > (const Q &r) const {
        double vv = vald(r);
        if (vv < -1e10) {
            return false;
        }
        if (vv > 1e10) {
            return true;
        }
        return value(r) > 0;
    }
    bool operator != (const Q &r) const {
        return !(*this == r);
    }
    bool operator >= (const Q &r) const {
        return *this > r || *this == r;
    }
    bool operator <= (const Q &r) const {
        return *this < r || *this == r;
    }


    bool operator == (const Q &r) const {
        double vv = vald(r);
        if (vv < -1e10) {
            return false;
        }
        if (vv > 1e10) {
            return false;
        }
        return value(r) == 0;
    }

    double getValue() const {
        return n / (double) d;
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

pii operator + (const pii &l, const pii &r) {
    return pii(l.x + r.x, l.y + r.y);
}

inline double cross(const pt &l, const pt &r) {
    return l.x * r.y - l.y * r.x;
}

inline double dot(const pt &l, const pt &r) {
    return l.x * r.x + l.y * r.y;
}

inline ll cross(const pii &l, const pii &r) {
    return l.x * r.y - l.y * r.x;
}

inline ll dot(const pii &l, const pii &r) {
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


bool is_sq(ll x) {
    for (ll i = 1; i * i <= x; ++i) {
        if (i * i == x) return true;
    }
    return false;
}

int p;
int sum;

map<vector<int>, int> dp;

int solve(vector<int> &cnt) {
    int s1 = accumulate(all(cnt), 0);
    if (s1 == 0) {
        return 0;
    }
    if (dp.count(cnt)) {
        return dp[cnt];
    }
    int s = 0;
    forn(i, p) {
        s += cnt[i] * i % p;
    }
    s %= p;

    int cur = sum - s;
    if (cur < 0) cur += p;
    int ret = 0;
    forn(i, p) {
        if (cnt[i] > 0) {
            cnt[i]--;
            ret = max(ret, solve(cnt));
            cnt[i]++;
        }
    }
    if (cur == 0) {
        ret++;
    }
    return dp[cnt] = ret;
}

void solve() {
    int n;
    cin >> n;
    cin >> p;
    vector<int> a(n);
    forn(i, n) {
        cin >> a[i];
    }
    sum = 0;
    forn(i, n) {
        sum += a[i] % p;
    }
    sum %= p;
    dp.clear();
    vector<int> cnt(p, 0);
    forn(i, n) {
        cnt[a[i] % p]++;
    }
    int ret = solve(cnt);
    cout << ret << "\n";
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
    cin >> t;
    forn(i, t) {
        cout << "Case #" << i + 1 << ": ";
        solve();
    }
    cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}
