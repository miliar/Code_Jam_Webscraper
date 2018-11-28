#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		int k;
		string p;
		cin >> p >> k;
		vector<bool> pc(p.size());
		for (int i = 0; i < p.size(); i++)
			pc[i] = (p[i] == '+');
		int flips = 0;
		for (int i = 0; i + k - 1 < pc.size(); i++)
		{
			if (!pc[i])
			{
				flips++;
				for (int j = i; j < i + k; j++)
					pc[j] = !pc[j];
			}
		}
		if (count(pc.begin(), pc.end(), false))
			printf("Case #%d: IMPOSSIBLE\n", c);
		else
			printf("Case #%d: %d\n", c, flips);
	}
}
