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
        cout << std::fixed << std::setprecision(10);
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

const int MAXN = 1001;
vector<int> g[MAXN];
int match[MAXN];
bool used[MAXN];

bool dfs(int v) {
    if (used[v])
        return false;
    used[v] = true;
    for (int to : g[v]) {
        if (match[to] == -1 || dfs(match[to])) {
            match[to] = v;
            return true;
        }
    }
    return false;
}

int a[MAXN], b[MAXN];
int rm[MAXN];

int32_t main() {

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; ++tt) {

        int nn, c, m, n = 0, k = 0;
        cin >> nn >> c >> m;
        dbg(nn, c, m);
        for (int i = 0; i < m; ++i) {
            int p, w;
            cin >> p >> w;
            if (w == 1)
                a[n++] = p;
            else
                b[k++] = p;
        }

        for (int i = 0; i < n; ++i) {
            g[i].clear();
            for (int j = 0; j < k; ++j)
                if (a[i] != b[j])
                    g[i].pb(j);
        }

        std::fill(match, match + k, -1);
        std::fill(rm, rm + n, -1);
        memset(used, 0, sizeof used);

        vector<char> used_greedy(n, false);
        for (int i = 0; i < n; ++i)
            for (int to : g[i])
                if (match[to] == -1) {
                    match[to] = i;
                    used_greedy[i] = true;
                    break;
                }

        for (int i = 0; i < n; ++i)
            if (!used_greedy[i] && dfs(i))
                memset(used, 0, sizeof used);


        int ans = 0, kal = 0;
        for (int i = 0; i < k; ++i) { 
            if (match[i] != -1) {
                rm[match[i]] = i;
                ++ans;
            }
        }
        dbg(ans);
        bool ones = false;
        int cup = 0, cdo = 0;
        for (int i = 0; i < n; ++i)
            if (rm[i] == -1) {
                ++cup;
                if (a[i] == 1)
                    ones = 1;
                // dbg(ones, a[i]);
            }
        for (int i = 0; i < k; ++i)
            if (match[i] == -1) {
                ++cdo;
                if (b[i] == 1)
                    ones = 1;
                // dbg(ones, b[i]);
            }
        // if (cup == 0 || cdo == 0) {
        //     ans += max(cup, cdo);
        // } else {
            dbg(ones, cup, cdo);
            if (ones)
                ans += cup + cdo;
            else
                ans += max(cup, cdo), kal += min(cup, cdo);
        // }
        cout << "Case #" << tt << ": " << ans << ' ' << kal << '\n';
    }


    return 0;
}
