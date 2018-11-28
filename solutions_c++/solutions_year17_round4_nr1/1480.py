#include <iostream>
#include <algorithm>
#include <vector>
#include <functional>
#include <map>

using namespace std;

int solve(vector<int>& state, map<vector<int>, int>& table, int p)
{
	int res = 0;
	if (table.count(state))
	{
		res = table[state];
	}
	else
	{
		int r = state[p];
		for (int i = 1; i < p; i++)
		{
			if (state[i] > 0)
			{
				state[i]--;
				state[p] = (r + i) % p;
				res = max(res, solve(state, table, p));
				state[i]++;
			}
		}
		state[p] = r;
		res += (r == 0);
		table[state] = res;
	}
	return res;
}

int main()
{
	int t;
	cin >> t;
	for (int c = 1; c <= t; c++)
	{
		int n, p, a, zeroes;
		cin >> n >> p;
		vector<int> initial(p + 1, 0);
		while (n--)
		{
			cin >> a;
			initial[(1000 * p - a) % p]++;
		}
		zeroes = initial[0];
		initial[0] = 0;
		map<vector<int>, int> table;
		vector<int> bottom(p + 1, 0);
		for (a = 0; a < p; a++)
		{
			bottom[p] = a;
			table[bottom] = 0;
		}
		printf("Case #%d: %d\n", c, zeroes + solve(initial, table, p));
	}
}
