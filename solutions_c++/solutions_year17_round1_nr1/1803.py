#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <typeinfo>
#include <functional>
using namespace std;
char grid[30][30];



int main()
{
	int T,R,C;

	vector<char> init;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> R >> C;
		for (int row = 0; row < R; row++)
		{
			char now = '?';
			for (int col = 0; col < C; col++)
			{
				cin >> grid[row][col];
				if (grid[row][col] != '?')
				{
					now = grid[row][col];
					for (int k = col - 1; 0 <= k; k--)
					{
						if (grid[row][k] == '?')
						{
							grid[row][k] = now;
						}
						else{
							break;
						}
					}
				}
				else{
					grid[row][col] = now;
				}
				//vector< char >::iterator cIter = find(init.begin(), init.end(), grid[row][col]);
				//if (cIter == init.end()){
				//	init.push_back(grid[row][col]);
				//}
			}
			if (now == '?' && row != 0)
			{
				for (int col = 0; col < C; col++)
				{
					grid[row][col] = grid[row - 1][col];
				}
			}
		}
		for (int row = R -1 ; 0<=row; row--)
		{
			for (int col = 0; col < C; col++)
			{
				if (grid[row][col] == '?')
				{
					grid[row][col] = grid[row + 1][col];
				}

			}
		}

		cout << "Case #" << i + 1 << ":"<<endl;
		for (int row = 0; row < R; row++)
		{
			for (int col = 0; col < C; col++)
			{
				cout << grid[row][col];
			}
			cout << endl;
		}
	}
	return 0;
}