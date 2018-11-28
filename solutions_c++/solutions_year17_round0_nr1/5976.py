#include <cstdio>
#include <vector>
#include <algorithm>
#include <queue>
#include <iostream>
#include <functional>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int numCases;
	cin >> numCases;

	for (int testCase = 1; testCase < numCases + 1; testCase++)
	{
		string tableString = "";
		int table[1005];
		int k;
		cin >> tableString;
		cin >> k;
		int tableSize = tableString.size();
		for (int i = 0; i < tableSize; i++)
			table[i] = tableString[i] == '+' ? 1 : 0;

		int numFlips = 0;
		int tp = 0;
		while (tp < tableSize)
		{
			if (table[tp] == 1) { tp++; continue; }
			else
			{
				if (tp + k > tableSize) { numFlips = -1; break; }
				else
				{
					numFlips += 1;
					for (int i = tp; i < tp + k; i++)
						table[i] = (table[i] + 1) % 2;
				}
			}
			tp++;
		}
		cout << "Case #" << testCase << ": ";
		if (numFlips == -1) cout << "IMPOSSIBLE\n";
		else cout << numFlips << "\n";
	}
}

