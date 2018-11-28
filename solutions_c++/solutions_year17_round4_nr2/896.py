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

int t,n,m,c,a,b;
int tic[5][1005];
VI pos[5];
int sum[5];
int main()
{
	scanf("%d",&t);
	int tt = 1;
	while(t--)
	{
		scanf("%d %d %d",&n,&c,&m);

		sum[2] = 0;
		sum[1] = 0;
		pos[2].clear();
		pos[1].clear();
		for(int i=0;i<=n;i++)
		{
			tic[2][i] = 0;
			tic[1][i] = 0;
		}


		for(int i=0;i<m;i++)
		{
			scanf("%d %d",&a,&b);
			pos[b].push_back(a);
			sum[b] += 1;
			tic[b][a]++;
		}
		sort(pos[2].begin(),pos[2].end());
		sort(pos[1].begin(),pos[1].end());

		int ans = tic[2][1] + tic[1][1] + max(max(0,sum[2]-tic[2][1]-tic[1][1]),max(0,sum[1]-tic[2][1]-tic[1][1]));
		int ans2 = 0;
		for(int i=2; i<=n;i++)
		{
			for(int j=2; j<=n ;j++)
			{
				if(tic[1][i] == 0)
					break;
				if(i != j)
				{
					int m = min(tic[1][i],tic[2][j]);
					tic[1][i] -= m;
					tic[2][j] -= m;
				}
			}
		}
		for(int i=2; i<=n;i++)
		{
			if(tic[1][i] != 0 && tic[2][i] != 0)
			{
				ans2 = min(max(tic[1][i]-tic[2][1],0),max(tic[2][i]-tic[1][1],0));
			}
		}

		// ans2 = max(0,ans2- max(tic[1][1],tic[2][1]));
		printf("Case #%d: %d %d\n",tt,ans,ans2 );
		tt++;
	}
	return 0;
}