#include <bits/stdc++.h>

using namespace std;

int n;

bool check(int x)
{
	int pre=10;
	while (x)
	{
		if ((x%10)>pre) return false;
		else
		{
			pre=x%10;
			x/=10;
		}
	}
	return true;
}

int solve()
{
	int ans=1;
	for (int i=1;i<=n;++i)
	{
		if (check(i))
		{
			ans=i;
		}
	}
	return ans;
}

int main(void)
{
	#ifdef ex
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	#endif
	
	int T;
	scanf("%d",&T);
	
	for (int iCase=1;iCase<=T;++iCase)
	{
		scanf("%d",&n);
		int ans=solve();
		printf("Case #%d: %d\n",iCase,ans);
	}
}
