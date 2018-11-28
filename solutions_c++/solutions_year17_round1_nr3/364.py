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

int hd,ad,hk,ak,b,d;

void solve(){
  scanf("%d%d%d%d%d%d",&hd,&ad,&hk,&ak,&b,&d);
  int ans = 1e9;
  REP(td,101)REP(tb,101){
    int tmp = 0;
    bool ok = true;
    int q=hd, w=ad, e=hk, r=ak;
    REP(_,td){
      if(q<=r-d){
        q = hd-r; tmp++;
      }
      r -= d; q -= r; tmp++;
      if(q<=0){
        ok = false; break;
      }
    }
    if(!ok)continue;
    REP(_,tb){
      if(q<=r){
        q = hd-r; tmp++;
      }
      w += b; q -= r; tmp++;
      if(q<=0){
        ok = false; break;
      }
    }
    if(!ok)continue;
    while(e>0){
      tmp++;
      e-=w; if(e<=0)break;
      if(q<=r){
        q = hd-r; tmp++;
      }
      q-=r;
      if(q<=0){
        ok = false; break;
      }
    }
    if(ok)CHMIN(ans,tmp);
  }
  if(ans==1e9){
    puts("IMPOSSIBLE");
  }else{
    printf("%d\n",ans);
  }
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d: ",i+1);
    solve();
    fflush(stdout);
  }
  return 0;
}
