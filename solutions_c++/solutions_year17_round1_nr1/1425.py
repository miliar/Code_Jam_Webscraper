#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

int R, C;
char grid[50][50];

bool check_row(int row, int ll, int rr)
{
	for (int i = ll; i <= rr; ++i)
		if (grid[row][i] != '?')
			return false;
	return true;
}

void expand(int row, int col)
{
	char elem = grid[row][col];
	int ll, rr, uu, dd;
	ll = rr = col;
	uu = dd = row;
	while (ll > 0 && grid[row][ll - 1] == '?')
		--ll;
	while (rr < C - 1 && grid[row][rr + 1] == '?')
		++rr;
	while (uu > 0 && check_row(uu - 1, ll, rr))
		--uu;
	while (dd < R - 1 && check_row(dd + 1, ll, rr))
		++dd;
	for (int i = uu; i <= dd; ++i)
		for (int j = ll; j <= rr; ++j)
			grid[i][j] = elem;
}

int main()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);

	int T;
	scanf("%d", &T);

	for (int tcase = 1; tcase <= T; ++tcase)
	{
		printf("Case #%d:\n", tcase);
		bool mrk[26];
		memset(mrk, false, sizeof(mrk));
		cin >> R >> C;
		for (int i = 0; i < R; ++i)
			scanf("%s", grid[i]);
		for (int row = 0; row < R; ++row)
			for (int col = 0; col < C; ++col)
			{
				char elem = grid[row][col];
				if (elem != '?' && !mrk[elem - 'A'])
				{
					mrk[elem - 'A'] = true;
					expand(row, col);
				}
			}
		for (int i = 0; i < R; ++i)
			printf("%s\n", grid[i]);
	}

	return 0;
}
