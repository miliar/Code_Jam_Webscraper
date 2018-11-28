#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <tuple>

using namespace std;

int testCount;
int ans;
int n;
int c;
int m;
int ticketCounts[1010][1010];
int main()
{
	freopen("B-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{

		cin >> n >> c >> m;
		for (int i = 0; i < c; i++)
			for (int j = 0; j < n; j++)
				ticketCounts[i][j] = 0;
		for (int i = 0; i < m; i++)
		{
			int t1, t2;
			cin >> t1 >> t2;
			ticketCounts[t2 - 1][t1 - 1]++;
		}

		// Small

		int minRides = ticketCounts[0][0] + ticketCounts[1][0];
		int total0 = 0;
		int total1 = 0;
		for (int i = 0; i < n; i++)
		{
			total0 += ticketCounts[0][i];
			total1 += ticketCounts[1][i];
		}
		minRides = max(minRides, total0);
		minRides = max(minRides, total1);
		int bumps = 0;
		int freeBumps = max(0, ticketCounts[0][0] + ticketCounts[1][0] - max(total0, total1));
		for (int i = 1; i < n; i++)
		{
			if (ticketCounts[0][i] > 0 && ticketCounts[1][i] > 0)
			{
				if (total0 - ticketCounts[0][i] < ticketCounts[1][i]
					&& total1 - ticketCounts[1][i] < ticketCounts[0][i])
				{
					bumps += min(ticketCounts[1][i] - total0 + ticketCounts[0][i],
						ticketCounts[1][i] - total1 + ticketCounts[0][i]);
				}
			}
		}
		bumps -= freeBumps;
		
		printf("Case #%d: %d %d\n", testNumber, minRides, max(0, bumps));
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
