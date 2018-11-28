#include <bits/stdc++.h>
//#define DEBUG
#define si(n) scanf("%d",&n)
#define sl(n) cin>>n
#define sf(n) scanf("%f",&n)
#define pn(n) printf("%d\n",n)
#define ps(n) printf("%d ",n)
#define pln(n) cout<<n<<endl
#define pnl() printf("\n")
#define pls(n) cout<<n<<" "
#define pl(n) cout<<n
#define FOR(i,j,n) for(i=j;i<=n;i++)
#define FORR(i,j,n) for(i=j;i>=n;i--)
#define SORT(n) std::sort(n.begin(),n.end())
#define FILL(n,a) std::fill(n.begin(),n.end(),a)
#define ALL(n) n.begin(),n.end()
#define rsz resize
#define pb push_back
#define MAXINT std::numeric_limits<int>::max()
#define MININT std::numeric_limits<int>::min()
#define gc getchar_unlocked
#define pc putchar_unlocked
#define iOS std::ios_base::sync_with_stdio(false)
#define endl "\n"
#define INF 1000000000000000005LL
#define INFI 1009990000
#ifdef DEBUG
    #define debugHello() cout << "Hello" << endl
#else
    #define debugHello()
#endif
#ifdef DEBUG
    #define debug(x) cout << #x << " = " << x << endl
#else
    #define debug(x)
#endif
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef vector<bool> vb;
typedef vector<vector<int> > vvi;
typedef vector<vector<ll> > vvl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
const ld eps = 0.0000001L;
/**************** TEMPLATE ENDS HERE *************************/
const int MAXN = 151234;
int main() {
    int tt,t,n,i;
    ld d,k,s;
    cin>>t;
    FOR(tt,1,t) {
        cin>>d>>n;
        ld ans = -1.0L;
        FOR(i,0,n-1) {
            cin>>k>>s;
            if (ans == -1.0L) {
                ans = (d-k)/s;
            } else {
                ans = max(ans, (d-k)/s);
            }
        }
        cout<<"Case #"<<tt<<": "<<fixed<<setprecision(15)<<(d/ans)<<endl;
    }
    return 0;
}
