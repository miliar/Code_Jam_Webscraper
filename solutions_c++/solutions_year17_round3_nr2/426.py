#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN=1500;
const int oo=1000000000;

int f[MAXN][MAXN/2][2],a[MAXN],ans,x[MAXN],y[MAXN];
int i,j,k,n,m;

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int DAT;
	scanf("%d",&DAT);
	for (int cas=1;cas<=DAT;cas++)
	{
		ans=oo;
		memset(a,0,sizeof(a));
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++)
		{
			scanf("%d%d",x+i,y+i);
			for (j=x[i]+1;j<=y[i];j++)
				a[j]=1;
		}
		for (i=1;i<=m;i++)
		{
			scanf("%d%d",x+i,y+i);
			for (j=x[i]+1;j<=y[i];j++)
				a[j]=-1;
		}
		//1
		if (a[1]!=-1)
		{
			for (i=0;i<=1440;i++)
				for (j=0;j<=720;j++)
					f[i][j][0]=f[i][j][1]=oo;
			f[1][1][0]=0;
			for (i=1;i<=1440;i++)
				for (j=0;j<=min(720,i);j++)
				{
					if (i-j>720 || (f[i][j][0]>=4 && f[i][j][1]>=4)) continue;
					//1
					for (k=i+1;k<=min(1440,i+720);k++)
					{
						if (a[k]==-1) break;
						if (k-i+j>720) break;
						f[k][k-i+j][0]=min(f[k][k-i+j][0],min(f[i][j][0],f[i][j][1]+1));
					}
					//-1
					for (k=i+1;k<=min(1440,i+720);k++)
					{
						if (a[k]==1) break;
						if (k-j>720) break;
						f[k][j][1]=min(f[k][j][1],min(f[i][j][0]+1,f[i][j][1]));
					}
				}
			ans=min(ans,f[1440][720][0]);
			ans=min(ans,f[1440][720][1]+1);
		}
		//-1
		if (a[1]!=1)
		{
			for (i=0;i<=1440;i++)
				for (j=0;j<=720;j++)
					f[i][j][0]=f[i][j][1]=oo;
			f[1][0][1]=0;
			for (i=1;i<=1440;i++)
				for (j=0;j<=min(720,i);j++)
				{
					if (i-j>720 || (f[i][j][0]>=ans && f[i][j][1]>=ans)) continue;
					//1
					for (k=i+1;k<=min(1440,i+720);k++)
					{
						if (a[k]==-1) break;
						if (k-i+j>720) break;
						f[k][k-i+j][0]=min(f[k][k-i+j][0],min(f[i][j][0],f[i][j][1]+1));
					}
					//-1
					for (k=i+1;k<=min(1440,i+720);k++)
					{
						if (a[k]==1) break;
						if (k-j>720) break;
						f[k][j][1]=min(f[k][j][1],min(f[i][j][0]+1,f[i][j][1]));
					}
				}
			ans=min(ans,f[1440][720][0]+1);
			ans=min(ans,f[1440][720][1]);
		}
		printf("Case #%d: %d\n",cas, ans);
	}
	return 0;
}