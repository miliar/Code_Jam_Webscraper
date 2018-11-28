#include <cstdio>
#include <algorithm>
#include <vector>

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


#define MAX_D 20

int d[MAX_D];
ll dp[MAX_D][10][2];

ll f(int i, int p, bool less)
{
	if (i==-1)
		return 1;
	if (dp[i][p][less]!=-1)
		return dp[i][p][less];
	ll ans=0;
	int to=less?9:d[i];
	for (int here=p; here<=to; here++)
		ans+=f(i-1,here,less||(here<d[i]));
	return dp[i][p][less]=ans;
}

ll cnt(ll up)
{
	if (up==0)
		return 0;
	int n=0;
	for (; up; up/=10)
		d[n++]=up%10;
	for (int i=0; i<n; i++)
		for (int j=0; j<10; j++)
			dp[i][j][0]=dp[i][j][1]=-1;
	return f(n-1,0,0)-1;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		ll n;
		scanf("%lld",&n);
		ll lo=1,hi=n;
		if (n>1)
		{
			ll cake=cnt(n);
			while (lo<hi)
			{
				ll m=(lo+hi+1)/2;
				if (cnt(m)<cake)
					lo=m;
				else
					hi=m-1;
			}
		}
		else
			lo=0;
		printf("Case #%d: %lld\n",asdf,lo+1);
	}
	return 0;
}
