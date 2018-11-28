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


#define MAX_T 1500
#define INF 123456789

int ac,aj,mark[MAX_T];
int dp[MAX_T][730][3][3];

int f(int i, int t, int g, int shit)
{
	if (t>720)
		return INF;
	if (i==24*60)
	{
		if (t==720)
			return shit!=g?1:0;
		return INF;
	}
	if (dp[i][t][g][shit]!=-1)
		return dp[i][t][g][shit];
	int ans=INF;
	//keep
	if (g==1)
	{
		if (mark[i]!=1)
			ans=f(i+1,t+1,1,shit);
	}
	else
	{
		if (mark[i]!=2)
			ans=f(i+1,t,2,shit);
	}
	//change
	if (g==1)
	{
		if (mark[i]!=2)
			ans=min(ans,1+f(i+1,t,2,shit));
	}
	else
	{
		if (mark[i]!=1)
			ans=min(ans,1+f(i+1,t+1,1,shit));
	}
	return dp[i][t][g][shit]=ans;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		for (int i=0; i<1500; i++)
			mark[i]=0;
		scanf("%d %d",&ac,&aj);
		for (int i=1; i<=ac; i++)
		{
			int l,r;
			scanf("%d %d",&l,&r);
			for (int j=l; j<r; j++)
				mark[j]=1;
		}
		for (int i=1; i<=aj; i++)
		{
			int l,r;
			scanf("%d %d",&l,&r);
			for (int j=l; j<r; j++)
				mark[j]=2;
		}
		for (int i=0; i<1500; i++)
			for (int j=0; j<730; j++)
				for (int g=0; g<3; g++)
					for (int shit=0; shit<3; shit++)
						dp[i][j][g][shit]=-1;
		int ans=INF;
		if (mark[0]==1)
			ans=f(1,0,2,2);
		else if (mark[0]==2)
			ans=f(1,1,1,1);
		else
			ans=min(f(1,1,1,1),f(1,0,2,2));
		printf("Case #%d: %d\n",asdf,ans);
	}
	return 0;
}
