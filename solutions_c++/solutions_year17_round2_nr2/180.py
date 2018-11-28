#include <bits/stdc++.h>
using namespace std;
#define REP(i, n) for (int i = 0; i < (int) (n); i++)
#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define maximize(a, b) ((a)<(b)?(a)=(b),1:0)
#define minimize(a, b) ((a)>(b)?(a)=(b),1:0)

void input();
void solve(int cs);

int main(int argc, char* argv[]) {
    if (argc == 1) freopen("input.txt", "r", stdin);
    int tc;
    cin >> tc;
    int l = 1, r = tc;
    if (argc > 1) {
        freopen(argv[2], "w", stdout);
        int n = atoi(argv[1]), i = atoi(argv[2]);
        l = tc / n * i + 1;
        r = i+1<n ? tc/n*(i+1) : tc;
    }
    for (int cs = 1; cs <= tc; cs++) {
        input();
        if (cs >= l && cs <= r) solve(cs);
    }
    return 0;
}

int n, r, o, y, g, b, v;
char R = 'R', O = 'O', Y = 'Y', G = 'G', B = 'B', V = 'V';

void input() {
    cin >> n >> r >> o >> y >> g >> b >> v;
}


void solve(int cs) {
    cout << "Case #" << cs << ": ";
    if (o > b || g > r || v > y) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if ( (o && o == b && o + b < n) ||
         (g && g == r && g + r < n) ||
         (v && v == y && v + y < n) ) {

        cout << "IMPOSSIBLE" << endl;
        return;
    }
    
    if (o && o == b) {
        string ans;
        REP(i, o) { ans += O; ans += B; }
        cout << ans << endl;
        return;
    }
    if (g && g == r) {
        string ans;
        REP(i, g) { ans += G; ans += R; }
        cout << ans << endl;
        return;
    }
    if (v && v == y) {
        string ans;
        REP(i, v) { ans += V; ans += Y; }
        cout << ans << endl;
        return;
    }


    vector<string> S[256];
    string s;
    if (o) { s = ""; REP(i, o) s += B, s += O; s += B; S['B'].pb(s); REP(i, b-1-o) S['B'].pb("B");}
    else REP(i, b) S['B'].pb("B");
    if (g) { s = ""; REP(i, g) s += R, s += G; s += R; S['R'].pb(s); REP(i, r-1-g) S['R'].pb("R");}
    else REP(i, r) S['R'].pb("R");
    if (v) { s = ""; REP(i, v) s += Y, s += V; s += Y; S['Y'].pb(s); REP(i, y-1-v) S['Y'].pb("Y");}
    else REP(i, y) S['Y'].pb("Y");

    
    vector<pair<int, char> > a = {mp(S['R'].size(), 'R'), mp(S['Y'].size(), 'Y'), mp(S['B'].size(), 'B')};
    sort(a.begin(), a.end());
    if (a[0].fi + a[1].fi < a[2].fi) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    else {
        string ans;
        REP(i, a[2].fi) ans += a[2].se;
        REP(i, a[0].fi) ans.insert(ans.begin() + 2*i+1, a[0].se);
        REP(i, a[1].fi) ans.insert(ans.end() - 2*i, a[1].se);

        string res;
        REP(i, ans.size()) {
            res += S[ans[i]].back();
            S[ans[i]].pop_back();
        }
        cout << res << endl;
    }
}

