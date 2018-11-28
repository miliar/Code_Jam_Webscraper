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

char s[100][100];
int u[100][100];
int main(){
  // freopen("product.in","r",stdin);
  // freopen("product.out","w",stdout);
  int t; scanf("%d",&t);
  REP(aa,t){
    int r,c; scanf("%d%d",&r,&c);
    REP(i,r) scanf("%s",s[i]);
    
    FILL(u,0);
    REP(i,r) REP(j,c) if(s[i][j]!='?') u[i][j]=1; 
    REP(i,r) REP(j,c) if(u[i][j]){
      int l=i,e=i;
      while(l&&s[l-1][j]=='?') l--;
      while(e<r-1&&s[e+1][j]=='?') e++;
      int p=j;
      while(p+1<c){
        int f=1;
        REPP(k,l,e+1) if(s[k][p+1]!='?') f=0;
        if(f==0) break;
        p++;
      }
      REPP(k,l,e+1) REPP(a,j,p+1) s[k][a]=s[i][j];
    }
    for(int j=c-1;j>=0;j--)for(int i=r-1;i>=0;i--) if(s[i][j]=='?') s[i][j]=s[i][j+1];
    REP(i,r) REP(j,c) assert(s[i][j]!='?');
    printf("Case #%d:\n",aa+1);
    REP(i,r) printf("%s\n",s[i]);
  }
  return 0;
}
