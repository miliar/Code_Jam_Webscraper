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

using namespace std;

int testCount;

int n;

int p;

vector<int> indexes;

vector<int> recipe;

vector<vector<int>> packages;

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		int ans = 0;
		recipe.clear();
		packages.clear();
		indexes.clear();
		cin >> n >> p;
		int t;
		for (int i = 0; i < n; i++)
		{
			cin >> t;
			recipe.push_back(t);
		}
		for (int i = 0; i < n; i++)
		{
			indexes.push_back(0);
			vector<int> temp;
			for (int j = 0; j < p; j++)
			{
				cin >> t;
				temp.push_back(t);
			}
			sort(temp.begin(), temp.end());
			packages.push_back(temp);
		}

		for (int i = 0; i < p; i++)
		{
			// we try package packages[0][i]
			int leftRange = ceil(packages[0][i] * 1.0 / recipe[0] / 1.1);
			int rightRange = floor(packages[0][i] * 1.0 / recipe[0] / 0.9);
			if (rightRange < leftRange)
				continue;
			bool good = 1;

			for (int j = 1; j < n; j++)
			{
				bool found = 0;
				// look for a package that fits, also fix the range
				while (indexes[j] < p && !found)
				{
					// if less -- add indexes, if more -- continue (had to change other indexes)
					int newLeftRange = ceil(packages[j][indexes[j]] * 1.0 / recipe[j] / 1.1);
					int newRightRange = floor(packages[j][indexes[j]] * 1.0 / recipe[j] / 0.9);
					if (newLeftRange > rightRange)
					{
						good = 0;
						break;
					}
					if (newRightRange < leftRange)
					{
						indexes[j]++;
						continue;
					}
					found = 1;
					leftRange = max(leftRange, newLeftRange);
					rightRange = min(rightRange, newRightRange);
				}
				if (!found)
				{
					good = 0;
					break;
				}
			}
			if (good)
			{
				for (int i = 1; i < n; i++)
					indexes[i]++;
			}

			ans += good;
		}

		printf("Case #%d: %d\n", testNumber, ans);
	}



	fclose(stdin);
	fclose(stdout);
	return 0;
}
