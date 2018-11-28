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
const int MAXN = 1123;
const ld PI = 4.0L * atan(1);
ll dp[MAXN][MAXN];
pair<ll, ll> arr[MAXN];
ll sq(ll a) {
    return(a*a);
}
int main() {
    int t,i,n,k,tt,j;
    cin>>t;
    FOR(tt,1,t) {
        cin>>n>>k;
        FOR(i,0,n-1) {
            cin>>arr[i].first>>arr[i].second;
        }
        sort(arr, arr + n);
        memset(dp, 0LL, sizeof(dp));
        dp[0][1] = (arr[0].first)*(arr[0].second);
        FOR(i,1,n-1) {
            FOR(j,1,i+1) {
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-1] + (arr[i].first)*(arr[i].second));
            }
        }
        /*
        FOR(i,0,n-1) cout<<arr[i].first<<" "<<arr[i].second<<" ";
        cout<<endl;
        FOR(i,0,n-1) {
            FOR(j,0,n) cout<<dp[i][j]<<" ";
            cout<<endl;
        }
        */
        ll ans = 0LL;
        debug(k);
        FOR(i,0,n-1) {
            debug(ans);
            debug(arr[i].first);
            debug(dp[i][k]);
            ans = max(ans, (sq(arr[i].first) + 
                        ((((i==0)?(0LL):(dp[i-1][k-1])) + (arr[i].first)*(arr[i].second))<<1LL)
                        )
                    );
        }
        debug(ans);
        ld pans = ld(ans) * PI;
        cout<<"Case #"<<tt<<": "<<fixed<<setprecision(11)<<pans<<endl;
    }
    return 0;
}
