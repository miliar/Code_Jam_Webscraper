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

int main() {
  io;
  ll start_time = clock();

  ll t;
  cin>>t;
  double d,n;
  ll a,b;
  double c,e,f;
  rep(ii,1,t+1) {
    cin>>d>>n;
    vii v;
    rep(j,0,n) {
      cin>>a>>b;
      v.pb(mp(a,b));
    }
    e=0;
    sort(v.begin(),v.end());
    for(ll i=n-1;i>=0;--i) {
      a=1.0*v[i].fi;
      b=1.0*v[i].se;
      c=(1.0*d-a)/b;
      e=max(e,c);
    }
    // cout<<e<<endl;
    double ans=1.0*d/e;
    // cout<<"Case #"<<ii<<": ";
    printf("Case #%lld: %.7lf\n",ii,ans);
  }


  ll end_time = clock();
  if(PRINT_TIME_OF_EXEC) cout<<"Time of exec. "<<((double)end_time-start_time)/CLOCKS_PER_SEC<<endl;
  return 0;
}
