#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
#define fore(i,a,b) for(int i=a,ThxDem=b;i<ThxDem;++i)
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
double ar(double r) {
	return M_PI*r*r;
}
int n,k;
const double PI=4.*atan(1);
ii p[1024];
double r[1024],h[1024];
bool vis[1024][1024];
double dp[1024][1024];
double f(int i, int u) {
	if(i==n&&u) return -(double)1e14;
	if(u==0) return 0;
	if(vis[i][u]) return dp[i][u];
	vis[i][u]=1;
	double b=M_PI*r[i]*h[i]*2.;
	double ans=f(i+1,u);
	ans=max(ans,f(i+1,u-1)+b);
	return dp[i][u]=ans;
}
int main(){
	int tn;
	scanf("%d",&tn);
	fore(tc,0,tn){
		scanf("%d%d",&n,&k);
		fore(i,0,n) scanf("%d%d",&p[i].fst,&p[i].snd);
		sort(p,p+n);reverse(p,p+n);
		fore(i,0,n) r[i]=p[i].fst,h[i]=p[i].snd;
		memset(vis,0,sizeof vis);
		double ans=0;
		fore(i,0,n) ans=max(ans,f(i+1,k-1)+ar(r[i])+M_PI*r[i]*h[i]*2.);
		printf("Case #%d: %.15lf\n",tc+1,ans);
	}
	return 0;
}
