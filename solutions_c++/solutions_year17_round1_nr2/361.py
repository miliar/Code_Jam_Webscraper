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

// n <= 50
// p <= 50
// np <= 1000
int n,p;
int r[52];
int q[52][52];
queue<int> Q[52];

inline int getlow(int x,int v){
  return (10 * v + 11 * x - 1) / (11 * x);
}
inline int gethigh(int x,int v){
  return 10 * v / (9 * x);
}

void solve(){
  scanf("%d%d",&n,&p);
  REP(i,n)scanf("%d",r+i);
  REP(i,n)REP(j,p)scanf("%d",&q[i][j]);
  REP(i,n)sort(q[i],q[i]+p);
  REP(i,n)REP(j,p){
    // calc low and high
    int v = q[i][j];
    int low = getlow(r[i],v);
    int high = gethigh(r[i],v);
    if(low <= high){
      Q[i].push(v);
    }
  }
  int ans = 0;
  while(true){
    bool exist = true;
    int minid = -1;
    int minhigh = 1e9;
    int low = -1, high = 1e9;
    REP(i,n){
      if(Q[i].empty()){
        exist = false;
        break;
      }
      int v = Q[i].front();
      CHMAX(low, getlow(r[i],v));
      int yo = gethigh(r[i],v);
      CHMIN(high, yo);
      if(yo < minhigh){
        minhigh = yo;
        minid = i;
      }
    }
    if(!exist)break;
    if(low <= high){
      ans ++;
      REP(i,n)Q[i].pop();
    }else{
      Q[minid].pop();
    }
  }
  // queue flush
  REP(i,n)while(Q[i].size())Q[i].pop();
  printf("%d\n",ans);
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
