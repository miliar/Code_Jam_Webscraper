#include<bits/stdc++.h>
using namespace std;
#define PI 3.141592653589793
pair<double,double> p[1000];
int n,k;
double vis[1001][1001];
double solve(int idx,int k){
	if(!k)return p[idx-1].first*p[idx-1].first;
	if(idx==n)return 0.0;
	if(vis[idx][k]!=-1)return vis[idx][k];
	return vis[idx][k]=max(p[idx].first*p[idx].second*2+solve(idx+1,k-1),solve(idx+1,k));
}
int main(){
	freopen("A-large.in","r",stdin);
	int t;
	scanf("%d",&t);
	for(int T=1;T<=t;T++){
		double ans=0;//,h=0,ans2=0;
		//memset(vis,-1,sizeof vis);
		for(int i=0;i<1001;i++)
			for(int j=0;j<1001;j++)
				vis[i][j]=-1;
		scanf("%d%d",&n,&k);
		for(int i=0;i<n;i++)
			scanf("%lf%lf",&p[i].first,&p[i].second);
		sort(p,p+n);
		ans=solve(0,k)*PI;
		printf("Case #%d: %.6lf\n",T,ans);
	}
}