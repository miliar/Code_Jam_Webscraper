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
	string s; cin >> s;
	int n = s.length(), k, answer = 0; cin >> k;

	for (int i = 0; i < n; ++i)
	{
		if (s[i] == '-')
		{
			if (i + k > n)
			{
				cout << "IMPOSSIBLE" << endl;
				return;
			}
			else
			{
				++answer;
				for (int j = 0; j < k; ++j)
				{
					int z = i + j;
					if (s[z] == '+')
						s[z] = '-';
					else
						s[z] = '+';
				}
			}
		}
	}

	cout << answer << endl;
}

int main()
{
	//freopen("i:/input.txt", "rt", stdin);
	//freopen("i:/input.out", "wt", stdout);

	int T; cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		cout << "Case #" << t << ": ";
		solve();
	}
	return 0;
}