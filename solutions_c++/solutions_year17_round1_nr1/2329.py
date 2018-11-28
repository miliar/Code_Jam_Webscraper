#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

#define DEBUG	0
#define MAX_N	26

int T, t;
int R, C;
char map[MAX_N][MAX_N];
bool isVisited[MAX_N][MAX_N];

void init()
{
	for (int i = 0; i < MAX_N; i++)
	{
		for (int j = 0; j < MAX_N; j++)
		{
			map[i][j] = '.';
			isVisited[i][j] = false;
		}
	}
}

void fill(int row, int col)
{
	int u = 1;
	int d = 1;
	int r = 1;
	int l = 1;

	isVisited[row][col] = true;

	//if ((t == 60) && map[row][col] == 'A')
	if (t == 60)
		cout << "";

	// left
	while (col - l >= 0)
	{
		if (map[row][col - l] != '?' || col - l < 0)
		{
			break;
		}

		map[row][col - l] = map[row][col];
		isVisited[row][col - l] = true;
		l++;
	}
	l--;



	// right
	while (col + r < C)
	{
		if (map[row][col + r] != '?' || col + r >= C)
		{
			//r--;
			break;
		}

		map[row][col + r] = map[row][col];
		isVisited[row][col + r] = true;
		r++;
	}
	r--;

	// up
	bool isOccupied = false;
	while (row - u >= 0)
	{
		for (int i = col - l; i <= col + r; i++)
		{
			if (map[row - u][i] != '?')
			{
				isOccupied = true;
				break;
			}	
		}
		if (isOccupied)
		{
			//u--;
			break;
		}

		for (int i = col - l; i <= col + r; i++)
		{
			map[row - u][i] = map[row][col];
			isVisited[row - u][i] = true;
		}
		u++;
	}
	u--;

	if ((t == 60) && map[row][col] == 'A')
		cout << "";

	// down
	isOccupied = false;
	while (row + d < R)
	{
		for (int i = col - l; i <= col + r; i++)
		{
			if (map[row + d][i] != '?')
			{
				isOccupied = true;
				break;
			}
		}
		if (isOccupied)
		{
			//d--;
			break;
		}

		for (int i = col - l; i <= col + r; i++)
		{
			map[row + d][i] = map[row][col];
			isVisited[row + d][i] = true;
		}
		d++;
	}
	d--;
}

void solve()
{
	if (DEBUG)
	{
		cout << endl;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cout << map[i][j];
			}
			cout << endl;
		}
	}

	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			if(map[i][j] != '?' && !isVisited[i][j])
				fill(i, j);
		}
	}

	cout << endl;
	for (int i = 0; i < R; i++)
	{
		for (int j = 0; j < C; j++)
		{
			cout << map[i][j];
		}
		cout << endl;
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> T;
	for (t = 1; t <= T; t++)
	{
		init();

		cout << "Case #" << t <<": ";

		cin >> R >> C;
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				cin >> map[r][c];
			}
		}
		
		solve();

		//cout << endl;
	}

	return 0;
}
