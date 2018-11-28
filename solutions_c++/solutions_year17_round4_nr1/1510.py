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

char F[101][101][101][101][4];
int cnt[4];

char dp(char n0, char n1, char n2, char n3, char k, char P) {
    if (n0<0||n1<0||n2<0||n3<0) return 127;
    if (n0==0&&n1==0&&n2==0&&n3==0) {
        if (k==0) return 0;
        return 127;
    }
    if ((unsigned int)F[n0][n1][n2][n3][k]<127) return F[n0][n1][n2][n3][k];
    char x = min(dp(n0-1,n1,n2,n3,k,P),min(dp(n0,n1-1,n2,n3,((k-1)%P+P)%P,P),min(dp(n0,n1,n2-1,n3,((k-2)%P+P)%P,P),dp(n0,n1,n2,n3-1,((k-3)%P+P)%P,P))));
    if (k!=0&&((unsigned int)x)<127) x++;
    F[n0][n1][n2][n3][k] = x;
    return x;
}

int main(){
    openread("A.inp");
    openwrite("A.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        int n, p;
        cin >> n >> p;
        filla(cnt,0);
        filla(F,255);
        int k = 0;
        rep(i,n) {
            int x;
            cin >> x;
            cnt[x%p]++;
            k = (k + x) % p;
        }
        int res = dp(cnt[0],cnt[1],cnt[2],cnt[3],k,p);
        if (k!=0) res--;
        cout << n - res << endl;
    }
}
