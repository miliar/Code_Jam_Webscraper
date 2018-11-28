#include <bits/stdc++.h>
using namespace std;
#define x first
#define y second
#define mp make_pair
#define REP(i,j,k)  for(int i=(j);i<=(k);++i)
#define REPD(i,j,k) for(int i=(j);i>=(k);--i)

const int maxn = 110;

long long a[maxn][maxn];
int n,m;
long long E[maxn],S[maxn];
double dis[maxn][maxn];

void init()
{
	scanf("%d%d",&n,&m);
	REP(i,1,n)
		cin>>E[i]>>S[i];
	REP(i,1,n)
	{
		REP(j,1,n)
		{
			cin>>a[i][j];
			if(a[i][j]==-1) a[i][j]=0x3fffffffffffffffLL;
		}
		a[i][i]=0;
	}
	REP(k,1,n)
		REP(i,1,n)
			REP(j,1,n)
				a[i][j]=min(a[i][j],a[i][k]+a[k][j]);
	REP(i,1,n)
		REP(j,1,n)
			if(a[i][j]<=E[i]) dis[i][j]=1.0*a[i][j]/S[i];
			else dis[i][j]=1e50;

	REP(k,1,n)
		REP(i,1,n)
			REP(j,1,n)
				dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j]);
}

void solve()
{
	while(m--)
	{
		int x,y;
		scanf("%d%d",&x,&y);
		printf(" %.10lf",dis[x][y]);
	}
	puts("");
}

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T;
	scanf("%d",&T);
	REP(i,1,T)
	{
		printf("Case #%d:",i);
		init();
		solve();
	}
	return 0;
}
