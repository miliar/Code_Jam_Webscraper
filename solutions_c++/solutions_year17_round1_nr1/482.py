#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;

int testCount;

int r;
int c;

char cakeMap[30][30];

set<char> done;

void doFill(int x, int y)
{
	// Try to fill left, then up, then right, then down
	int upCur = x;
	int downCur = x;
	int leftCur = y;
	int rightCur = y;

	// left
	while (leftCur > 0 && cakeMap[x][leftCur - 1] == '?')
		leftCur--;
	// up
	bool good = 1;
	while (upCur > 0 && good)
	{
		for (int i = leftCur; i <= rightCur; i++)
		{
			if (cakeMap[upCur - 1][i] != '?')
				good = 0;
		}
		if (good)
			upCur--;
	}
	// right
	good = 1;
	while (rightCur < c - 1 && good)
	{
		for (int i = upCur; i <= downCur; i++)
		{
			if (cakeMap[i][rightCur + 1] != '?')
				good = 0;
		}
		if (good)
			rightCur++;
	}
	// down
	good = 1;
	while (downCur < r - 1 && good)
	{
		for (int i = leftCur; i <= rightCur; i++)
		{
			if (cakeMap[downCur + 1][i] != '?')
				good = 0;
		}
		if (good)
			downCur++;
	}

	for (int i = upCur; i <= downCur; i++)
		for (int j = leftCur; j <= rightCur; j++)
			cakeMap[i][j] = cakeMap[x][y];
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);	
	cin >> testCount;
	for (int testNumber = 1; testNumber <= testCount; testNumber++)
	{
		done.clear();
		cin >> r >> c;
		string s;
		for (int i = 0; i < r; i++)
		{
			cin >> s;
			for (int j = 0; j < c; j++)
			{
				cakeMap[i][j] = s[j];
			}
		}

		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (cakeMap[i][j] != '?' && done.find(cakeMap[i][j]) == done.end())
				{
					done.insert(cakeMap[i][j]);
					doFill(i,j);
				}
			}
		}
		printf("Case #%d:\n", testNumber);
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
				printf("%c", cakeMap[i][j]);
			printf("\n");
		}
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
