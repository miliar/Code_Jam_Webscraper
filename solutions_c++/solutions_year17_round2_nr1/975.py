#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<ll, ll> P;
typedef pair<ll, P> PPI;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb(s) push_back(s)
#define mp(a,b) make_pair(a,b)
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define maxch(x,y) x=max(x,y)
#define minch(x,y) x=min(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt(x) bitset<32>(x).count()

#define INF INT_MAX/3

ll n;
double d;
double k[1111],s[1111];

bool ok(double x){
  double t=d/x;
  rep(i,n){
    double tt=(d-k[i])/s[i];
    if(tt>t)return false;
  }
  return true;
}

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  rep(hoge,cases){
    cin>>d>>n;
    rep(i,n)cin>>k[i]>>s[i];
    double lb=0,ub=1e18;
    rep(i,300){
      double mid=(lb+ub)/2.0;
      if(ok(mid))lb=mid;
      else ub=mid;
    }
    printf("Case #%lld: %.10f\n", hoge+1,lb);
  }
	return 0;
}
