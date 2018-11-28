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
    openread("C.inp");
    openwrite("C.out");
    ios_base::sync_with_stdio(0);
    int T;
    cin >> T;
    rep(test,T) {
        cout << "Case #" << test+1 << ": ";
        ll n , k;
        cin >> n >> k;
        ll parity[2] = {0,0};
        ll paritysmall[2] = {0,0};
        parity[n%2] = 1;
        if (k == 1) {
            cout << n/2 << ' ' << (n-1)/2 << endl;
            continue;
        }
        k--;
        ll l = 1;
        while (k>0) {
            ll p, q;
            if (n%2==1) {
                p = parity[1] * 2 + paritysmall[0];
                q = paritysmall[0];
            }
            else {
                p = parity[0];
                q = paritysmall[1] * 2 + p;
            }
            n = n/2;
            l *= 2;
            parity[0] = parity[1] = 0;
            paritysmall[0] = paritysmall[1] = 0;
            parity[n%2] = p;
            paritysmall[(n-1)%2] = q;
            if (k<=p) {
                k = 0;
                cout << n/2 << ' ' << (n-1)/2 << endl;
            }
            else if (k <= l) {
                k = 0;
                cout << (n-1)/2 << ' ' << (n-2)/2 << endl;
            }
            else {
                k -= l;
            }
        }
    }
}
