//Name     : Hemant Mangla
//Username : hkmangla
//College  : DCRUST Murthal
//Country  : India
 
#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
#define IN(s) freopen(s,"r",stdin)
#define OUT(s) freopen(s,"w",stdout)
# define PI   3.14159265358979323846
#define pll pair<ll,ll>
#define pii pair<int,int>
#define pdd pair<double,double>
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define MEM(a,x) memset(a,x,sizeof(a))
#define foreach( gg,itit )  for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define mp make_pair
#define pb push_back
#define all(s) s.begin(),s.end()
#define present(c,x) ((c).find(x) != (c).end())
const double EPS = 1e-8;
const int mod = 1e9+7;
const int N = 1e6+10;
const ll INF = 1e18;
		 
ll power(ll x,ll y,ll m){
  ll t=1;
  while(y>0){
    if(y%2) y-=1,t=t*x%m;
    else y/=2,x=x*x%m;
  }
  return t;
}
vector<pdd> rh;
int n,k;
double dp[1003][1003];
int dp2[1003][1003];
double solve(int idx,int total){
	if(total == k) return 0.0;
	if(idx >= n) return -1e18;
	if(dp2[idx][total] != -1)  return dp[idx][total];
	dp2[idx][total] = 1;
	if(total == 0){
		return dp[idx][total] = max(solve(idx+1,total), 
			PI*rh[idx].X*rh[idx].X + 2.0*PI*rh[idx].X*rh[idx].Y + solve(idx+1,total+1));
	}
	else return dp[idx][total] = max(solve(idx+1,total), 
		2.0*PI*rh[idx].X*rh[idx].Y + solve(idx+1,total+1));
}
int main(){
	IN("input.txt");
	OUT("output.txt");
	int t; cin>>t;
	REPP(tt,1,t+1){
		cin>>n>>k;
		rh.clear();
		REP(i,n+2) REP(j,n+2) {
			dp[i][j] = -1;
			dp2[i][j] = -1;
		}
		double x,y;
		REP(i,n) {
			cin>>x>>y;
			rh.pb(mp(x,y));
		}
		sort(all(rh));
		reverse(all(rh));
		printf("Case #%d: %0.9lf\n",tt,solve(0,0));
	}
return 0;
}