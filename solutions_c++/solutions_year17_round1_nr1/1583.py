#include <iostream>
#include <string>
#include <cmath>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <vector>
#include <algorithm>

using namespace std;

void solve()
{
	int R, C; cin >> R >> C;
	vector<string> a(R);
	for (int i = 0; i < R; ++i) cin >> a[i];

	for (int r = 0; r < R; ++r)
	{
		for (int c = 0; c < C; ++c)
		{
			if (a[r][c] >= 'A' && a[r][c] <= 'Z')
			{
				int cl = c, cr = c;
				while (cl > 0 && a[r][cl - 1] == '?')
				{
					--cl; a[r][cl] = a[r][c] - 'A' + 'a';
				}
				while (cr < C - 1 && a[r][cr + 1] == '?')
				{
					++cr; a[r][cr] = a[r][c] - 'A' + 'a';
				}

				int rd = r + 1;
				while (rd < R)
				{
					bool good = true;
					for (int i = cl; i <= cr; ++i)
					{
						if (a[rd][i] != '?')
						{
							good = false;
							break;
						}
					}
					if (good)
					{
						for (int i = cl; i <= cr; ++i)
						{
							a[rd][i] = a[r][c] - 'A' + 'a';
						}
						++rd;
					}
					else
					{
						break;
					}
				}
				rd = r - 1;
				while (rd >= 0)
				{
					bool good = true;
					for (int i = cl; i <= cr; ++i)
					{
						if (a[rd][i] != '?')
						{
							good = false;
							break;
						}
					}
					if (good)
					{
						for (int i = cl; i <= cr; ++i)
						{
							a[rd][i] = a[r][c] - 'A' + 'a';
						}
						--rd;
					}
					else
					{
						break;
					}
				}
			}
		}
	}

	for (int r = 0; r < R; ++r)
	{
		for (int c = 0; c < C; ++c)
		{
			if (a[r][c] <= 'z' && a[r][c] >= 'a')
			{
				a[r][c] = a[r][c] + 'A' - 'a';
			}
		}
	}
	
	for (int r = 0; r < R; ++r)
	{
		cout << a[r] << endl;
	}
}

int main()
{
	//freopen("i:/input.txt", "rt", stdin);
	//freopen("i:/input.out", "wt", stdout);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": " << endl;
		solve();
	}
	return 0;
}