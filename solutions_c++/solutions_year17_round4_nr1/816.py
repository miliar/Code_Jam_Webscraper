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
vector<int> groups;
int n;
int p;
int counts[4];
int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		cin >> n >> p;
		groups.clear();
		int t;
		for (int j = 0; j < p; j++)
			counts[j] = 0;
		for (int i = 0; i < n; ++i)
		{
			cin >> t;
			counts[t % p]++;
		}

		if (p == 2)
		{
			ans = n - counts[1] / 2;
		}
		else if (p == 3)
		{
			int temp1 = 2 * min(counts[1], counts[2]);
			int temp2 = max(counts[1], counts[2]) - min(counts[1], counts[2]);
			ans = n - temp1 / 2 - 2 * (temp2 / 3) - max(0, temp2 % 3 - 1);
		}
		else
		{
			ans = n;
			int temp1 = counts[2] + 2 * min(counts[1], counts[3]);
			ans -= temp1 / 2;
			int temp2 = max(counts[1], counts[3]) - min(counts[1], counts[3]);
			if (counts[2] % 2)
			{
				if (temp2 > 2)
					ans -= 2 + 3 * ((temp2 - 2) / 4) + max((temp2 - 2) % 4 - 1, 0);
				else
					ans -= temp2;
			}
			else
			{
				ans -= 3 * (temp2 / 4) + max(temp2 % 4 - 1, 0);
			}
		}
		printf("Case #%d: %lld\n", testNumber, ans);
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}
