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

// mod
const ll MOD = 1000000007ll;
#define FIX(a) ((a)%MOD+MOD)%MOD

// floating
typedef double Real;
const Real EPS = 1e-11;
#define EQ0(x) (abs(x)<EPS)
#define EQ(a,b) (abs(a-b)<EPS)
typedef complex<Real> P;

ll next(ll x){
  if(x < 10)return x;
  // itos
  string s = "";
  while(x > 0){
    s = string(1,'0'+(x%10)) + s;
    x /= 10;
  }
  // modify
  int mx = 0;
  REP(i,s.size()){
    int y = s[i] - '0';
    CHMAX(mx, y);
    s[i] = '0' + mx;
  }
  // stoi
  ll ret = 0;
  REP(i,s.size()){
    ret *= 10;
    ret += s[i]-'0';
  }
  return ret;
}

void solve(){
  ll n;
  cin>>n;
  ll low = 1, high = n+1;
  while(low+1 < high){
    ll mid = (low+high)/2;
    if(next(mid) <= n){
      low = mid;
    }else{
      high = mid;
    }
  }
  printf("%lld\n",next(low));
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
