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

int mark[20000];
int f[20000][3][721][3];

int main(){
    openread("B.in");
    openwrite("B.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        int n, m, x, y;
        cin >> n >> m;
        filla(mark,0);
        rep(i,n) {
            cin >> x >> y;
            fori(i,x,y-1) mark[i] = 1;
        }
        rep(i,m) {
            cin >> x >> y;
            fori(i,x,y-1) mark[i] = 2;
        }
        int k = 1439;
        fori(j,0,720) fori(z,1,2) f[0][1][j][z] = oo, f[0][2][j][z] = oo;
        if (mark[0] == 1) {
            f[0][1][1][1] = oo;
            f[0][2][0][2] = 1;
        }
        else if (mark[0] == 2) {
//            cout << "a1" << endl;
            f[0][1][1][1] = 1;
            f[0][2][0][2] = oo;
        }
        else {
            f[0][1][1][1] = 1;
            f[0][2][0][2] = 1;
        }
        fori(i,1,k) {
            fori(z,1,2) {
                if (mark[i]==0&&mark[i-1]==0) {
    //                cout << "a3" << endl;
                    f[i][2][0][z] = f[i-1][2][0][z];
                    f[i][1][0][z] = oo;
                    fori(j,1,720) {
                        f[i][1][j][z] = min(f[i-1][1][j-1][z], f[i-1][2][j-1][z] + 1);
                        f[i][2][j][z] = min(f[i-1][2][j][z], f[i-1][1][j][z] + 1);
                    }
                }
                else if (mark[i]==0) {
    //                cout << "a2" << endl;
                    if (3 - mark[i-1] == 2) f[i][2][0][z] = f[i-1][2][0][z];
                    else f[i][2][0][z] = oo;
                    f[i][1][0][z] = oo;
                    fori(j,1,720) {
                        int x = j;
                        if (mark[i-1] == 1) x--;
                        f[i][mark[i-1]][j][z] = f[i-1][3 - mark[i-1]][x][z] + 1;
                        x = j;
                        if (3 - mark[i-1] == 1) x--;
                        f[i][3-mark[i-1]][j][z] = f[i-1][3-mark[i-1]][x][z];
                    }
                }
                else {
    //                cout << "a4" << endl;
                    f[i][1][0][z] = oo;
                    if (3 - mark[i] == 2) f[i][2][0][z] = f[i-1][2][0][z];
                    else f[i][2][0][z] = oo;
                    fori(j,1,720) {
                        f[i][mark[i]][j][z] = oo;
                        int x = j;
                        if (3 - mark[i] == 1) x--;
                        f[i][3-mark[i]][j][z] = min(f[i-1][3-mark[i]][x][z], f[i-1][mark[i]][x][z] + 1);
                    }
                }
            }
        }
        cout << min(min(min(f[k][1][720][1] - 1,f[k][1][720][2]),f[k][2][720][1]),f[k][2][720][2] - 1) << endl;
    }
}
