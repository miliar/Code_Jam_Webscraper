#include <bits/stdc++.h>
#define mp make_pair
#define ft first
#define sd second
#define ue printf("what?\n");
#define pb push_back
#define pf push_front
#define oo 0x3F3F3F3F
#define OO 0x3F3F3F3F3F3F3F3F
#define EPS 0
#define inf 1000000000000000LL
#define N 10005
#define pi acos(-1)
#define mod 1000000007

typedef long long ll;

using namespace std;

int dp[105][105][105][105], vis[105][105][105][105];

int b, d, cure;

int f(int h, int a, int hk, int ak)
{
	if(dp[h][a][hk][ak] != -1)
		return dp[h][a][hk][ak];
	if(vis[h][a][hk][ak])
		return oo;
	vis[h][a][hk][ak] = 1;
	int ans = oo;
	if(a >= hk)
		ans = 1;
	else
	{
		if(h > ak)
			ans = min(ans,1+f(h-ak,a,hk-a,ak));
		if(h > ak)
			ans = min(ans,1+f(h-ak,min(a+b,100),hk,ak));
		if(h > max(ak-d,0))
			ans = min(ans,1+f(h-(max(ak-d,0)),a,hk,max(ak-d,0)));
		if(cure > ak)
			ans = min(ans,1+f(cure-ak,a,hk,ak));
	}
	return dp[h][a][hk][ak] = ans;
}
		
main()
{
	int test, h, a, hk, ak, ans;
	scanf("%d", &test);
	int caso = 1;
	while(test--)
	{
		scanf("%d%d%d%d%d%d", &h, &a, &hk, &ak, &b, &d);
		cure = h;
		memset(dp,-1,sizeof dp);
		memset(vis,0,sizeof vis);
		ans = f(h,a,hk,ak);
		if(ans < oo)
			printf("Case #%d: %d\n", caso++, ans);
		else
			printf("Case #%d: IMPOSSIBLE\n", caso++);
	}
}
			
	
		
		
		
			
	
