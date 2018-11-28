#include<cstdio>
#include<algorithm>
#include<cstring>
#define fo(i,a,b) for(int i=a;i<=b;i++)
#define fd(i,a,b) for(int i=a;i>=b;i--)
using namespace std;
const int N=210;
int e[N],s[N];
double d[N][N];
int main()
{
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	scanf("%d",&T);
	int c=0;
	while (T--)
	{
		printf("Case #%d: ",++c);
		int n,q;
		scanf("%d%d",&n,&q);
		fo(i,1,n) scanf("%d%d",&e[i],&s[i]);
		fo(i,1,n)
		{
			fo(j,1,n)
			scanf("%lf",&d[i][j]);
		}
		fo(i,1,n)
			fo(j,1,n)
				fo(k,1,n)
				if (d[j][i]!=-1 && d[i][k]!=-1 && (d[j][k]==-1 || d[j][i]+d[i][k]<d[j][k]))
				d[j][k]=d[j][i]+d[i][k];
		fo(i,1,n)
			fo(j,1,n)
			if (d[i][j]!=-1)
			if (d[i][j]<=e[i]) d[i][j]/=s[i]; else d[i][j]=-1;
		fo(i,1,n)
			fo(j,1,n)
				fo(k,1,n)
				if (d[j][i]!=-1 && d[i][k]!=-1 && (d[j][k]==-1 || d[j][i]+d[i][k]<d[j][k]))
				d[j][k]=d[j][i]+d[i][k];
		fo(i,1,q)
		{
			int x,y;
			scanf("%d%d",&x,&y);
			printf("%.8f ",d[x][y]);
		}
		printf("\n");
	}
} 
