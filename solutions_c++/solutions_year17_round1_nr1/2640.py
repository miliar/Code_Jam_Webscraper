#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	freopen("a.in", "r", stdin);
	freopen("a.out", "w", stdout);
	int t;
	cin >> t;
	for (int k = 1; k <= t; k++)
	{
		char ch[30][30];
		int r, c;
		cin >> r >> c;
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
				cin >> ch[i][j];
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				if (ch[i][j] != '?' && i == 0)
				{
					int tmp = i;
					tmp++;
					while (ch[tmp][j] == '?')
					{
						ch[tmp][j] = ch[tmp-1][j];
						tmp++;
					}
				}
				else if (ch[i][j] != '?' && i == r-1)
				{
					int tmp = i;
					tmp--;
					while (ch[tmp][j] == '?')
					{
						ch[tmp][j] = ch[tmp+1][j];
						tmp--;
					}
				}
				else 
				{
					int tmp = i, tmp2 = i;
					tmp++;
					while (ch[tmp][j] == '?')
					{
						ch[tmp][j] = ch[tmp-1][j];
						tmp++;
					}
					tmp2--;
					while (ch[tmp2][j] == '?')
					{
						ch[tmp2][j] = ch[tmp2+1][j];
						tmp2--;
					}
				}
			}
		for (int i = 0; i < r; i++)
			for (int j = 0; j < c; j++)
			{
				if (ch[i][j] != '?' && j == 0)
				{
					int tmp = j;
					tmp++;
					while (ch[i][tmp] == '?')
					{
						ch[i][tmp] = ch[i][tmp-1];
						tmp++;
					}
				}
				else if (ch[i][j] != '?' && j == c-1)
				{
					int tmp = j;
					tmp--;
					while (ch[i][tmp] == '?')
					{
						ch[i][tmp] = ch[i][tmp+1];
						tmp--;
					}
				}
				else 
				{
					int tmp = j, tmp2 = j;
					tmp++;
					while (ch[i][tmp] == '?')
					{
						ch[i][tmp] = ch[i][tmp-1];
						tmp++;
					}
					tmp2--;
					while (ch[i][tmp2] == '?')
					{
						ch[i][tmp2] = ch[i][tmp2+1];
						tmp2--;
					}
				}
			}
		cout << "Case #" << k << ": " << endl;
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
				cout << ch[i][j];
			cout << endl;
		}
	}
	return 0;
}