#include <iostream>
#include <string>
#include <ctype.h>

using namespace std;

string board[26];

int R, C;

inline void init()
{
	cin >> R >> C;

	for (int i = 0; i < R; i++)
		cin >> board[i];
}

void fill(int r, int c)
{
	int i;

	for (i = c - 1; i >= 0 && board[r][i] == '?'; i--)
		board[r][i] = board[r][c];

	for (i = c + 1; i < C && board[r][i] == '?'; i++)
		board[r][i] = board[r][c];
}

char findc(int r, int c)
{
	int i;

	for (i = r - 1; i >= 0; i--)
		if (board[i][c] != '?')
			return board[i][c];

	for (i = r + 1; i < R; i++)
		if (board[i][c] != '?')
			return board[i][c];

	return '0';
}

void fillcol(int r, int c, char ch)
{
	int i;

	for (i = r; i >= 0 && board[i][c] == '?'; i--)
		board[i][c] = ch;

	for (i = r + 1; i < R && board[i][c] == '?'; i++)
		board[i][c] = ch;
}

inline void solve()
{
	int i, j;

	for (i = 0; i < R; i++)
		for (j = 0; j < C; j++)
			if (board[i][j] != '?')
				fill(i, j);

	for (i = 0; i < R; i++)
		for (j = 0; j < C; j++)
			if (board[i][j] == '?')
				fillcol(i, j, findc(i, j));

	for (i = 0; i < R; i++)
		cout << board[i] << "\n";
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	ios::sync_with_stdio(0);

	int T, i;

	cin >> T;

	for (i = 1; i <= T; i++)
	{
		init();
		cout << "Case #" << i << ":\n";
		solve();
	}

	return 0;
}