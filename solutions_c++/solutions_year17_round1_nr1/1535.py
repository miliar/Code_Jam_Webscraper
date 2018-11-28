#include <iostream>

using namespace std;

const int Max = 33;
char pole[Max][Max];
int n, m;

void solve(int num)
{
	cin >> n >> m;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cin >> pole[i][j];
		}
	}
	int first = 0;
	for (int i = 1; i <= n; i++)
	{
		bool Have = false;
		char color = ' ';
		for (int j = 1; j <= m; j++)
		{
			if (pole[i][j] != '?')
			{
				color = pole[i][j];
				if (!Have)
				{
					Have = true;
					for (int z = 1; z <= j; z++)
					{
						pole[i][z] = color;
					}
				}
			}
			else
			{
				if (Have)
				{
					pole[i][j] = color;
				}
			}
		}
		if (Have)
		{
			if (first == 0)
			{
				first = i;
			}
		}
		if (!Have)
		{
			if (first != 0)
			{
				for (int j = 1; j <= m; j++)
				{
					pole[i][j] = pole[i - 1][j];
				}
			}
		}
	}
	for (int i = first - 1; i >= 1; i--)
	{
		for (int j = 1; j <= m; j++)
		{
			pole[i][j] = pole[i + 1][j];
		}
	}
	cout << "Case #" << num << ":" << endl;
	for (int i = 1; i <= n; i++)
	{
		for (int j = 1; j <= m; j++)
		{
			cout << pole[i][j];
		}
		cout << endl;
	}
	return;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("Answer.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 1; i <= T; i++)
	{
		solve(i);
	}
	return 0;
}