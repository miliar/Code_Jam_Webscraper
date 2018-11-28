#include<bits/stdc++.h>
#define rep(i,N) for(int i=0;i<N;i++)
#define fori(i,a,b) for(ll i=a,_b=b;i<=_b;i++)
#define ford(i,a,b) for(ll i=a,_b=b;i>=_b;i--)
#define foreach(it,a) for(__typeof(a.begin()) it=a.begin(); it!=a.end(); ++it)
#define outarray(a,n) REP(i,n) cout << a[i] << ' '
#define outarray(a,x,y) fori(i,x,y) cout << a[i]
#define openread(s) freopen(s,"r",stdin)
#define openwrite(s) freopen(s,"w",stdout)
#define filla(a,x) memset(a,x,sizeof(a))
#define pb push_back
#define sqr(a) (a)*(a)
#define mp(x,y) make_pair(x,y)
#define pb push_back
#define fi first
#define	se second
#define endl "\n"
using namespace std;
typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<pii> vii;
typedef vector<int> vi;
const double eps=1e-8;
const ll lloo=1e18;
const int oo=1e9;
const double pi = acos(-1);

pair<ll,ll> a[10000];
double f[1001][1001];

int main(){
    openread("A.inp");
    openwrite("A.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    cout.precision(6);
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        int n, k;
        cin >> n >> k;
        rep(i,n) cin >> a[i].first >> a[i].second;
        sort(a,a+n);
        reverse(a,a+n);
        rep(i,n) {
            if (i == 0) f[i][1] = pi * sqr(a[i].fi) + 2 * pi * a[i].fi * a[i].se;
            else f[i][1] = max(f[i-1][1], pi * sqr(a[i].fi) + 2 * pi * a[i].fi * a[i].se);
            fori(j,2,k) {
                f[i][j] = max(f[i-1][j],f[i-1][j-1] + 2 * pi * a[i].fi * a[i].se);
            }
        }
        cout << fixed << f[n-1][k] << endl;
    }
}
