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
    ios_base::sync_with_stdio(false); cin.tie(0);

    int T; cin >> T;
    for (int tt = 1; tt <= T; ++tt) {
        string s; cin >> s;
        int k; cin >> k;

        int res = 0;
        for (int i = 0; i + k <= Sz(s); ++i) {
            if (s[i] == '-') {
                ++res;
                for (int j = 0; j < k; ++j)
                    s[i+j] = s[i+j] == '-' ? '+' : '-';
            }
        }

        bool ok = true;
        for (char c : s) if (c == '-') {
            ok = false;
            break;
        }

        cout << "Case #" << tt << ": ";
        if (ok)
            cout << res;
        else
            cout << "IMPOSSIBLE";
        cout << endl;
    }


    return 0;
}
