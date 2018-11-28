#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>

using namespace std;

int n, k;
int dLeft[1003], dRight[1003];
bool existOne[1003];

void updateLeft()
{
	int curCount = 1;
	for (int i = 0; i <= n; i++)
	{
		if (existOne[i])
		{
			dLeft[i] = 0;
			curCount = 0;
		}
		else
		{
			dLeft[i] = curCount;
			curCount++;
		}
	}
}

void updateRight()
{
	int curCount = 0;
	for (int i = n; i > 0; i--)
	{
		if (existOne[i])
		{
			dRight[i] = 0;
			curCount = 0;
		}
		else
		{
			dRight[i] = curCount;
			curCount++;
		}
	}
}

int main()
{
	freopen("C-small-1-attempt0.in", "r", stdin);
	freopen("C-small-1-attempt0.out", "w", stdout);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++)
	{
		memset(existOne, 0, sizeof(existOne));
		cin >> n >> k;
		existOne[0] = 1;
		existOne[n + 1] = 1;
		updateLeft();
		updateRight();
		int maxMin, maxMax;
		maxMin = maxMax = 0;
		int resLeft, resRight;
		int toEnter = 1;
		for (int j = 1; j <= k; j++)
		{
			maxMin = maxMax = 0;
			for (int z = 1; z <= n; z++)
			{
				if (min(dLeft[z], dRight[z]) > maxMin)
				{
					maxMin = min(dLeft[z], dRight[z]);
					maxMax = max(dLeft[z], dRight[z]);
					toEnter = z;
				}
				else if (min(dLeft[z], dRight[z]) == maxMin && max(dLeft[z], dRight[z]) > maxMax)
				{
					maxMax = max(dLeft[z], dRight[z]);
					toEnter = z;
				}
			}

			existOne[toEnter] = 1;
			resLeft = max(dLeft[toEnter], dRight[toEnter]);
			resRight = min(dLeft[toEnter], dRight[toEnter]);
			updateLeft();
			updateRight();
		}

		cout << "Case #" << i << ": " << resLeft << " " << resRight << endl;
	}
	return 0;
}
