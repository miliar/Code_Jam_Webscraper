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

#include "InfInt.h"

using namespace std;

int main()
{
    int T;
    cin >> T;
    for (int t = 1; t <= T; ++t)
    {
		int R, C;
		cin >> R >> C;

		char M[25][25],N[25][25];
		for (int i = 0; i < R; ++i)
		{
			string line;
			cin >> line;
			for (int j = 0; j < C; ++j)
			{
				M[i][j] = N[i][j] = line[j];
			}
		}

		for (int i = 0; i < R; ++i)
		{
			for (int j = 0; j < C; ++j)
			{
				if (M[i][j] != '?')
				{
					int left = 0, right = 0, up = 0, down = 0;
					for (int k = i - 1; k >= 0 && N[k][j] == '?'; --k, ++up);
					for (int k = i + 1; k < R && N[k][j] == '?'; ++k, ++down);
					for (int k = j - 1; k >= 0 && N[i][k] == '?'; --k, ++left);
					for (int k = j + 1; k < C && N[i][k] == '?'; ++k, ++right);
					int horizontal = left + right + 1;
					int vertical = up + down + 1;
					if (horizontal > 1 || vertical > 1)
					{
						if (horizontal > 1)
						{
							for (int k = j-left; k <= j+right; ++k)
							{
								N[i][k] = M[i][j];
							}
							for (int k = i - 1; k >= 0 ; --k)
							{
								bool found = true;
								for (int l = j - left; l <= j + right; ++l)
									if (N[k][l] != '?') { found = false; break; }
								if (found)
									for (int l = j - left; l <= j + right; ++l)
										N[k][l] = M[i][j];
								else break;
							}
							for (int k = i + 1; k < R ; ++k)
							{
								bool found = true;
								for (int l = j - left; l <= j + right; ++l)
									if (N[k][l] != '?') { found = false; break; }
								if (found)
									for (int l = j - left; l <= j + right; ++l)
										N[k][l] = M[i][j];
								else break;
							}
						}
						else
						{
							for (int k = i-up; k <= i+down; ++k)
							{
								N[k][j] = M[i][j];
							}
							for (int k = j - 1; k >= 0; --k)
							{
								bool found = true;
								for (int l = i - up; l <= i + down; ++l)
									if (N[l][k] != '?') { found = false; break; }
								if (found)
									for (int l = i - up; l <= i + down; ++l)
										N[l][k] = M[i][j];
								else break;
							}
							for (int k = j + 1; k < C; ++k)
							{
								bool found = true;
								for (int l = i - up; l <= i + down; ++l)
									if (N[l][k] != '?') { found = false; break; }
								if (found)
									for (int l = i - up; l <= i + down; ++l)
										N[l][k] = M[i][j];
								else break;
							}
						}
					}
				}

			}
		}

		cout << "Case #" << t << ": ";
		for (int i = 0; i < R; ++i)
		{
			cout << endl;
			for (int j = 0; j < C; ++j)
				cout << N[i][j];
		}
		cout << endl;
    }

    return 0;
}
