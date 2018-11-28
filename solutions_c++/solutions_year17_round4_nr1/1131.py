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


int dp[3][105][105][105][4];
bool got[3][105][105][105][4];

//				1		2		3
int f(int p, int a, int b, int c, int left)
{
	if (a+b+c==0)
		return 0;
	if (got[p-2][a][b][c][left])
		return dp[p-2][a][b][c][left];
	got[p-2][a][b][c][left]=true;
	int ans=0;
	if (a>0)
		ans=max(ans,f(p,a-1,b,c,(left-1+p)%p));
	if (b>0)
		ans=max(ans,f(p,a,b-1,c,(left-2+p)%p));
	if (c>0)
		ans=max(ans,f(p,a,b,c-1,(left-3+p)%p));
	if (left==0)
		ans++;
	return dp[p-2][a][b][c][left]=ans;
}

int main()
{
	int tc;
	scanf("%d",&tc);
	for (int asdf=1; asdf<=tc; asdf++)
	{
		int n,p;
		scanf("%d %d",&n,&p);
		int cnt[4]={0,0,0,0};
		while (n--)
		{
			int g;
			scanf("%d",&g);
			cnt[g%p]++;
		}
		printf("Case #%d: %d\n",asdf,f(p,cnt[1],cnt[2],cnt[3],0)+cnt[0]);
	}
	return 0;
}
