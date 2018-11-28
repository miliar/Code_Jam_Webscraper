#include <bits/stdc++.h>
#define ff first
#define ss second
#define pb push_back
#define MOD (1000000007LL)
#define LEFT(n) (2*(n))
#define RIGHT(n) (2*(n)+1)
 
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> ii;
typedef pair<int, ii> iii;
 
ll pwr(ll base, ll p, ll mod = MOD){
ll ans = 1;while(p){if(p&1)ans=(ans*base)%mod;base=(base*base)%mod;p/=2;}return ans;
}
 
ll gcd(ll a, ll b){
    if(b == 0)  return a;
    return gcd(b, a%b);
}

typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector<int> VI;

int t,n,q;
double dist[105],speed[105];

double d[105][105];
double ti[105][105];
int u[105],v[105];


int main()
{
	scanf("%d",&t);
	int cnt = 1;
	while(t--)
	{
		scanf("%d %d",&n,&q);
		for(int i=1;i<=n;i++)
			scanf("%lf%lf",&dist[i],&speed[i]);
		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
				scanf("%lf",&d[i][j]);
		for(int i=0;i<q;i++)
			scanf("%d %d",&u[i],&v[i]);

		for(int i=1;i<=n;i++)
			d[i][i] = 0;	

		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
				{
					if(d[i][k] != -1 && d[k][j] != -1)
						if(d[i][j] == -1 || d[i][k] + d[k][j] < d[i][j])
							d[i][j] = d[i][k]+d[k][j];
				}

		// for(int i=1;i<=n;i++)
		// {
		// 	for(int j=1;j<=n;j++)
		// 	{
		// 		printf("%lf ",d[i][j]);
		// 	}
		// 	printf("\n");
		// }


		for(int i=1;i<=n;i++)
			for(int j=1;j<=n;j++)
			{
				if(d[i][i] >= 0 && d[i][j] <= dist[i])
					d[i][j] = (double)d[i][j]/speed[i];
				else
					d[i][j] = -1;
			}

		// for(int i=1;i<=n;i++)
		// {
		// 	for(int j=1;j<=n;j++)
		// 	{
		// 		printf("%lf ",d[i][j]);
		// 	}
		// 	printf("\n");
		// }

		for(int k=1;k<=n;k++)
			for(int i=1;i<=n;i++)
				for(int j=1;j<=n;j++)
				{
					if(d[i][k] >= 0 && d[k][j] >= 0)
						if(d[i][j] < 0|| d[i][k] + d[k][j] < d[i][j])
							d[i][j] = d[i][k]+d[k][j];
				}

		printf("Case #%d: ",cnt);
		cnt++;
		for(int i=0;i<q;i++)
			printf("%0.9lf ",d[u[i]][v[i]]);
		printf("\n");
		
	}
	return 0;
}