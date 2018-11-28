#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

void fillLetters(vector<string>& cake)
{
	int n = cake.size(), m = cake[0].size();
	int filledRows = 0;

	for (int i = 0; i < n; ++ i)
	{
		char last = 0;
		int filledCols = 0;
		for (int j = 0; j < m; ++ j) if (cake[i][j] != '?')
		{
			last = cake[i][j];
			for (int x = filledRows; x <= i; ++ x)
				for (int y = filledCols; y <= j; ++ y)
					cake[x][y] = last;

			filledCols = j + 1;
		}

		if (last > 0)
		{
			for (int x = filledRows; x <= i; ++ x)
				for (int y = filledCols; y < m; ++ y)
					cake[x][y] = last;
			filledRows = i + 1;
		}
	}

	for (int x = filledRows; x < n; ++ x)
		for (int y = 0; y < m; ++ y)
			cake[x][y] = cake[x-1][y];
}

int main()
{
	int tc;
	cin >> tc;
	for (int i = 1; i <= tc; ++ i)
	{
		int n, m;
		vector<string> cake;
		cin >> n >> m;
		cake.resize(n);
		for (int x = 0; x < n; ++ x) cin >> cake[x];

		fillLetters(cake);
		cout << "Case #" << i << ":\n";
		for (int x = 0; x < n; ++ x) cout << cake[x] << "\n";
	}
}

