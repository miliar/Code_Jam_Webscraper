#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

//http://stackoverflow.com/questions/11376288/fast-computing-of-log2-for-64-bit-integers
const int tab64[64] = {
    63,  0, 58,  1, 59, 47, 53,  2,
    60, 39, 48, 27, 54, 33, 42,  3,
    61, 51, 37, 40, 49, 18, 28, 20,
    55, 30, 34, 11, 43, 14, 22,  4,
    62, 57, 46, 52, 38, 26, 32, 41,
    50, 36, 17, 19, 29, 10, 13, 21,
    56, 45, 25, 31, 35, 16,  9, 12,
    44, 24, 15,  8, 23,  7,  6,  5};

int log2_64 (uint64_t value)
{
    value |= value >> 1;
    value |= value >> 2;
    value |= value >> 4;
    value |= value >> 8;
    value |= value >> 16;
    value |= value >> 32;
    return tab64[((uint64_t)((value - (value >> 1))*0x07EDD5E59A4E28C2)) >> 58];
}

int C, R, M;
vector<vector<pair<int, pair<int, int>>>> dp;
vector<string> field;
vector<pair<int, int>> turrets, soldiers;
vector<vector<set<int>>> covered_by;

pair<int, pair<int, int>> get(int a, int b)
{
	if(dp[a][b].first != -1)
		return dp[a][b];

	dp[a][b].first = 0;

	for(int i = 0; i < soldiers.size(); ++i)
	{
		if((b & (1 << i)) == 0)
			continue;

		set<int> canReach;

		vector<vector<bool>> vis(R, vector<bool>(C));
		queue<pair<int, pair<int, int>>> Q;
		Q.emplace(0, soldiers[i]);
		vis[soldiers[i].first][soldiers[i].second] = true;

		while(Q.size())
		{
			int d, c, r;
			pair<int, int> t;
			tie(d, t) = Q.front();
			tie(r, c) = t;
			Q.pop();


			bool good = d < M;
			for(auto tr : covered_by[r][c])
				if(a & (1 << tr))
				{
					canReach.insert(tr);
					good = false;
				}

			if(!good)
				continue;

			vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
			for(auto di : dir)
			{
				int rr = r + di.first;
				int cc = c + di.second;
				if(rr >= 0 && rr < R && cc >= 0 && cc < C && field[rr][cc] != '#' && !vis[rr][cc])
				{
					Q.emplace(d + 1, make_pair(rr, cc));
					vis[rr][cc] = true;
				}
			}
		}

		for(auto tr : canReach)
		{
			auto p = get(a & ~(1 << tr), b & ~(1 << i));
			if(p.first >= dp[a][b].first)
				dp[a][b] = {p.first + 1, make_pair(a & ~(1 << tr), b & ~(1 << i))};
		}
	}

	return dp[a][b];
}

void solve()
{
	turrets.clear();
	soldiers.clear();

	cin >> C >> R >> M;
	field = vector<string>(R);
	for(auto &r : field) cin >> r;

	for(int r = 0; r < R; ++r)
	for(int c = 0; c < C; ++c)
	{
		if(field[r][c] == 'T')
			turrets.emplace_back(r, c);
		if(field[r][c] == 'S')
			soldiers.emplace_back(r, c);
	}

	covered_by = vector<vector<set<int>>>(R, vector<set<int>>(C));
	for(int i = 0; i < turrets.size(); ++i)
	{
		int r, c;
		tie(r, c) = turrets[i];
		vector<pair<int, int>> dir = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
		for(auto d : dir)
		{
			int rr = r, cc = c;
			while(rr >= 0 && rr < R && cc >= 0 && cc < C && field[rr][cc] != '#')
			{
				covered_by[rr][cc].insert(i);
				rr += d.first;
				cc += d.second;
			}
		}
	}

	dp = vector<vector<pair<int, pair<int, int>>>>(1 << turrets.size(), vector<pair<int, pair<int, int>>>(1 << soldiers.size(), make_pair(-1, make_pair(-1, -1))));

	pair<int, int> cur = {(1 << turrets.size()) - 1, (1 << soldiers.size()) - 1};
	get(cur.first, cur.second);
	int dd;
	cout << (dd = dp[cur.first][cur.second].first) << endl;
	while(cur != make_pair(-1, -1) && dd--)
	{
		auto next = dp[cur.first][cur.second].second;
		cout << log2_64(cur.second - next.second) + 1 << " " << log2_64(cur.first - next.first) + 1 << endl;
		cur = next;
	}
}

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(0);

	int T;
	cin >> T;
	for(int i = 1; i <= T; ++i)
	{
		cout << "Case #" << i << ": ";
		solve();
	}
}
