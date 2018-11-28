#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef pair<ll, ll> P;

#define fi first
#define se second
#define repl(i,a,b) for(ll i=(ll)(a);i<(ll)(b);i++)
#define rep(i,n) repl(i,0,n)
#define each(itr,v) for(auto itr:v)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define dbg(x) cout<<#x"="<<x<<endl
#define mmax(x,y) (x>y?x:y)
#define mmin(x,y) (x<y?x:y)
#define maxch(x,y) x=mmax(x,y)
#define minch(x,y) x=mmin(x,y)
#define uni(x) x.erase(unique(all(x)),x.end())
#define exist(x,y) (find(all(x),y)!=x.end())
#define bcnt __builtin_popcount

#define INF INT_MAX/3

P dp[2222][777][2];
int a,b;
int pa[2222],pb[2222];

int main(){
	cin.sync_with_stdio(false);
  int cases;
  cin>>cases;
  repl(hoge,1,cases+1){
    memset(pa,0,sizeof(pa));
    memset(pb,0,sizeof(pb));
    rep(i,2222)rep(j,777)rep(k,2)dp[i][j][k]=P(INF,-1);
    cin>>a>>b;
    rep(i,a){
      int s,t;
      cin>>s>>t;
      repl(j,s,t)pa[j]=1;
    }
    rep(i,b){
      int s,t;
      cin>>s>>t;
      repl(j,s,t)pb[j]=1;
    }
    if(!pa[0])dp[0][0][0]=P(0,0);
    if(!pb[0])dp[0][0][1]=P(0,1);
    rep(i,1440+2)rep(j,720+2)rep(k,2){
      if(k==0){
        if(!pa[i+1])minch(dp[i+1][j+1][0],dp[i][j][0]);
        if(!pb[i+1])minch(dp[i+1][j+1][1],P(dp[i][j][0].fi+1,dp[i][j][0].se));
      }else{
        if(!pb[i+1])minch(dp[i+1][j][1],dp[i][j][1]);
        if(!pa[i+1])minch(dp[i+1][j][0],P(dp[i][j][1].fi+1,dp[i][j][1].se));
      }
    }
    printf("Case #%lld: %lld\n", hoge,min(dp[1440][720][0].fi+(dp[1440][720][0].se!=0?1:0),dp[1440][720][1].fi+(dp[1440][720][1].se!=1?1:0)));
  }
	return 0;
}
