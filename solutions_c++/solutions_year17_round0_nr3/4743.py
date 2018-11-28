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

const double EPS = 1e-9;
const double PI = 3.141592653589793238462;

template<typename T>
inline T sq(T a) { return a * a; }

struct mystruct {
    ll val, mn, mx;

    inline bool operator <(const mystruct &other) const {
        if (mn == other.mn) {
            if (mx == other.mx)
                return val > other.val;
            return mx < other.mx;
        }
        return mn < other.mn;
    }
};

int main() {
    freopen("c-small2.in", "rt", stdin);
    freopen("c-small2.out", "wt", stdout);
    int t, tc = 1;
    scanf("%d", &t);
    while (t--) {
        ll n, k;
        scanf("%lld %lld", &n, &k);
        set<ll> mys;
        mys.insert(0);
        mys.insert(n + 1);
        priority_queue<mystruct> pq;

        ll what = (n + 1) / 2;
        pq.push((mystruct){what, min(what, n + 1 - what), max(what, n + 1 - what)});
        ll mxl, mnl;
        while (k--) {
            ll pos = pq.top().val;
            mxl = pq.top().mx;
            mnl = pq.top().mn;
            pq.pop();

            //printf("pos: %lld\n", pos);

            auto it = mys.insert(pos).fi;

            ll L = *prev(it), R = *next(it), what;
            if (L + 1 < pos) {
                what = (pos + L) / 2;
                pq.push((mystruct){what, min(what - L, pos - what), max(what - L, pos - what)});
            }

            if (pos + 1 < R) {
                what = (R + pos) / 2;
                pq.push((mystruct){what, min(what - pos, R - what), max(what - pos, R - what)});
            }
        }

        printf("Case #%d: %lld %lld\n", tc++, mxl - 1, mnl - 1);
    }
    return 0;
}

