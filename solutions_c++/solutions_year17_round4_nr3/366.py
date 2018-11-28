#include <bits/stdc++.h>
#define LFT 0
#define UP 1
#define RGT 2
#define DWN 3
using namespace std;
typedef long long LL;
typedef pair<int, int> pii;

const LL MOD = 1000000007LL;

char grid[55][55];
vector<pii> lsr;
bool imps[2525][2];
int lsr_num[55][55];
vector<pii> lsr_inc[55][55];
int R, C;

vector<pii> grph[2525][2];
bool vis[2525][2];

int sol[2525];

bool is_rch(pii nd, pii dst)
{
	bool rch = false;
	if (vis[nd.first][nd.second])
		return false;
	vis[nd.first][nd.second] = true;
	if (nd.first == dst.first && nd.second == dst.second)
		return true;
	for (int i = 0; i < grph[nd.first][nd.second].size() && !rch; i++)
		rch = is_rch(grph[nd.first][nd.second][i], dst);

	return rch;
}

bool is_ok(pii rc, int dir, bool mark, int lsr_n, int ornt)
{
	switch (dir)
	{
		case LFT: rc.second--; break;
		case UP: rc.first--; break;
		case RGT: rc.second++; break;
		case DWN: rc.first++; break;
	}
	if (rc.first < 0 || rc.second < 0)
		return true;
	if (rc.first >= R || rc.second >= C)
		return true;
	if (grid[rc.first][rc.second] == '#')
		return true;
	else if (grid[rc.first][rc.second] == '-' || grid[rc.first][rc.second] == '|')
		return false;
	else if (grid[rc.first][rc.second] == '\\')
	{
		switch(dir)
		{
			case LFT: dir = UP; break;
			case UP: dir = LFT; break;
			case RGT: dir = DWN; break;
			case DWN: dir = RGT; break;
		}
	}
	else if (grid[rc.first][rc.second] == '/')
	{
		switch(dir)
		{
			case LFT: dir = DWN; break;
			case UP: dir = RGT; break;
			case RGT: dir = UP; break;
			case DWN: dir = LFT; break;
		}
	}
	else if (grid[rc.first][rc.second] == '.' && mark)
	{
		bool alr_prs = false;
		for (int i = 0; i < lsr_inc[rc.first][rc.second].size(); i++)
			if (lsr_inc[rc.first][rc.second][i] == make_pair(lsr_n, ornt))
				alr_prs = true;
		if (!alr_prs)
			lsr_inc[rc.first][rc.second].push_back(make_pair(lsr_n, ornt));
	}

	return is_ok(rc, dir, mark, lsr_n, ornt);
}

int main()
{
	int T;

	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; i++)
			scanf("%s", grid[i]);

		lsr.clear();
		memset(lsr_num, 0, sizeof(lsr_num));

		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				char ch = grid[r][c];
				if (ch == '|' || ch == '-')
				{
					lsr_num[r][c] = lsr.size();
					grph[lsr.size()][0].clear();
					grph[lsr.size()][1].clear();
					lsr.push_back(make_pair(r, c));
				}
				lsr_inc[r][c].clear();
			}
		}

		bool rimp = false;
		memset(imps, false, sizeof(imps));
		for (int i = 0; i < lsr.size(); i++)
		{
			if (is_ok(lsr[i], LFT, false, i, 0) && is_ok(lsr[i], RGT, false, i, 0))
			{
				is_ok(lsr[i], LFT, true, i, 0);
				is_ok(lsr[i], RGT, true, i, 0);
			}
			else
			{
				imps[i][0] = true;
			}

			if (is_ok(lsr[i], UP, false, i, 1) && is_ok(lsr[i], DWN, false, i, 1))
			{
				is_ok(lsr[i], UP, true, i, 1);
				is_ok(lsr[i], DWN, true, i, 1);
			}
			else
			{
				imps[i][1] = true;
			}
			if (imps[i][0] && imps[i][1])
				rimp = true;
		}
		if (rimp)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		bool chng = true;
		while (chng && !rimp)
		{
			chng = false;
			for (int r = 0; r < R && !rimp; r++)
			{
				for (int c = 0; c < C; c++)
				{
					if (grid[r][c] != '.')
						continue;
					for (int i = 0; i < lsr_inc[r][c].size(); i++)
					{
						while (i < lsr_inc[r][c].size() &&
							imps[lsr_inc[r][c][i].first][lsr_inc[r][c][i].second])
						{
							lsr_inc[r][c].erase(lsr_inc[r][c].begin() + i);
						}
					}
					if (lsr_inc[r][c].size() == 0)
					{
						rimp = true;
						break;
					}
					if (lsr_inc[r][c].size() == 1)
					{
						pii ln_o = lsr_inc[r][c][0];
						if (imps[ln_o.first][1 - ln_o.second] == false)
						{
							chng = true;
							imps[ln_o.first][1 - ln_o.second] = true;
						}
					}
				}
			}
		}
		if (rimp)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}

		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				if (lsr_inc[r][c].size() != 2)
					continue;
				pii nd1 = lsr_inc[r][c][0];
				pii nd2 = lsr_inc[r][c][1];
				grph[nd1.first][1 - nd1.second].push_back(nd2);
				grph[nd2.first][1 - nd2.second].push_back(nd1);
			}
		}

		memset(sol, 0, sizeof(sol));
		for (int i = 0; i < lsr.size(); i++)
		{
			if (imps[i][0] && imps[i][1])
			{
				rimp = true;
				break;
			}
			if (imps[i][0])
			{
				sol[i] = 1;
				continue;
			}
			if (imps[i][1])
			{
				sol[i] = 0;
				continue;
			}
			memset(vis, false, sizeof(vis));
			bool rch0to1 = is_rch(make_pair(i, 0), make_pair(i, 1));
			memset(vis, false, sizeof(vis));
			bool rch1to0 = is_rch(make_pair(i, 1), make_pair(i, 0));
			if (rch1to0 && rch0to1)
			{
				rimp = true;
				break;
			}
			sol[i] = rch1to0 ? 0 : 1;
		}
		if (rimp)
		{
			printf("Case #%d: IMPOSSIBLE\n", t);
			continue;
		}
		printf("Case #%d: POSSIBLE\n", t);
		for (int r = 0; r < R; r++)
		{
			for (int c = 0; c < C; c++)
			{
				if (grid[r][c] == '-' || grid[r][c] == '|')
				{
					putchar(sol[lsr_num[r][c]] == 0 ? '-' : '|');
				}
				else
					putchar(grid[r][c]);
			}
			printf("\n");
		}
	}


	return 0;
}