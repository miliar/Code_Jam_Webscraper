#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <bitset>
#include <unordered_map>
#include <unordered_set>

using namespace std;
typedef long long ll;


void solve(int test)
{

	int n, p;
	cin >> n >> p;
	vector<int> v(n);
	map<int, int> ma;
	for (int i = 0; i < n; ++i)
	{
		cin >> v[i];
		v[i] %= p;
		ma[v[i]] ++;
	}
	int ans = ma[0];
	vector<vector<vector<vector<int> > > > dp(ma[1] + 1, vector<vector<vector<int> > >(ma[2] + 1, vector<vector<int> >(ma[3] + 1, vector<int>(p, -1))));
	dp[ma[1]][ma[2]][ma[3]][0] = 0;
	queue<pair<pair<int, int>, pair<int, int> > > q;
	q.push({ {ma[1], ma[2]}, {ma[3], 0} });
	int mxval = -1;
	while (!q.empty())
	{
		int a = q.front().first.first, b=q.front().first.second, c = q.front().second.first, d =q.front().second.second;
		q.pop();
		int val = dp[a][b][c][d];
		mxval = max(mxval, val);
		if (d == 0)
			val++;
		if (a > 0)
		{
			int tmp = d + 1;
			if (tmp >= p)
				tmp -= p;
			if (dp[a - 1][b][c][tmp] == -1)
				q.push({ { a - 1,b },{ c, tmp } });
			dp[a - 1][b][c][tmp] = max(dp[a - 1][b][c][tmp], val);
		}
		if (b > 0)
		{
			int tmp = d + 2;
			if (tmp >= p)
				tmp -= p;
			if (dp[a][b-1][c][tmp] == -1)
				q.push({ { a,b - 1 },{ c, tmp } });
			dp[a][b - 1][c][tmp] = max(dp[a][b - 1][c][tmp], val);
		}
		if (c > 0)
		{
			int tmp = d + 3;
			if (tmp >= p)
				tmp -= p;
			if (dp[a][b][c - 1][tmp] == -1)
				q.push({ { a,b },{ c - 1, tmp } });
			dp[a][b][c - 1][tmp] = max(dp[a][b][c - 1][tmp], val);
		}

	}
	printf("Case #%d: %d\n", test, ans + mxval);
	
}


int main() {
#ifdef _CONSOLE
	freopen("A-large (4).in", "r", stdin);
	freopen("out.txt", "w", stdout);
#endif
	int testNum;
	cin >> testNum;
	for (int test = 1; test <= testNum; ++test)
	{
		solve(test);
	}			

	return 0;
}