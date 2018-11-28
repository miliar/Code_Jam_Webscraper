#include<cstdio>
#include<iostream>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 105
int T,a[maxn],b[maxn];
long long d[maxn][maxn];
double f[maxn][maxn];
#define inf 1e16
int main(){
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	scanf("%d",&T);
	for (int _=1;_<=T;_++) {
		printf("Case #%d: ",_);
		int n,q;
		scanf("%d%d",&n,&q);
		for (int i=1;i<=n;i++) scanf("%d%d",a+i,b+i);
		for (int i=1;i<=n;i++) 
			for (int j=1;j<=n;j++) scanf("%lld",d[i]+j);
		for (int i=1;i<=n;i++) 
			for (int j=1;j<=n;j++) f[i][j]=inf;
		for (int k=1;k<=n;k++) 
			for (int i=1;i<=n;i++) 
				if (i!=k&&d[i][k]>-1) 
					for (int j=1;j<=n;j++) 
						if (j!=i&&j!=k&&d[k][j]>-1) 
							if (d[i][j]==-1||d[i][j]>d[i][k]+d[k][j]) d[i][j]=d[i][k]+d[k][j];
		for (int i=1;i<=n;i++) 
			for (int j=1;j<=n;j++) 
				if (d[i][j]>-1&&d[i][j]<=a[i]) f[i][j]=d[i][j]*1.0/b[i];
		for (int k=1;k<=n;k++) 
			for (int i=1;i<=n;i++) 
				if (i!=k&&f[i][k]<inf) 
					for (int j=1;j<=n;j++) 
						if (j!=i&&j!=k&&f[k][j]<inf) 
							f[i][j]=min(f[i][j],f[i][k]+f[k][j]);
		while (q--) {
			int u,v;
			scanf("%d%d",&u,&v);
			printf("%.8lf ",f[u][v]);
		}
		puts("");
	}
	return 0;
}
