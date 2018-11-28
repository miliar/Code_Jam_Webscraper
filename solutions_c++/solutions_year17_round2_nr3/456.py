#include<bits/stdc++.h>
#define MAX 1000000000005
using namespace std;
long long e[105],sp[105];
long long d[105][105];
double rd[105][105];
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("output_C-large.txt","w",stdout);
	int t,n,q,k,i,j,kb,num=1,u,v;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d",&n,&q);
		for(i=1;i<=n;i++)
			scanf("%lld%lld",&e[i],&sp[i]);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
			{
				scanf("%lld",&d[i][j]);
				if(d[i][j]==-1) d[i][j]=MAX;
			}
		for(k=1;k<=n;k++)
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
					d[i][j]=min(d[i][j],d[i][k]+d[k][j]);
		for(i=1;i<=n;i++)
			for(j=1;j<=n;j++)
			{
				if(e[i]>=d[i][j]) rd[i][j]=(double)d[i][j]/sp[i];
				else rd[i][j]=MAX;
			}
		for(k=1;k<=n;k++)
			for(i=1;i<=n;i++)
				for(j=1;j<=n;j++)
					rd[i][j]=min(rd[i][j],rd[i][k]+rd[k][j]);
		printf("Case #%d: ",num++);
		while(q--)
		{
			scanf("%d%d",&u,&v);
			printf("%f ",rd[u][v]);
		}
		printf("\n");

	}

}