#include <iostream>
#include <cmath>
#include <string>
#include <map>
#include <fstream>
#include <sstream>
#include <stack>
#include <set>
#include <bitset>
#include <queue>
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <unordered_map>
#include <functional>
#include <set>
#include <map>
using namespace std;
void helper(vector<string>& board, int x, int y,int r,int c, int flag,char w)
{
	if (x < 0 || x >= r || y < 0 || y >= c)return;
	if (board[x][y] == '?')board[x][y] = w;
	else return;
	if (flag == 1)helper(board, x - 1, y, r, c, flag, w);
	if (flag == 0)helper(board, x + 1, y, r, c, flag, w);
	if (flag == 2)helper(board, x, y-1, r, c, flag, w);
	if (flag == 3)helper(board, x, y+1, r, c, flag, w);
}
int main()
{
	int T;
	freopen("d:/codejam/A-small-attempt0_1.in", "r", stdin);
	freopen("d:/codejam/415.out", "w", stdout);
	cin >> T;
	for (int cas = 1; cas <= T; cas++)
	{
		int r, c;
		cin >> r >> c;
		vector<string> board(r);
		for (int i = 0; i < r; i++)cin >> board[i];
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (board[i][j] != '?')
				{
					helper(board, i - 1, j, r, c, 1, board[i][j]);
					helper(board, i + 1, j, r, c, 0, board[i][j]);
				}
			}
		}
		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (board[i][j] != '?')
				{
					helper(board, i, j-1, r, c, 2, board[i][j]);
					helper(board, i, j+1, r, c, 3, board[i][j]);
				}
			}
		}
		printf("Case #%d:\n", cas);
		for (int i = 0; i < r; i++)
			cout << board[i] << endl;
	}
	return 0;
}
