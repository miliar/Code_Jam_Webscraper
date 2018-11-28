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
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef long long i64;
typedef unsigned long long ull;

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
    ld x, y, z;

    pt() = default;

    pt(ld x, ld y, ld z) : x(x), y(y), z(z) {}

    inline pt operator-(const pt &r) const {
        return pt(x - r.x, y - r.y, z - r.z);
    }

    inline pt operator+(const pt &r) const {
        return pt(x + r.x, y + r.y, z + r.z);
    }

    inline pt operator*(const ld &r) const {
        return pt(x * r, y * r, z * r);
    }

    inline pt operator -() const {
        return pt(-x, -y, -z);
    }

    inline ld sqlen() const {
        return fabsl(x * x + y * y + z * z);
    }
};

ostream &operator<<(ostream &os, const pt &p) {
    return os << "(" << p.x << "," << p.y << "," << p.z << ")";
}

inline pt cross(const pt &l, const pt &r) {
    return pt(l.y * r.z - l.z * r.y,
              l.z * r.x - l.x * r.z,
              l.x * r.y - l.y * r.x);
}

inline ld dot(const pt &l, const pt &r) {
    return l.x * r.x + l.y * r.y + l.z * r.z;
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

string solve() {
    string s;
    cin >> s;
    string ans;
    if (string(s.length(), '1') <= s) {
        forn(i, s.length()) {
            string cur = s.substr(0, i + 1) + string(s.length() - i - 1, s[i]);
            if (cur > s) {
                return s.substr(0, i) + char(s[i] - 1) + string(s.length() - i - 1, '9');
            }
        }
        return s;
    } else {
        return string(s.length() - 1, '9');
    }
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
        string res = solve();
        cout << "Case #" << i + 1 << ": ";
        cout << res << "\n";
    }
    cerr << "Time " << clock() / (double) CLOCKS_PER_SEC << endl;
    return 0;
}
