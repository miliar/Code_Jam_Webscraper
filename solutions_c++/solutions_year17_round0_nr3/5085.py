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
        cerr << std::fixed << std::setprecision(10);
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

struct comp {
    bool operator()(const pii & a, const pii & b) {
        return a.ss - a.ff == b.ss - b.ff ? a.ff < b.ff : a.ss - a.ff > b.ss - b.ff;
    }
};

int32_t main() {

    int t;
    cin >> t;

    for (int tt = 1; tt <= t; ++tt) {
        int n, k;
        cin >> n >> k;
        set<pii, comp> s;
        s.insert({1, n});
        int l, r;
        for (int i = 0; i < k; ++i) {
            auto it = s.begin();
            auto p = *it;
            s.erase(it);
            int tl = p.ff, tr = p.ss;
            int len = tr - tl + 1;
            --len;
            l = len / 2;
            r = len - l;
            int tm = tl + tr >> 1;
            if (tl <= tm - 1)
                s.insert({tl, tm - 1});
            if (tm + 1 <= tr)
                s.insert({tm + 1, tr});
        }
        cout << "Case #" << tt << ": " << r << ' ' << l << '\n';
    }


    return 0;
}
