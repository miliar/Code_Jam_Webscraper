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

double a[102][102];
double t[102][102];
int k[102], v[102];

void floyd(double a[][102], int n) {
    fori(k,1,n) {
        fori(i,1,n) {
            fori(j,1,n) {
                if ((a[i][k] + 1) > eps  && a[k][j] + 1 > eps && (a[i][k] + a[k][j] < a[i][j] || a[i][j] + 1 <= eps)) {
                    a[i][j] = a[i][k] + a[k][j];
                }
            }
        }
    }
}

void build_graph(int n) {
    fori(i,1,n) {
        fori(j,1,n) {
            if (a[i][j] + 1 > eps && a[i][j] <= k[i]) {
                t[i][j] = 1.0 * a[i][j] / v[i];
            }
            else t[i][j] = -1;
        }
    }
}

int main(){
    openread("C.inp");
    openwrite("C.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    cout.precision(6);
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        int n, q;
        cin >> n >> q;
        fori(i,1,n) cin >> k[i] >> v[i];
        fori(i,1,n) {
            fori(j,1,n) {
                cin >> a[i][j];
            }
        }
        floyd(a,n); // floyd on a
        build_graph(n);
        floyd(t,n);
        rep(i,q) {
            int x, y;
            cin >> x >> y;
            cout << fixed << t[x][y] << ' ';
        }
        cout << endl;
    }
}
