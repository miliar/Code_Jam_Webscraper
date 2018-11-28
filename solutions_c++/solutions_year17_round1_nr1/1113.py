#include <iostream>
#include <fstream>
#include <cstdlib>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <sstream>
#include <iomanip>
#include <cstring>
#include <cmath>
#include <ctime>
#include <random>
#include <climits>
#include <queue>
#include <numeric>
#include <thread>
using namespace std;
#define MAXN 255
char board[MAXN][MAXN];
int main() {

#ifdef DEBUG
	ifstream cin("in.txt");
	ofstream cout("out.txt");
	//freopen("in.txt", "r",stdin);
	//freopen("out.txt", "w",stdout);
#endif 
	int T, R, C;
	cin >> T;
	char ch;
	for (size_t t = 0; t < T; t++)
	{
		cin >> R >> C;
		for (size_t i = 0; i < R; i++)
		{
			for (size_t j = 0; j < C; j++)
			{
				cin >> board[i][j];
			}
		}
		for (int i = 0; i < R; i++)
		{
			for (int j = 0; j < C; j++)
			{
				if (board[i][j] == '?')
				{
					if (j - 1 >= 0 && board[i][j - 1] != '?')
						board[i][j] = board[i][j - 1];
				}				
			}
		}
		for (int i = R-1; i >=0; i--)
		{
			for (int j = C-1; j >=0; j--)
			{
				if (board[i][j] == '?')
				{
					if (j+1 < C && board[i][j + 1] != '?')
						board[i][j] = board[i][j + 1];
				}
			}
		}
		for (int i = 0; i < R; i++)
		{
			if (i - 1 >=0&&board[i][0] == '?'&&board[i - 1][0] != '?')
			{
				for (int j = 0; j < C; j++)
				{
					board[i][j] = board[i - 1][j];
				}
			}
		}
		for (int i = R-1; i >=0; i--)
		{
			if (i+1<R&&board[i][0]=='?'&&board[i+1][0]!='?')
				for (int j = 0; j < C; j++)
				{
					board[i][j] = board[i + 1][j];
				}
		}
		cout << "Case #" << t + 1 << ":" << endl;
		for (size_t i = 0; i < R; i++)
		{
			for (size_t j = 0; j < C; j++)
			{
				cout << board[i][j];
			}
			cout << endl;
		}
	}
	return 0;
}
