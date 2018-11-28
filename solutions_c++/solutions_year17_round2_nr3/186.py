#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<algorithm>
#include<queue>
#include<map>
#include<cmath>
#define ll long long
using namespace std;
int t;
int n,q,x,y;
ll e[110],s[110],d[110][110];
double f[110][110],dp[110][110];
int ans;
int main(){
	scanf("%d",&t);
	for (int I=1;I<=t;I++){
		scanf("%d%d",&n,&q);
		for (int i=1;i<=n;i++) scanf("%d%d",&e[i],&s[i]);
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++) scanf("%d",&d[i][j]);
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					if (d[i][k]!=-1 && d[k][j]!=-1){
						if (d[i][j]==-1 || d[i][j]>d[i][k]+d[k][j])
							d[i][j]=d[i][k]+d[k][j];
					}
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				if (i==j) f[i][j]=0;
				else if (d[i][j]<=e[i])
					f[i][j]=d[i][j]*1.0/s[i];
				else f[i][j]=-1;
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					if (f[i][k]!=-1 && f[k][j]!=-1){
						if (f[i][j]==-1 || f[i][j]>f[i][k]+f[k][j])
							f[i][j]=f[i][k]+f[k][j];
					}
		printf("Case #%d:",I);
		while (q--){
			scanf("%d%d",&x,&y);
			printf(" %.9f",f[x][y]);
		}
		
		printf("\n",I,dp[n]);
	}
    return 0;
}

