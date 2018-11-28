#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second
#define mp make_pair
#define pb push_back
#define pf push_front
#define iter(v, i) for (__typeof__((v).begin()) i = (v).begin(); i != (v).end(); i++)
#define fast_io_without_cstdio ios_base::sync_with_stdio(false), cin.tie(NULL)
#define all(v) (v).begin(), (v).end()

#ifdef __linux__
#define gc getchar_unlocked
#define pc putchar_unlocked
#else
#define gc getchar
#define pc putchar
#endif

#if __cplusplus <= 199711L
template<class BidirIt>
BidirIt prev(BidirIt it, typename iterator_traits<BidirIt>::difference_type n = 1) {
    advance(it, -n);
    return it;
}

template<class ForwardIt>
ForwardIt next(ForwardIt it, typename iterator_traits<ForwardIt>::difference_type n = 1) {
    advance(it, n);
    return it;
}
#endif

typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long double ldouble;

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

template<typename T>
inline T sq(T a) { return a * a; }

const int MAXN = 1005;

struct horse {
    ldouble x;
    ldouble v;
} ar[MAXN];
int d, n;

inline bool comp(const horse &a, const horse &b) {
    return a.x < b.x;
}

inline ldouble get_time(const horse a, const horse b) {
    return (b.x - a.x) / (a.v - b.v);
}

bool intersect(horse a, horse b) {
    ldouble dt = get_time(a, b);
    if (dt < 0.0000000) return false;
    if (a.x + dt * a.v > ( ldouble )d) return false;
    return true;
}

bool can(ldouble vel) {
    horse annie;
    annie.x = 0;
    annie.v = vel;

    vector<horse> vec(ar, ar + n);
    for (int i = n - 2; i >= 0; i--) {
        if (intersect(ar[i], ar[i + 1])) {
            vec.pb((horse){get_time(ar[i], ar[i + 1]) * ar[i].v + ar[i].x,
                            min(ar[i].v, ar[i + 1].v)});
        }
    }

    for (auto it : vec)
        if (intersect(annie, it))
            return false;
    return true;
}

int main() {
    freopen("a-large.in", "rt", stdin);
    freopen("a-large.out", "wt", stdout);
    int t;
    cin >> t;
    for (int tc = 1; tc <= t; tc++) {
        cin >> d >> n;
        for (int i = 0; i < n; i++)
            cin >> ar[i].x >> ar[i].v;
        sort(ar, ar + n, comp);
        ldouble lo = 0.0, hi = 1e18;
        for (int i = 0; i < 1000; i++) {
            ldouble mid = (lo + hi) / 2.0;
            if (can(mid))
                lo = mid;
            else
                hi = mid;
        }
        cout << "Case #" << tc << ": " << setprecision(7) << fixed << lo << endl;
    }
    return 0;
}

