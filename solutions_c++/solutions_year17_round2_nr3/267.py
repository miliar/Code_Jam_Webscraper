#include<cstdio>
#include<algorithm>
#define fo(i,a,b) for(int i=a;i<=b;i++)
using namespace std;

typedef long long LL;

const int maxn=105;
const double inf=1e18;

int n,Q,e[maxn],s[maxn];
LL d[maxn][maxn];

int T;
double f[maxn][maxn];
int main()
{
	//freopen("C.in","r",stdin);
	//freopen("C.out","w",stdout);
	
	scanf("%d",&T);
	fo(Ti,1,T)
	{
		printf("Case #%d: ",Ti);
		
		scanf("%d %d",&n,&Q);
		fo(i,1,n) scanf("%d %d",&e[i],&s[i]);
		fo(i,1,n)
			fo(j,1,n) scanf("%lld",&d[i][j]);
		
		fo(i,1,n)
			fo(j,1,n) f[i][j]=inf;
		
		fo(k,1,n)
			fo(i,1,n) if (i!=k && d[i][k]>-1)
				fo(j,1,n) if (j!=i && j!=k && d[k][j]>-1)
					d[i][j]=(d[i][j]==-1 || d[i][j]>d[i][k]+d[k][j]) ?d[i][k]+d[k][j] :d[i][j] ;
		fo(i,1,n)
			fo(j,1,n) if (i!=j && d[i][j]>-1 && d[i][j]<=e[i])
				f[i][j]=min(f[i][j],(double)d[i][j]/s[i]);
		fo(k,1,n)
			fo(i,1,n) if (i!=k && f[i][k]<inf)
				fo(j,1,n) if (j!=i && j!=k && f[k][j]<inf) f[i][j]=min(f[i][j],f[i][k]+f[k][j]);
		
		while (Q--)
		{
			int u,v;
			scanf("%d %d",&u,&v);
			printf("%.8f ",f[u][v]);
		}
		printf("\n");
	}
}