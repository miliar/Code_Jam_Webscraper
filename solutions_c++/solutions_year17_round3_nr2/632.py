#include <bits/stdc++.h>

using namespace std;

const int maxx = 1500, inf = 20000;

int n, t, dp[maxx][maxx][2][2], tim[maxx], m;

int main()
{
	ifstream in;	in.open("tt.txt");	ofstream out;	out.open("ans.out");
	in >> t;
	for(int q = 1; q <= t; q++)
	{
		out << "Case #" << q << ": ";	
		in >> n >> m;
		fill(tim, tim + maxx, 0);
		for(int i = 0; i < maxx; i++) 
			for(int j = 0; j < maxx; j++) 	
				dp[i][j][0][0] = dp[i][j][0][1] = dp[i][j][1][0] = dp[i][j][1][1] = inf;
		for(int i = 0; i < n; i++)
		{
			int x, y;
			in >> x >> y;
			for(int j = x; j < y; j++) tim[j] = 1;
		}
		for(int i = 0; i < m; i++)
		{
			int x, y;
			in >> x >> y;
			for(int j = x; j < y; j++) tim[j] = 2;
			}	
//	tim[1440] = tim[0];
		dp[0][0][0][0] = dp[0][0][1][1] = 0;
		for(int i = 1; i <= 1440; i++)
		{
			int x = tim[i - 1];
			for(int j = 0; j <= min(i, 720); j++)
			{
//				if (i == 1440)
//				cout << i << " " << j << endl;
				dp[i][j][0][0] = dp[i][j][1][0] = dp[i][j][0][1] = dp[i][j][1][1] = inf;
				if (x != 1 && j > 0)
					dp[i][j][0][0] = min(dp[i - 1][j - 1][0][0], dp[i - 1][j - 1][0][1] + 1),
					dp[i][j][1][0] = min(dp[i - 1][j - 1][1][0], dp[i - 1][j - 1][1][1] + 1);
			
				if (x != 2 && j < i)
					dp[i][j][0][1] = min(dp[i - 1][j][0][1], dp[i - 1][j][0][0] + 1),
					dp[i][j][1][1] = min(dp[i - 1][j][1][1], dp[i - 1][j][1][0] + 1);
					
//				if (dp[i][j][0] != inf) cout << i << " " << j << " " << dp[i][j][0] << endl;
			}
		}
//	cou	t << dp[1][0][1] << " " << dp[2][1][0] << " " << dp[1438][719][1] << " " << dp[1439][719][1] << endl;
		int x1 = dp[1440][720][0][0];
		int	x2 = dp[1440][720][0][1] + 1;
		int x3 = dp[1440][720][1][0] + 1;
		int x4 = dp[1440][720][1][1];
		out << min(min(x1, x2), min(x3, x4)) << endl;
	}
//	cout << min(dp[1441][721][0], dp[1441][720][1]) << endl;
	return 0;
}
