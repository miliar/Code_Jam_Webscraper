#include <bits/stdc++.h>
using namespace std;

#ifdef ILIKEGENTOO
#   define Eo(x) { cerr << #x << " = " << (x) << endl; }
#   define E(x) { cerr << #x << " = " << (x) << "   "; }
#   define FREOPEN(x)
#else
#   define Eo(x) {}
#   define E(x) {}
#   define FREOPEN(x) (void)freopen(x ".in", "r", stdin);(void)freopen(x ".out", "w", stdout);
#endif
#define EO(x) Eo(x)
#define Sz(x) (int((x).size()))
#define All(x) (x).begin(),(x).end()

template<class A, class B> ostream &operator<<(ostream &os, const pair<A, B>& p) { return os << '(' << p.first << ", " << p.second << ')'; }

template<class C> void operator<<(vector<C> &v, const C &x){v.push_back(x);}
template<class D> void operator>>(vector<D> &v, D &x){assert(!v.empty()); x=v.back(); v.pop_back();}
template<class E> void operator<<(set<E> &v, const E &x){v.insert(x);}

typedef double flt;
typedef long long int64;
typedef unsigned long long uint64;
typedef pair<int, int> pii;

const int inf = 0x3f3f3f3f;
const int64 inf64 = 0x3f3f3f3f3f3f3f3fLL;
const flt eps = 1e-8;
const flt pi = acos(-1.0);
const int dir[4][2] = { {0, 1}, {1, 0}, {0, -1}, {-1, 0} };

constexpr inline int bit(int t) { return 1 << t; }



int main() {
    // FREOPEN("a");
    ios_base::sync_with_stdio(false); cin.tie(0);

    int Q; cin >> Q;
    for (int T = 1; T <= Q; ++T) {
        int n, k; cin >> n >> k;
        vector<double> r(n, 0.0), h(n, 0.0);

        for (int i = 0; i < n; ++i) {
            cin >> r[i] >> h[i];
        }

        double best = 0.0;
        for (int j = 0; j < n; ++j) {
            double maxr = r[j];
            double maxh = h[j];
            vector<double> hs;

            for (int i = 0; i < n; ++i) {
                if (r[i] > maxr)
                    continue;
                if (i == j)
                    continue;

                const double ph = 2 * M_PI * r[i] * h[i];
                hs.push_back(ph);
            }
            if (Sz(hs) < k - 1)
                continue;

            sort(All(hs), greater<double>());
            double ans = maxr * maxr * M_PI + 2 * M_PI * maxr * maxh;
            for (int i = 0; i < k - 1; ++i)
                ans += hs[i];

            best = max(best, ans);
        }


        printf("Case #%d: %.20lf\n", T, best);
    }

    return 0;
}
