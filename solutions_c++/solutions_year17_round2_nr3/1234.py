#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

#define pll pair<ll, ll>
#define F first
#define S second
#define mp make_pair
#define pb push_back

double dp[101][1001];
double endurance[101], speed[101], dis[101];
int  N, Q;

double calc(double prev_end, int prev_s, int i) {
	if(i == N - 1)
	{
		if(prev_end < dis[i])
			dp[i][prev_s] = (dis[i]/speed[i]) ;
		else 
			dp[i][prev_s] = min(dis[i]/speed[i], dis[i]/prev_s);
	}
	else if(dp[i][prev_s] == -1)
	{
		if(prev_end < dis[i])
			dp[i][prev_s] = (dis[i]/speed[i]) + calc(endurance[i] - dis[i], speed[i], i + 1);
		else 
			dp[i][prev_s] = min(dis[i]/speed[i] + calc(endurance[i] - dis[i], speed[i], i + 1), dis[i]/prev_s + calc(prev_end - dis[i], prev_s, i + 1));
	}
	return dp[i][prev_s];
}

int main(){
	int T;
	cin >> T;
	for(int t = 1; t <= T; t++) {
		for(int i = 0; i < 101; i++)
		{
			for(int j = 0; j < 1001; j++)
				dp[i][j] = -1;
		}		
		cin >> N >> Q;
		for(int i = 1; i <= N; i++)
		{
			cin >> endurance[i] >> speed[i];
		}
		double d;
		for(int i = 1; i <= N; i++)
		{
			for(int j = 1; j <= N; j++)
			{
				cin >> d;
				if(d != -1)
					dis[i] = d;
			}
		}
		int start, end;
		cin >> start >> end;
		double ans = 1e14;
		calc(0, 0, 1);
		for(int i = 0; i < 1001; i++)
		{
			if(dp[1][i] != -1)
				ans = min(ans, dp[1][i]);
		}
		printf("Case #%d: %.8lf\n", t, ans);
	}
	return 0;
}