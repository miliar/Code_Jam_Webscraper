#include<bits/stdc++.h>
#define rep(i,N) for(int i=0;i<N;i++)
#define fori(i,a,b) for(ll i=a,_b=b;i<=_b;i++)
#define ford(i,a,b) for(ll i=a,_b=b;i>=_b;i--)
#define foreach(it,a) for(__typeof(a.begin()) it=a.begin(); it!=a.end(); ++it)
#define outarray(a,n) REP(i,n) cout << a[i] << ' '
#define outarray(a,x,y) fori(i,x,y) cout << a[i]
#define openread(s) freopen(s,"r",stdin)
#define openwrite(s) freopen(s,"w",stdout)
#define filla(a) memset(a,0,sizeof(a))
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

int main(){
    openread("A.inp");
    openwrite("A.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        string s;
        int k;
        cin >> s;
        cin >> k;
        int res = 0;
        rep(i,s.size()) {
            if (s[i] == '-') {
                if (i+k-1 < s.size()) {
                    res++;
                    fori(j,i,i+k-1) {
                        if (s[j] == '-') s[j] = '+';
                        else s[j] ='-';
                    }
                }
            }
        }
        int lc = 0;
        rep(i,s.size()) {
            if (s[i] == '-') lc = 1;
        }
        if (lc == 1) {
            cout << "IMPOSSIBLE" << endl;
        }
        else cout << res << endl;
    }
}
