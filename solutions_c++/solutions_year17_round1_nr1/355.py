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

char cake[35][35];
bool used[35][35];

void solve(){
  int r,c;
  scanf("%d%d",&r,&c);
  REP(i,r)scanf("%s",cake[i]);
  REP(i,r)REP(j,c)used[i][j] = false;
  REP(i,r)REP(j,c){
    if(used[i][j])continue;
    if(cake[i][j]=='?')continue;
    char cc = cake[i][j];
    // yoko ni nobasu
    int hidari = j, migi = j;
    while(hidari > 0){
      if(cake[i][hidari-1]!='?')break;
      hidari--;
    }
    while(migi < c-1){
      if(cake[i][migi+1]!='?')break;
      migi++;
    }
    // tate ni nobasu
    int ue = i, shita = i;
    while(ue > 0){
      bool ok = true;
      FOR(volga,hidari,migi+1){
        if(cake[ue-1][volga]!='?')ok=false;
      }
      if(!ok)break;
      ue--;
    }
    while(shita < r-1){
      bool ok = true;
      FOR(hakase,hidari,migi+1){
        if(cake[shita+1][hakase]!='?')ok=false;
      }
      if(!ok)break;
      shita++;
    }
    // update
    FOR(oyurushi,ue,shita+1)FOR(kudasai,hidari,migi+1){
      used[oyurushi][kudasai] = true;
      cake[oyurushi][kudasai] = cc;
    }
  }
  REP(okashisukikai,r)puts(cake[okashisukikai]);
}

int main(){
  int t;
  scanf("%d",&t);
  REP(i,t){
    printf("Case #%d:\n",i+1);
    solve();
  }
  return 0;
}
