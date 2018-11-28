#include <bits/stdc++.h>
#include <time.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<ll> vi;
typedef pair<ll, ll> pii;
typedef vector<pii > vii;
typedef vector<vector<ll> > vvi;
typedef vector<vector<pair<ll, ll> > > vvii;

#define pb push_back
#define mp make_pair
#define fi first
#define se second
#define rep(i,s,e) for(ll i=(s);i<(e);++i)
#define repr(i,s,e) for(ll i=(e);i>(s);--i)
#define io ios::sync_with_stdio(false)

const ll MOD = 1e9+7;
const ll INF = 1e14;
const ll TE3 = 1005;
const ll TE5 = 100005;

bool PRINT_TIME_OF_EXEC = false;

ll n,q;
double ans;
double ff(ll x, ll s, ll md, ll d, double a, vii & h, vvi & v) {
  // cout<<n<<" "<<x<<" "<<s<<" "<<md<<" "<<d<<" "<<a<<endl;
  if(x==n-1) {
    ans=min(ans,a);
    return 0.0;
  }
  double y=1.0*MOD;
  ff(x+1,h[x].se,h[x].fi,v[x][x+1],a+(1.0*v[x][x+1]/h[x].se),h,v);
  if(d+v[x][x+1]<=md){
    ff(x+1,s,md,v[x][x+1]+d,a+(1.0*v[x][x+1]/s),h,v);
  }
  return 0;
}

int main() {
  io;
  ll start_time = clock();

  ll t;
  cin>>t;
  rep(ii,1,t+1) {
    // ll n,q;
    cin>>n>>q;
    vii h(n);
    rep(i,0,n) {
      cin>>h[i].fi>>h[i].se;
    }
    vvi v(n,vi(n));
    rep(i,0,n) {
      rep(j,0,n) {
        cin>>v[i][j];
      }
    }
    ll a,b,c,e,f;
    cin>>a>>b;
    c=0;
    e=h[0].se;
    rep(i,0,n-1) {
      c=v[i][i+1]/h[i].se;
    }
    ans=1.0*INF;
    ff(1,h[0].se,h[0].fi,v[0][1],1.0*v[0][1]/h[0].se,h,v);
    printf("Case #%lld: %.7lf\n",ii,ans);
    // cout<<ans<<endl;
  }



  ll end_time = clock();
  if(PRINT_TIME_OF_EXEC) cout<<"Time of exec. "<<((double)end_time-start_time)/CLOCKS_PER_SEC<<endl;
  return 0;
}
