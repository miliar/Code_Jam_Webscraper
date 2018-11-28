#include<bits/stdc++.h>
using namespace std;
# define ll double
# define mod 1000000007
# define MAX 111
# define anotherMax 11
# define INF 1e16
ll grid[MAX][MAX];
double timeTaken[MAX];
pair <ll, ll> horseData[MAX];
int main()
{
	ifstream in("file/a.txt");
	ofstream out("file/b.txt");
	in.sync_with_stdio(false);
	int t, var = 0;
	in >> t;
	while(t--)
	{
		var++;
		out << "Case #" << var << ": ";
		int n, q;
		in >> n >> q;
		for (auto i = 1; i <= n; i++)
			in >> horseData[i].first >> horseData[i].second;
		for (auto i = 1; i <= n; i++)
			for (auto j = 1; j <= n; j++)
				in >> grid[i][j];
		in >> q >> q;
		for (auto i = 1; i <= n; i++)
			timeTaken[i] = -1.0;
		timeTaken[n] = 0.0;
		timeTaken[n - 1] = horseData[n - 1].first >= grid[n - 1][n] ? grid[n - 1][n] / horseData[n - 1].second : -1.00;
		for(auto i=n-2;i>=1;i--)
		{
			auto totalDistance = 0.0;
			timeTaken[i] = 1e11;
			auto cond = true;
			for(auto j=i+1;j<=n;j++)
			{
				totalDistance += grid[j - 1][j];
				
				if (totalDistance > horseData[i].first)
					break;
				if(timeTaken[j]==-1)
					continue;
				cond = false;
				timeTaken[i] = min(timeTaken[i], timeTaken[j] + static_cast<double>(totalDistance / horseData[i].second));
			}
			if (cond)
				timeTaken[i] = -1;
		}
		out << fixed << setprecision(10) << timeTaken[1] << '\n';
	}
	return 0;
}