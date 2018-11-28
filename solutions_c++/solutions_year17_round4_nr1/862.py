//IIT Kanpur FacelessMen India
#pragma GCC optimize("O3")
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;

//#define DEBUG
ll power(ll x,ll y){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%mod;
    else y/=2,x=x*x%mod;
  }
  return t;
}
#ifdef DEBUG
#define dprintf(fmt,...) fprintf(stderr,fmt,__VA_ARGS__)
#else
#define dprintf(fmt,...)
#endif

int dp[111][111][111],sp[110][110];
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(i,101) REP(j,101) REP(k,101){
    dp[i+1][j][k+1]=max(dp[i+1][j][k+1],dp[i][j][k]+1);
    dp[i+2][j+1][k]=max(dp[i+2][j+1][k],dp[i][j][k]+1);
    dp[i][j+2][k]=max(dp[i][j+2][k],dp[i][j][k]+1);
    dp[i][j+1][k+2]=max(dp[i][j+1][k+2],dp[i][j][k]+1);
    dp[i][j][k+4]=max(dp[i][j][k+4],dp[i][j][k]+1);
    dp[i+4][j][k]=max(dp[i+4][j][k],dp[i][j][k]+1);
  }
  REP(i,101) REP(j,101){
    sp[i+3][j]=max(sp[i+3][j],sp[i][j]+1);
    sp[i][j+3]=max(sp[i][j+3],sp[i][j]+1);
    sp[i+1][j+1]=max(sp[i+1][j+1],sp[i][j]+1);
  }
  REP(aa,t){
    int a[4];
    FILL(a,0);
    int n,p; scanf("%d%d",&n,&p);
    int su=0;
    REP(i,n){
      int x; scanf("%d",&x);
      a[x%p]++;
      su+=x;
    }
    int ans = a[0]-(su%p==0)+1;
    //printf("%d %d %d\n",a[1],a[2],sp[a[1]][a[2]]);
    if(p==2) ans+=a[1]/2;
    else if(p==3) ans+=sp[a[1]][a[2]];
    else ans+=dp[a[1]][a[2]][a[3]];
    printf("Case #%d: %d\n",aa+1,ans);
  }  
  return 0;
}
