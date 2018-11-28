#include <bits/stdc++.h>
#define si(n) scanf("%d",&n);
#define pi(n) printf("%d\n",n);
#define pl(n) printf("%lld\n",n);
#define sl(n) scanf("%lld",&n);
#define sd(n) scanf("%lf",&n);
#define pd(n) printf("%lf\n",n);
#define ss(s) scanf("%s",s);
#define ps(s) printf("%s\n",s);
#define pb push_back
#define ll long long int
#define maxn 101
#define sqrtn 317
#define maxm 51
#define minv(a,b,c) min(a,min(b,c))
#define pii pair<int,int>
#define pll pair<ll,ll>
#define pli pair<ll,int>
#define eps 1e-9
#define mod 1000000007
#define psi pair < string,ll>
#define mp make_pair
#define BLOCK 450
using namespace std;

double dist[maxn][maxn];
double horses[maxn][2];
double dp[maxn];
double dists[maxn];
double fdist[maxn][maxn];
double timearr[maxn][maxn];


int main()
{
	int t;
	si(t);
	for(int i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		int n,q;
		si(n);si(q);
		int a,b;
		for(int i=1;i<=n;i++)
		{
			sd(horses[i][0]);
			sd(horses[i][1]);
		}
		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				sd(dist[i][j]);
			}
		}

		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				if(dist[i][j]==-1)
				{
					fdist[i][j]=1e15;
				}
				else
				{
					fdist[i][j]=dist[i][j];
				}
			}
		}

		for(int k=1;k<=n;k++)
		{
			for(int i=1;i<=n;i++)
			{
				for(int j=1;j<=n;j++)
				{
					if(fdist[i][j]>fdist[i][k]+fdist[k][j])
					{
						fdist[i][j]=fdist[i][k]+fdist[k][j];
					}
					
				}
			}
		}

		for(int i=1;i<=n;i++)
		{
			for(int j=1;j<=n;j++)
			{
				if(fdist[i][j]<=horses[i][0])
				{
					timearr[i][j]=fdist[i][j]/horses[i][1];
				}
				else
				{
					timearr[i][j]=1e15;
				}
			}
		}

		for(int k=1;k<=n;k++)
		{
			for(int i=1;i<=n;i++)
			{
				for(int j=1;j<=n;j++)
				{
					if(timearr[i][j]>timearr[i][k]+timearr[k][j])
					{
						timearr[i][j]=timearr[i][k]+timearr[k][j];
					}
					
				}
			}
		}

		for(int i=1;i<=q;i++)
		{
			si(a);si(b);
			printf("%lf ",timearr[a][b]);
		}
		ps("");

		
		


	}
}