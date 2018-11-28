#include <set>
#include <map>
#include <queue>
#include <vector>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;
int group[110];

int safe(int i, int j, vector<vector<int> > & dp)
{
	if (i >= 0 && j >= 0) return dp[i][j];
	else return -1;
}

void solve(int casen)
{
	int n, p, ans = 0;
	int cnt[4] = { 0,0,0,0 };
	cin >> n >> p;
	for (int i = 0; i < n; i++) cin >> group[i];
	for (int i = 0; i < n; i++) cnt[group[i] % p]++;
	ans += cnt[0];
	//printf("n %d p %d\n", n, p);
	//printf("%d %d %d %d\n", cnt[0], cnt[1], cnt[2], cnt[3]);
	if (p == 2)
	{
		if(cnt[1] > 0)ans += (cnt[1]-1) / 2 + 1;
		printf("Case #%d: %d\n", casen, ans);
	}
	else if (p == 3)
	{
		vector<vector<int> > dp; vector<int> temp;
		for (int i = 0; i < cnt[2] + 10; i++) {
			temp.push_back(0);
		}
		for (int i = 0; i < cnt[1] + 10; i++) {
			dp.push_back(temp);
		}
		for (int i = 0; i <= cnt[1]; i++)for (int j = 0; j <= cnt[2]; j++)dp[i][j] = 1;
		dp[0][0] = 0;
		for (int i = 0; i <= cnt[1]; i++)
		{
			for (int j = 0; j <= cnt[2]; j++)
			{
				dp[i][j] = max(safe(i,j,dp),max(safe(i-1,j,dp),safe(i,j-1,dp)));
				dp[i][j] = max(safe(i-1,j-1,dp) + 1, dp[i][j]);
			}
		}
		for (int i = 0; i <= cnt[1]; i++)
		{
			for (int j = 0; j <= cnt[2]; j++)
			{
				dp[i][j] = max(safe(i, j, dp), max(safe(i - 1, j, dp), safe(i, j - 1, dp)));
				dp[i][j] = max(safe(i - 3, j, dp) + 1, dp[i][j]);
			}
		}
		for (int i = 0; i <= cnt[1]; i++)
		{
			for (int j = 0; j <= cnt[2]; j++)
			{
				dp[i][j] = max(safe(i, j, dp), max(safe(i - 1, j, dp), safe(i, j - 1, dp)));
				dp[i][j] = max(safe(i, j - 3, dp) + 1, dp[i][j]);
			}
		}
		//if(((cnt[1]*1+cnt[2]*2)%p)!=0)ans++;

		printf("Case #%d: %d\n", casen, ans + dp[cnt[1]][cnt[2]]);
	}
	else
	{
		
	}
}

int main()
{
	freopen("A-small-attempt5.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; cin >> t;
	for (int i = 1; i <= t; i++)solve(i);

}