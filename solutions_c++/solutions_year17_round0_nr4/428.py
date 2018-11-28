/********   All Required Header Files ********/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <deque>
#include <bitset>
#include <iterator>
#include <list>
#include <stack>
#include <map>
#include <set>
#include <functional>
#include <numeric>
#include <utility>
#include <limits>
#include <time.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; ++testCase)
	{
		int N, M;
		cin >> N >> M;
		char **grid = new char*[N];
		for (int i = 0; i < N; ++i)
		{
			grid[i] = new char[N];
			for (int j = 0; j < N; ++j)
			{
				grid[i][j] = '.';
			}
		}

		int oColumn = -1;
		ostringstream oss;
		int count = 0;

		for (int i = 0; i < M; ++i)
		{
			char style;
			int R, C;
			cin >> style >> R >> C;
			if (style == 'x')
			{
				style = 'o';
				++count;
				oss << "o " << (R) << " " << (C) << endl;
			}
			grid[R-1][C-1] = style;
			if (style == 'o') oColumn = C-1;
		}

		if (oColumn == -1)
		{
			for (int i = 0; i < N; ++i)
			{
				if (grid[0][i] == '.')
				{
					oColumn = i;
					grid[0][i] = 'o';
					++count;
					oss << "o 1 " << (i + 1) << endl;
					break;
				}
			}
		}

		if (oColumn == -1)
		{
			oColumn = 0;
			grid[0][0] = 'o';
			++count;
			oss << "o 1 1" << endl;
		}

		for (int i = 0; i < N; ++i)
		{
			if (grid[0][i] == '.')
			{
				grid[0][i] = '+';
				++count;
				oss << "+ 1 " << (i + 1) << endl;
			}
		}

		for (int i = 1; i < N; ++i)
		{
			++count;
			oss << "x " << (i + 1) << " " << ((i - 1 < oColumn) ? i : i+1) << endl;
		}

		for (int i = 1; i < N-1; ++i)
		{
			++count;
			oss << "+ " << N << " " << (i + 1) << endl;
		}

		cout << "Case #" << testCase << ": " << ((N == 1) ? 2 : (3 * N - 2)) << " " << count << endl << oss.str();
	}

	return 0;
}