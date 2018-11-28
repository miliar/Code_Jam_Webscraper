#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <sstream>
#include <cmath>

using namespace std;


typedef long long ll;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<string> vs;
typedef vector< vector<int> > vvi;
typedef vector<ll> vl;
typedef vector< vector<ll> > vvl;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forv(i, v) forn(i, v.size())
#define all(v) v.begin(), v.end()
#define mp make_pair
#define pb push_back

const ll INF = 1e15;


void solveCase(int tc) {
    printf("Case #%d: ", tc);
    cerr << tc << endl;
    int n, q;
    cin >> n >> q;
    vl e(n);
    vl s(n);
    forn(i, n) cin >> e[i] >> s[i];
    vvl d(n, vl(n));
    forn(i, n) {
        forn(j, n) {
            cin >> d[i][j];
            if (d[i][j] == -1) d[i][j] = INF;
        }
        d[i][i] = 0;
    }
    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                d[i][j] = min(d[i][j], d[i][k] + d[k][j]);
            }
        }
    }
    vector< vector<ld> > D(n, vector<ld>(n, 1e20));
    
    forn(i, n) {
        forn(j, n) {
            if (d[i][j] <= e[i]) {
                D[i][j] = d[i][j] * 1.0 / s[i];
            }
        }
    }
    forn(k, n) {
        forn(i, n) {
            forn(j, n) {
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]);
            }
        }
    }
    cout.precision(10);
    cout << fixed;
    forn(i, q) {
        int u, v;
        cin >> u >> v;
        u--, v--;
        cout << D[u][v];
        if (i < q - 1) cout << " "; else cout << endl;
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int tc; cin >> tc;
    forn(it, tc) solveCase(it + 1);
    return 0;
}
