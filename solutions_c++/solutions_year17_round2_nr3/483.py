#pragma GCC optimize("O3")
#include <bits/stdc++.h>

using std::cerr;
using std::cin;
using std::cout;

using std::abs;
using std::min;
using std::max;
using std::swap;

using std::map;
using std::pair;
using std::set;
using std::string;
using std::vector;

using ll = long long;
using uint = unsigned int;
using pii = pair<int, int>;
using pll = pair<ll, ll>;

#define ff first
#define ss second
#define pb emplace_back
#define sqr(x) ((x) * (x))
#ifdef LOCAL
#define dbg(as...) {\
    vector<string> _v; \
    std::stringstream _ss(#as);\
    string _cur, _loc;\
    while (getline(_ss, _cur, ',')) {\
        while (count(_cur.begin(), _cur.end(), '(') != count(_cur.begin(), _cur.end(), ')')) {\
            getline(_ss, _loc, ',');\
            _cur += "," + _loc;\
        }\
    _v.pb(_cur);\
    }\
    err(_v.begin(), as);\
}
#else
#define dbg(as...)
#endif

template<typename T>
void err(vector<string>::iterator it, T a) {
    cerr << it->substr((*it)[0] == ' ') << " = " << a << '\n';
}
template<typename T, typename...Ts>
void err(vector<string>::iterator it, T a, Ts...as) {
    cerr << it->substr((*it)[0] == ' ') << " = " << a << ", ";
    err(++it, as...);
}

struct init {
    init() {
        cin.tie(0);
        std::iostream::sync_with_stdio(0);
        cout << std::fixed << std::setprecision(6);
        cerr << std::fixed << std::setprecision(3);
        #ifdef LOCAL
        srand(300); 
        #else
        srand(time(0));
        #endif
    }
    ~init() {
        cerr << "Time elapsed: " << (double)clock() / CLOCKS_PER_SEC << "s.\n";
    }
} init;

#define int ll
#define double long double
const int MAXN = 101, INF = 1e12;
int d[MAXN][MAXN];
double g[MAXN][MAXN];
int e[MAXN]; double s[MAXN];

int32_t main() {

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; ++tt) {

        int n, q;
        cin >> n >> q;
        for (int i = 1; i <= n; ++i)
            cin >> e[i] >> s[i];

        for (int i = 1; i <= n; ++i)
            for (int j = 1; j <= n; ++j) {
                cin >> d[i][j];
                if (d[i][j] < 0) d[i][j] = INF;
            }

        for (int k = 1; k <= n; ++k) 
            for (int i = 1; i <= n; ++i) 
                for (int j = 1; j <= n; ++j) {
                    int pot = d[i][k] + d[k][j];
                    if (d[i][j] > pot)
                        d[i][j] = pot;
                }

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (e[i] >= d[i][j]) {
                    g[i][j] = d[i][j] / s[i];
                }
                else {
                    g[i][j] = INF;
                }
            }
        }

        for (int k = 1; k <= n; ++k)
            for (int i = 1; i <= n; ++i)
                for (int j = 1; j <= n; ++j) {
                    double pot = g[i][k] + g[k][j];
                    if (g[i][j] > pot)
                        g[i][j] = pot;
                }

        cout << "Case #" << tt << ":";
        while (q--) {
            int u, v;
            cin >> u >> v;
            cout << ' ' << g[u][v];
        }
        cout << '\n';
    }


    return 0;
}
