#include<bits/stdc++.h>
using namespace std;
#define FOR(i,s,e) for(int i = (s); i < (e); i++)
#define FOE(i,s,e) for(int i = (s); i <= (e); i++)
#define FOD(i,s,e) for(int i = (s); i >= (e); i--)
#define ll long long
#define pb push_back

int n, m, x, y, z, k, w, l;
int A[105];
int tc, ans, tt;
int dp[105][105][105][4];
int a, b, c;

int main ()
{
	scanf("%d", &tc);
	while (tc--)
	{
		scanf("%d %d", &n, &m);
		FOR(i, 0, n) { scanf("%d", &A[i]); A[i] %= m; }
		
		a = b = c = 0;
		FOR(i, 0, n) if (A[i] == 1) a++; else if (A[i] == 2) b++; else if (A[i] == 3) c++;
		
		memset(dp, -1, sizeof(dp));
		dp[0][0][0][0] = 0;
		
	//	printf("%d %d %d\n", a, b, c);
		
		FOE(i, 1, a + b + c)
		{
			FOE(j, 0, a) FOE(k, 0, b)
			{
				l = i - (j + k);
				if (l > c || l < 0) continue;
								
				FOR(remain, 0, m)
				{
					if (j > 0 && dp[j - 1][k][l][remain] != -1)
					{
						x = (remain + m - 1) % m;
						if (remain == 0) y = 0;
						else y = 1;
						if (dp[j][k][l][x] == -1) dp[j][k][l][x] = dp[j - 1][k][l][remain] + y;
						else dp[j][k][l][x] = min(dp[j][k][l][x], dp[j - 1][k][l][remain] + y);
					}
					if (k > 0 && dp[j][k - 1][l][remain] != -1)
					{
						x = (remain + m - 2) % m;
						if (remain == 0) y = 0;
						else y = 1;
						if (dp[j][k][l][x] == -1) dp[j][k][l][x] = dp[j][k - 1][l][remain] + y;
						else dp[j][k][l][x] = min(dp[j][k][l][x], dp[j][k - 1][l][remain] + y);
					}
					if (l > 0 && dp[j][k][l - 1][x] != -1)
					{
						x = (remain + m - 3) % m;
						if (remain == 0) y = 0;
						else y = 1;
						if (dp[j][k][l][x] == -1) dp[j][k][l][x] = dp[j][k][l - 1][remain] + y;
						else dp[j][k][l][x] = min(dp[j][k][l][x], dp[j][k][l - 1][remain] + y);
					}
				}
				
			}
		}
		
		ans = -1;
		FOR(i, 0, m) if (dp[a][b][c][i] != -1)
		{
			if (ans == -1) ans = dp[a][b][c][i];
			else ans = min(ans, dp[a][b][c][i]);
		}
		
		printf("Case #%d: %d\n", ++tt, n  -ans);
	}
	
	return 0;
}
