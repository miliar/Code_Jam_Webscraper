#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
int T;
int MAX = 2000000000;
int dp[105][105][105];
int main()
{ 
	freopen("infile.txt", "r", stdin);
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		for(int a=0; a<105; a++)
		{
			for(int b=0; b<105; b++)
			{
				for(int c=0; c<105; c++)
				{
					dp[a][b][c] = -MAX;
				}
			}
		}
		int N, P;
		int group[200];
		int groupmod[5] = {0, 0, 0, 0, 0};
		scanf("%d %d", &N, &P);
		for(int n=0; n<N; n++)
		{
			scanf(" %d ", &group[n]);
			groupmod[group[n]%P]++;
		}
		int ans = 0;
		if(P==2)
		{
			ans += groupmod[1]/2;
			if(groupmod[1]%2==1) ans++;
		}
		else if(P==3)
		{
			dp[0][groupmod[2]][groupmod[1]] = 0;
			for(int a=groupmod[2]; a>=0; a--)
			{
				for(int b=groupmod[1]; b>=0; b--)
				{
					dp[0][a][b] = max(max(dp[0][a][b], dp[0][a+1][b+1]+1), max(dp[0][a+3][b]+1, dp[0][a][b+3]+1));
					if(a!=0 || b!=0) ans = max(ans, dp[0][a][b]+1);
					else ans = max(ans, dp[0][a][b]);
				}
			}
		}
		else
		{
			dp[groupmod[3]][groupmod[2]][groupmod[1]] = 0;
			for(int a=groupmod[3]; a>=0; a--)
			{
				for(int b=groupmod[2]; b>=0; b--)
				{
					for(int c=groupmod[1]; c>=0; c--)
					{
						dp[a][b][c] = max(dp[a][b][c], dp[a+4][b][c]+1);
						dp[a][b][c] = max(dp[a][b][c], dp[a][b+2][c]+1);
						dp[a][b][c] = max(dp[a][b][c], dp[a][b][c+4]+1);
						dp[a][b][c] = max(dp[a][b][c], dp[a+1][b][c+1]+1);
						dp[a][b][c] = max(dp[a][b][c], dp[a][b+1][c+2]+1);
						dp[a][b][c] = max(dp[a][b][c], dp[a+2][b+1][c]+1);
						if(a!=0 || b!=0 || c!=0) ans = max(ans, dp[a][b][c]+1);
						else ans = max(ans, dp[a][b][c]);
					}
				}
			}
		}
		printf("Case #%d: %d\n", t, ans+groupmod[0]);
	}
}