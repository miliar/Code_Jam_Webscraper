
#include <iostream>
#include <string>
#include <cmath>
#include <bitset>
#include <algorithm>
#include <map>
#include <vector>
using namespace std;
double eps = 1e-15;
int R, C;
char board[25][25];
struct bound
{
	int T, B, L, R;
};
map<char, bound> m;

void fix()
{
	for (char c = 'A'; c <= 'Z'; c++)
	{
		int minR = R, maxR = -1, minC = C, maxC = -1;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (board[i][j] == c)
				{
					minR = min(minR, i);
					maxR = max(maxR, i);
					minC = min(minC, j);
					maxC = max(maxC, j);
				}
			}
		}
		if (maxR >= 0)
		{
			bound b = { minR, maxR, minC, maxC };
			m[c] = b;
			for (int i = minR; i <= maxR; i++)
			{
				for (int j = minC; j <= maxC; j++)
				{
					board[i][j] = c;
				}
			}
		}
	}
}

bool dfs(int curr)
{
	if (m.size() == curr)
	{
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (board[i][j] == '?')return false;
			}
		}
		return true;
	}
	auto it = m.begin();
	for (int i = 0; i < curr; i++)
	{
		it++;
	}
	bound b = it->second;
	//try vertical
	int top = b.T, bottom = b.B, left = b.L, right = b.R;
	for (int i = b.T - 1; i >= 0; i--)
	{
		bool success = true;
		for (int j = b.L; j <= b.R; j++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			top = i + 1;
			break;
		}
		if (i == 0)
		{
			top = 0;
		}
	}
	for (int i = b.B + 1; i < R; i++)
	{
		bool success = true;
		for (int j = b.L; j <= b.R; j++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			bottom = i - 1;
			break;
		}
		if (i == R - 1)
		{
			bottom = R - 1;
		}
	}
	// find left and right
	for (int j = b.L - 1; j >= 0; j--)
	{
		bool success = true;
		for (int i = top; i <= bottom; i++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			left = j + 1;
			break;
		}
		if (j == 0)
		{
			left = 0;
		}
	}
	for (int j = b.R + 1; j < C; j++)
	{
		bool success = true;
		for (int i = top; i <= bottom; i++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			right = j - 1;
			break;
		}
		if (j == C - 1)
		{
			right = C - 1;
		}
	}
	//have vertical max box, setting now.
	for (int i = top; i <= bottom; i++)
	{
		for (int j = left; j <= right; j++)
		{
			board[i][j] = it->first;
		}
	}
	if (dfs(curr + 1)) return true;
	//undo vertical max box
	for (int i = top; i <= bottom; i++)
	{
		for (int j = left; j <= right; j++)
		{
			board[i][j] = '?';
		}
	}
	for (int i = b.T; i <= b.B; i++)
	{
		for (int j = b.L; j <= b.R; j++)
		{
			board[i][j] = it->first;
		}
	}
	//done undoing, now try horizontal max box
	top = b.T, bottom = b.B, left = b.L, right = b.R;
	for (int j = b.L - 1; j >= 0; j--)
	{
		bool success = true;
		for (int i = b.T; i <= b.B; i++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			left = j + 1;
			break;
		}
		if (j == 0)
		{
			left = 0;
		}
	}
	for (int j = b.R + 1; j < C; j++)
	{
		bool success = true;
		for (int i = b.T; i <= b.B; i++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			right = j - 1;
			break;
		}
		if (j == C - 1)
		{
			right = R - 1;
		}
	}
	// find top and bottom
	for (int i = b.T - 1; i >= 0; i--)
	{
		bool success = true;
		for (int j = left; j <= right; j++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			top = i + 1;
			break;
		}
		if (i == 0)
		{
			top = 0;
		}
	}
	for (int i = b.B + 1; i < R; i++)
	{
		bool success = true;
		for (int j = left; j <= right; j++)
		{
			if (board[i][j] != '?')success = false;
		}
		if (!success)
		{
			bottom = i - 1;
			break;
		}
		if (i == R - 1)
		{
			bottom = R - 1;
		}
	}
	//have horizontal max box, setting now.
	for (int i = top; i <= bottom; i++)
	{
		for (int j = left; j <= right; j++)
		{
			board[i][j] = it->first;
		}
	}
	if (dfs(curr + 1)) return true;
	//undo horizontal max box
	for (int i = top; i <= bottom; i++)
	{
		for (int j = left; j <= right; j++)
		{
			board[i][j] = '?';
		}
	}
	for (int i = b.T; i <= b.B; i++)
	{
		for (int j = b.L; j <= b.R; j++)
		{
			board[i][j] = it->first;
		}
	}
	return false;
}

int main() {
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; tc++)
	{
		m.clear();
		cin >> R >> C;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cin >> board[i][j];
			}
		}
		fix();
		
		dfs(0);
		cout << "Case #" << tc << ":" << endl;
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				cout << board[i][j];
			}
			cout << endl;
		}
	}
}