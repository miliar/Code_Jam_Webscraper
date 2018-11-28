#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>

using namespace std;

typedef long long LL;
typedef pair<int, int> pii;

void solve()
{
	int r, c;
	cin >> r >> c;
	vector<string> cake(r);
	for (string& row : cake)
	{
		cin >> row;
		int i = row.find_first_not_of('?');
		if (i != string::npos)
		{
			fill(row.begin(), row.begin() + i, row[i]);
			for (; i + 1 < c; i++)
				if (row[i + 1] == '?')
					row[i + 1] = row[i];
		}
	}
	for (int i = 0; i < r; i++)
	{
		if (cake[i][0] == '?')
		{
			bool found = false;
			if (i > 0 && cake[i - 1][0] != '?')
			{
				cake[i] = cake[i - 1];
				found = true;
			}
			for (int j = i + 1; j < r && !found; j++)
			{
				if (cake[j][0] != '?')
				{
					cake[i] = cake[j];
					found = true;
				}
			}
		}
	}
	for (string& row : cake)
		cout << row << endl;
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		printf("Case #%d:\n", c);
		solve();
	}
}
