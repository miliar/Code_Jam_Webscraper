#include <bits/stdc++.h>
#define INF 0x3f3f3f3f3f3f3f3fll
using namespace std;
long long dis[105][105];
double speed[105];
long long upup[105];
double tt[105][105];
int main(){
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,ca=0;
	scanf("%d",&T);
	int n,q;
	while(T--){
		scanf("%d%d",&n,&q);
		memset(dis,0x3f,sizeof dis);
		for (int i=1;i<=n;i++)
			scanf("%lld%lf",&upup[i],&speed[i]);
		for (int i=1;i<=n;i++)
			dis[i][i]=0;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++){
				long long x;
				scanf("%lld",&x);
				if (x!=-1) dis[i][j] = x;
			}
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);

		printf("Case #%d: ",++ca );
		for (int i=0;i<=100;i++)
			for (int j=0;j<=100;j++)
					tt[i][j]=1e20;
		for (int i=1;i<=n;i++)
			for (int j=1;j<=n;j++)
				if (dis[i][j]<=upup[i]) {
					tt[i][j]=((double)dis[i][j])/((double)speed[i]);
				}
		for (int k=1;k<=n;k++)
			for (int i=1;i<=n;i++)
				for (int j=1;j<=n;j++)
					tt[i][j]=min(tt[i][j],tt[i][k]+tt[k][j]);

		while (q--){
			int uu,vv;
			scanf("%d%d",&uu,&vv);;
			printf("%.10f",tt[uu][vv] );
			if (q) printf(" ");
			else puts("");
		}
	}
	return 0;
}