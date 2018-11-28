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

const int minutes = 24 * 60;

bool busy[2][minutes];
int dp[minutes][minutes][2];

void fillbusy(int cnt, int id) {
    for (int i = 0; i < cnt; ++i) {
        int a, b; cin >> a >> b;
        while (a < b) {
            busy[id][a++] = true;
        }
    }
}

int main() {
    // FREOPEN("a");
    ios_base::sync_with_stdio(false); cin.tie(0);

    int Q; cin >> Q;
    for (int T = 1; T <= Q; ++T) {
        memset(busy, 0, sizeof(busy));

        int ac, aj; cin >> ac >> aj;
        fillbusy(ac, 0);
        fillbusy(aj, 1);

        int best = inf;
        for (int i = 0; i < 2; ++i) {
            memset(dp, 0x3f, sizeof(dp));
            dp[0][0][i] = 0;
            for (int m0 = 0; m0 < minutes; ++m0)
                for (int m1 = 0; m1 < minutes; ++m1)
                    if (m0 + m1 && m0 + m1 <= minutes) {
                        const int curmin = m0 + m1 - 1;
                        if (!busy[0][curmin]) {
                            int& d = dp[m0][m1][0];
                            if (m0) {
                                d = min(d, dp[m0 - 1][m1][0]);
                                d = min(d, dp[m0 - 1][m1][1] + 1);
                            }
                        }
                        if (!busy[1][curmin]) {
                            int& d = dp[m0][m1][1];
                            if (m1) {
                                d = min(d, dp[m0][m1 - 1][0] + 1);
                                d = min(d, dp[m0][m1 - 1][1]);
                            }
                        }
                        //E(m0); E(m1); E(dp[m0][m1][0]); Eo(dp[m0][m1][1]);
                    }
            
            //E(i); E(dp[minutes / 2][minutes / 2][0]); Eo(dp[minutes / 2][minutes / 2][1]);
            const int midmin = minutes / 2;
            best = min(best, dp[midmin][midmin][i]);
            best = min(best, dp[midmin][midmin][1 - i] + 1);
        }

        printf("Case #%d: %d\n", T, best);
    }

    return 0;
}
