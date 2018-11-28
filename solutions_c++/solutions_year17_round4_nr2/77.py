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

int n,m,c;

int NO = -125283025;
int calc(int x,vi cnt){
  if(cnt[0]>x)return NO;
  int izumi = 0;
  int prom = 0;
  FOR(i,1,n){
    if(cnt[i]<=x)continue;
    while(true){
      if(izumi==i)return NO;
      if(cnt[izumi]==x){
        izumi++;
        continue;
      }
      int need = cnt[i] - x;
      int rest = x - cnt[izumi];
      if(need <= rest){
        cnt[i] -= need;
        cnt[izumi] += need;
        prom += need;
        break;
      }else{
        cnt[i] -= rest;
        cnt[izumi] += rest;
        prom += rest;
      }
    }
  }
  return prom;
}

void solve(){
  scanf("%d%d%d",&n,&c,&m);
  map<int,int> sum;
  vi cnt(n,0);
  REP(i,m){
    int p,b;
    scanf("%d%d",&p,&b);
    --p;--b;
    sum[b]++;
    cnt[p]++;
  }
  int low = 0;
  for(auto P : sum){
    CHMAX(low,P.second);
  }
  low--;
  int high = 1024;
  while(low+1<high){
    int x = (low+high)/2;
    // make it lower than x
    int po = calc(x,cnt);
    if(po!=NO){
      high = x;
    }else{
      low = x;
    }
  }
  int ans1 = high;
  int ans2 = calc(ans1,cnt);
  printf("%d %d\n",ans1,ans2);
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
