#include <bits/stdc++.h>

using namespace std;
const double INF=DBL_MAX;
const double eps=1e-6;
int t,tc=0,q,n,u,v;double D[110][110],MD[110][110];
double E[110],S[110],memo[110][110];
double f(int i,int j){
	if (i==v) return 0;
	if (memo[i][j]!=-1.0) return memo[i][j];
	double ans;
	if (D[i][i+1]+MD[j][i]<=E[j]) ans= min(f(i+1,j)+D[i][i+1]/S[j],f(i+1,i)+D[i][i+1]/S[i]);
	else ans=f(i+1,i)+D[i][i+1]/S[i];
	return memo[i][j]=ans;
}
int main(){
	scanf("%d",&t);
	while(t--){
		scanf("%d%d",&n,&q);
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				memo[i][j]=-1.0;
		for (int i=0;i<n;i++) scanf("%lf%lf",&E[i],&S[i]);
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				scanf("%lf",&D[i][j]),MD[i][j]=(D[i][j]!=-1?D[i][j]:INF);
		for (int i=0;i<n;i++)
			for (int j=0;j<n;j++)
				for (int k=0;k<n;k++)
					MD[j][k]=min(MD[j][k],MD[j][i]+MD[i][k]);
		printf("Case #%d:",++tc);
		while(q--){
			scanf("%d%d",&u,&v);u--,v--;
			printf(" %lf",f(1,0)+D[0][1]/S[0]);
		}
		printf("\n");
	}
	return 0;
}
