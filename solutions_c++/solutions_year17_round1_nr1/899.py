
#define _CRT_SECURE_NO_WARNINGS
#include<vector>
#include<iostream>

using namespace std;

void going(vector<vector<char> > &map, int dx, int dy)
{
	for (int x = 0; x < map.size(); ++x)
	{
		for (int y = 0; y < map[x].size(); ++y)
		{
			if ( (x + dx < 0) || (y + dy < 0) || (x + dx >= map.size()) || (y + dy >= map[x].size()) )
				continue;
			if (map[x][y] != '?' && map[x + dx][y + dy] == '?')
				map[x + dx][y + dy] = map[x][y];
		}
	}

	for (int x = map.size() - 1; x >=0; --x)
	{
		for (int y = map[x].size() - 1; y >= 0; --y)
		{
			if ((x + dx < 0) || (y + dy < 0) || (x + dx >= map.size()) || (y + dy >= map[x].size()))
				continue;
			if (map[x][y] != '?' && map[x + dx][y + dy] == '?')
				map[x + dx][y + dy] = map[x][y];
		}
	}
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int test;
	cin >> test;
	for (int testNum = 0; testNum < test; ++testNum)
	{
		int row, col;
		cin >> row >> col;
		vector<vector<char> > mapa(row, vector<char>(col));
		for (int i = 0; i < row; ++i)
		{
			for (int j = 0; j < col; ++j)
			{
				cin >> mapa[i][j];
			}
		}

		going(mapa, 0, 1);
		going(mapa, 0, -1);
		going(mapa, 1, 0);
		going(mapa, -1, 0);

		cout << "Case #" << testNum + 1 << ": " << endl;
		for (int i = 0; i < row; ++i)
		{
			for (int j = 0; j < col; ++j)
			{
				cout << mapa[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}