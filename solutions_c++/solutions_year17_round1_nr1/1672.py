#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FILE_NAME "A-large"

using namespace std;

int main()
{
	freopen(FILE_NAME ".in", "r", stdin);
	freopen(FILE_NAME ".out", "w", stdout);
	
	int numTestCaces = 0;
	cin >> numTestCaces;
	for(int Case = 1; Case <= numTestCaces; ++Case)
	{
		int r, c;
		cin >> r >> c;
		//cerr << r << ' ' << c;
		std::vector<string> g(r);
		for(int i = 0; i < r; ++i)
			cin >> g[i];
		char cl = '?';
		for(int i = 0; i < r; ++i)
		{
			cl = '?';
			for(int j = 0; j < c; ++j)
			{
				if(g[i][j] != '?')
				{
					cl = g[i][j];
					for(int ii = i; ii >= 0; --ii)
					{
						for(int jj = j; jj >= 0; --jj)
						{
							if(g[ii][jj] == '?')
								g[ii][jj] = cl;
						}
					}
				}
				else if(cl != '?')
				{
					for(int ii = i; ii >= 0; --ii)
					{
						if(g[ii][j] == '?')
							g[ii][j] = cl;
					}
				}
			}
			//cerr << i << endl;
		}
		cl = '?';
		for(int j = 0; j < c; ++j)
			for(int i = 0; i < r; ++i)
			{
				if(g[i][j] != '?')
					cl = g[i][j];
				else
					g[i][j] = cl;
			}

		cout << "Case #" << Case << ": ";
		cout << endl;
		for(int i = 0; i < r; ++i)
			cout << g[i] << endl;
	}

	return 0;
}
