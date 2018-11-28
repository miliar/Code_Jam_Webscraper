#include <cstdio>
#include <algorithm>
#include <vector>
#include <cmath>

using namespace std;

#define all(a) (a).begin(),(a).end()
#define pb push_back
#define sz(a) ((int)(a).size())
#define mp make_pair
#define fi first
#define se second

typedef pair<int,int> pint;
typedef long long ll;
typedef vector<int> vi;


#define MAX_N 1005


typedef long double real;

int n,k;
pint rh[MAX_N];
ll dp[MAX_N][MAX_N];

ll f(int i, int g)
{
	if (g==k||i==n+1)
		return 0;
	if (dp[i][g]!=-1)
		return dp[i][g];
	return dp[i][g]=max(f(i+1,g),f(i+1,g+1)+rh[i].fi*1LL*rh[i].se);	
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		fprintf(stderr,"solving %d\n",asdf);
		scanf("%d %d",&n,&k);
		for (int i=1; i<=n; i++)
		{
			scanf("%d %d",&rh[i].fi,&rh[i].se);
			for (int j=1; j<=k; j++)
				dp[i][j]=-1;
		}
		sort(rh+1,rh+1+n);
		reverse(rh+1,rh+1+n);
		ll cake=0;
		for (int bottom=1; bottom<=n; bottom++)
		{
			ll here=rh[bottom].fi;
			here*=here;
			here+=(f(bottom+1,1)+rh[bottom].fi*1LL*rh[bottom].se)*2;
			cake=max(cake,here);
		}
		printf("Case #%d: %.10Lf\n",asdf,cake*3.1415926535897932L);
	}
	return 0;
}
