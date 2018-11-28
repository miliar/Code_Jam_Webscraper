#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <iomanip>
#include <map>
using namespace std;

#define forn(i, n) for(int i = 0; i < (n); ++i)
#define forv(i, a) forn(i, (int)(a).size())

typedef long long lng;

int n, q;
int e[2000];
int s[2000];
int d[200][200];

void read()
{
    cin >> n >> q;
    forn(i, n) {
        cin >> e[i] >> s[i];
    }

    forn(i, n) forn(j, n) {
        cin >> d[i][j];
    }

    int x, y;
    cin >> x >> y;
}

struct state {
    double t;
    int e, s;

    state(double t, int e, int s) : t(t), e(e), s(s){}
};

double get_mint(const vector<state>& vec) {
    int idx = -1;
    forv(i, vec) {
        if (idx < 0 || vec[i].t < vec[idx].t) {
            idx = i;
        }
    }

    return vec[idx].t;
}

double solve() {
    read();

    vector<state> vec[2];
    int t = 0;

    vec[0].reserve(n);
    vec[1].reserve(n);

    state first = {1.0 * d[0][1]/s[0], e[0] - d[0][1], s[0]};
    vec[t].push_back(first);

    for(int i = 1; i < n - 1; ++i) {
        double mint = get_mint(vec[t]);
        vec[t].emplace_back(mint, e[i], s[i]);

        vec[1 - t].clear();
        forv(idx, vec[t]) {
            state& cur = vec[t][idx];
            if (cur.e - d[i][i+1] >= 0) {
                vec[1-t].emplace_back(cur.t + 1.0*d[i][i+1]/cur.s, cur.e - d[i][i+1], cur.s);
            }
        }

        t = 1 - t;
    }

    return get_mint(vec[t]);
}


int main () {
    ios_base::sync_with_stdio(false);
    cin.tie(0); 

    int T;
    cin >> T;
    forn(tc, T) {
        auto res = solve();

        std::cout << "Case #" << tc + 1 << ": " << setprecision(7) << fixed << res << endl;
    }
    
    return 0;
}
