#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define all(c) (c).begin(), (c).end()
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define eb emplace_back
#define mp make_pair

typedef long long int ll;
typedef vector<int> vi;
typedef pair<int,int> pii;

const ll INF = 4e18;
const int N = 111;

int n;
ll d[N][N], e[N], s[N];
double ans[N][N];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    cout << fixed << setprecision(12);
    int T; cin >> T;
    forn(cas,T) {
        cout << "Case #" << cas+1 << ":";
        int q; cin >> n >> q;
        forn(i,n) cin >> e[i] >> s[i];
        forn(i,n) forn(j,n) {
            cin >> d[i][j];
            if (d[i][j] == -1) d[i][j] = INF;
        }
        forn(k,n) forn(i,n) forn(j,n) d[i][j] = min(d[i][j], d[i][k] + d[k][j]);


        fill(ans[0], ans[n], 1e200);
        forn(i,n) ans[i][i] = 0;
        forn(i,n) forn(j,n){ 
            if (d[i][j] <= e[i]) 
                ans[i][j] = min(ans[i][j], d[i][j] / (double) s[i]);
        }
        forn(k,n) forn(i,n) forn(j,n) ans[i][j] = min(ans[i][j], ans[i][k] + ans[k][j]);

        while (q--) {
            int u,v; cin >> u >> v;
            u--; v--;
            cout << ' ' << ans[u][v];
        }
        cout << endl;
    }


    return 0;
}
