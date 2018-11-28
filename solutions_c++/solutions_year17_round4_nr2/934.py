#include <iostream>
#include <cstring>
#include <set>
#include <map>
#include <list>
#include <queue>
#include <stack>
#include <bitset>
#define _USE_MATH_DEFINES
#include <math.h>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <assert.h>
#include <stdlib.h>
using namespace std;

void smain();
int main() {
    ios_base::sync_with_stdio(0);
#ifdef TASK
    freopen("/Users/ramis/Downloads/B-small-attempt0.in.txt","rt",stdin);
    //freopen(TASK".in","rt",stdin);
    freopen(TASK".out","wt",stdout);
    const clock_t start = clock();
#endif
    smain();
#ifdef TASK
    cerr << "\nTotal Execution Time: " << float( clock () - start ) /  CLOCKS_PER_SEC << endl;
#endif
    return 0;
}

#ifndef M_PI
#define M_PI 3.14159265358979311599796346854418516
#endif
#define forn(i,n) for (int i=0;i<n;i++)
#define rforn(i,n) for (int i=n-1;i>=0;i--)
#define int long long
#define LL long long
#define mp(a,b) make_pair(a,b)
#define MOD 1000000007
#define EPS 1E-9
#define N 200002
/* --------- END TEMPLATE CODE --------- */
int p[N], b[N];
vector<int> a[N];
int o[N];
int n, c, m;

int calc(int x) {
    vector<vector<bool>> d(x, vector<bool>(n));
    vector<set<int> > s(x);
    forn(i, x) forn(j, n) s[i].insert(j);
    int res = 0;
    forn(_i, c) {
        int i = o[_i];
        vector<int> rem;
        for (auto j : a[i]) {
            int t = 0;
            for (; t < x && d[t][j]; ++t);
            if (t < x) { 
                d[t][j] = 1;
                s[t].erase(j);
            } else {
                rem.push_back(j);
            }
        }
        for (auto j : rem) {
            int r = -1, vr = -1;
            for (int t = 0; t < x; ++t) {
                auto it = s[t].lower_bound(j);
                if (it == s[t].begin()) continue;
                it = prev(it);
                if (*it > vr) vr = *it, r = t;
            }
            if (r == -1) return -1;
            s[r].erase(vr);
            res += 1;
        }
    }
    return res;
}

pair<int, int> solve() {
    forn(i, c) o[i] = i;
    sort(o, o + c, [](int i, int j) { return a[i].size() > a[j].size(); });
    int l = 0, r = m;
    forn(i, c) l = max(l, (int)a[i].size());
    while (l < r) {
        int x = (l + r) / 2;
        int y = calc(x);
        if (y == -1) l = x + 1;
        else r = x;
    }
    return {l, calc(l)};
}

void smain() {
    cin >> n;
    for (int cas = 1; cin >> n >> c >> m; ++cas) {
        forn(i, c) a[i].clear();
        forn(i, m) {
            cin >> p[i] >> b[i], p[i] -= 1, b[i] -= 1;
            a[b[i]].push_back(p[i]);
        }
        auto res = solve();
        cout << "Case #" << cas << ": " << res.first << ' ' << res.second << '\n';
        cerr << "Case #" << cas << ": " << res.first << ' ' << res.second << '\n';
    }
}
