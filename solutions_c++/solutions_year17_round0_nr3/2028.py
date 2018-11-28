#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vl;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

typedef int _loop_int;
#define REP(i,n) for(_loop_int i=0;i<(_loop_int)(n);++i)
#define FOR(i,a,b) for(_loop_int i=(_loop_int)(a);i<(_loop_int)(b);++i)
#define FORR(i,a,b) for(_loop_int i=(_loop_int)(b)-1;i>=(_loop_int)(a);--i)

#define DEBUG(x) cout<<#x<<": "<<x<<endl
#define DEBUG_VEC(v) cout<<#v<<":";REP(i,v.size())cout<<" "<<v[i];cout<<endl
#define ALL(a) (a).begin(),(a).end()

#define CHMIN(a,b) a=min((a),(b))
#define CHMAX(a,b) a=max((a),(b))

void solve(){
  ll n,k;
  cin>>n>>k;
  ll x = 1;
  k--;
  while(k >= x){
    k -= x;
    n -= x;
    x <<= 1;
  }
  ll mn = n/x;
  ll mx = (n+x-1)/x;
  ll rest = n%x;
  // DEBUG(k);
  // DEBUG(rest);
  ll ans = k<rest ? mx : mn;
  ans--;
  ll a = (ans+1)/2;
  ll b = ans-a;
  printf("%lld %lld\n",a,b);
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
  }
  return 0;
}
