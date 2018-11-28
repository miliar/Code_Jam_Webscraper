#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cstring>

using namespace std;

const int MAXN=109;

int a[4],ans,n,m,i,j,k;
int f[MAXN][MAXN][MAXN][4];

int er() {
	return a[0] + (a[1]>0?a[1]/2+a[1]%2:0);
}

int san() {
	ans = a[0];
	int g[MAXN],o;
	j=k=0;
	if (a[1]>a[2]) o = 1;
	else o = 2;
	while (a[1]>0 || a[2]>0) {
		if (a[o]>0) {
			g[k++] = o;
			a[o]--;
		}
		else {
			g[k++] = 3-o;
			a[3-o]--;
		}
		o = 3-o;
	}
	for (i=0;i<k;i++)
	{	
		if (j==0) ans++;
		j = (g[i]+j)%m;
	}
	return ans;
}

void update(int &r,int a, int b, int c,int d,int x)
{
	int v = (d-x+m)%m;
	int res = f[a][b][c][v]+(v>0?0:1);
	if (f[a][b][c][v] >=0 && res>r) r=res;
}

int si() {
	memset(f,-1,sizeof(f));
	
	f[0][0][0][0] = 0;
	
	for (i=0;i<=a[1];i++)
		for (j=0;j<=a[2];j++)
			for (k=0;k<=a[3];k++)
				for (int d=0;d<4;d++)
				{
					if (i!=0) update(f[i][j][k][d],i-1,j,k,d,1);
					if (j!=0) update(f[i][j][k][d],i,j-1,k,d,2);
					if (k!=0) update(f[i][j][k][d],i,j,k-1,d,3);
				}
	return max(max(f[a[1]][a[2]][a[3]][0], f[a[1]][a[2]][a[3]][3]),max(f[a[1]][a[2]][a[3]][1],f[a[1]][a[2]][a[3]][2]))+a[0];
}

int main()
{
	freopen("A-large (1).in", "r",stdin);
	freopen("a.out","w",stdout);
	int DAT;
	scanf("%d",&DAT);
	for (int cas=1;cas<=DAT;cas++)
	{
		memset(a,0,sizeof(a));
		printf("Case #%d: ",cas);
		scanf("%d%d",&n,&m);
		for (i=1;i<=n;i++) {
			scanf("%d",&j);
			a[j%m]++;
		}
		if (m==2) printf("%d\n",er());
		if (m==3) printf("%d\n",san());
		if (m==4) printf("%d\n",si());
	}
	return 0;
}
