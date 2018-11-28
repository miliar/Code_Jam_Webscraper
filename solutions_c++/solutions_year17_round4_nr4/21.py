#include <bits/stdc++.h>
#define NOMINMAX
#define WIN32_LEAN_AND_MEAN
#include <windows.h>
using namespace std;

vector<pair<int, int>> sol, tur;
int r, c, m;

char dat[33][33];
int idx[33][33];
bool vis[33][33];
int dp[1024][1024];
bool v[1024][1024];

vector<int> get_turrets(int x, int y, int tst)
{
    vector<int> ret;
    for (int i = x - 1; i >= 0; i--) if (dat[i][y] == 'T' && (tst & (1 << idx[i][y]))) ret.push_back(idx[i][y]); else if (dat[i][y] == '#') break;
    for (int i = x + 1; i < r; i++) if (dat[i][y] == 'T' && (tst & (1 << idx[i][y]))) ret.push_back(idx[i][y]); else if (dat[i][y] == '#') break;
    for (int i = y - 1; i >= 0; i--) if (dat[x][i] == 'T' && (tst & (1 << idx[x][i]))) ret.push_back(idx[x][i]); else if (dat[x][i] == '#') break;
    for (int i = y + 1; i < c; i++) if (dat[x][i] == 'T' && (tst & (1 << idx[x][i]))) ret.push_back(idx[x][i]); else if (dat[x][i] == '#') break;
    return ret;
}

bool blocked(int x, int y, int tst)
{
    if (dat[x][y] == '#') return true;
    if (dat[x][y] == 'T' && (tst & (1 << idx[x][y]))) return true;
    return false;
}

int D(int sst, int tst)
{
    if (sst == 0 || tst == 0) return 0;

    if (v[sst][tst] == false)
    {
        v[sst][tst] = true;
        dp[sst][tst] = 0;

        for (int i = 0; i < sol.size(); i++)
        {
            if (!(sst & (1 << i))) continue;

            memset(vis, 0, sizeof(vis));
            queue<tuple<int, int, int>> que;
            vis[sol[i].first][sol[i].second] = true;
            que.emplace(sol[i].first, sol[i].second, 0);

            while (que.empty() == false)
            {
                int x, y, w;
                tie(x, y, w) = que.front();
                que.pop();

                auto adj = get_turrets(x, y, tst);
                if (adj.empty() == false)
                {
                    for (int t : adj) dp[sst][tst] = max(dp[sst][tst], D(sst - (1 << i), tst - (1 << t)) + 1);
                    continue;
                }

                if (w >= m) continue;

#define F(a, b) if (x+a >= 0 && x+a < r && y+b >= 0 && y+b < c && !blocked(x+a, y+b, tst) && vis[x+a][y+b] == false) vis[x+a][y+b] = true, que.emplace(x+a, y+b, w+1)
                F(1, 0);
                F(0, 1);
                F(-1, 0);
                F(0, -1);
#undef F
            }
        }
    }

    return dp[sst][tst];
}

void recur(int sst, int tst)
{
    int d = D(sst, tst);
    if (d == 0) return;

    for (int i = 0; i < sol.size(); i++)
    {
        if (!(sst & (1 << i))) continue;

        memset(vis, 0, sizeof(vis));
        queue<tuple<int, int, int>> que;
        vis[sol[i].first][sol[i].second] = true;
        que.emplace(sol[i].first, sol[i].second, 0);

        while (que.empty() == false)
        {
            int x, y, w;
            tie(x, y, w) = que.front();
            que.pop();

            auto adj = get_turrets(x, y, tst);
            if (adj.empty() == false)
            {
                for (int t : adj)
                {
                    if (d == D(sst - (1 << i), tst - (1 << t)) + 1)
                    {
                        printf("%d %d\n", i + 1, t + 1);
                        recur(sst - (1 << i), tst - (1 << t));
                        return;
                    }
                }
                continue;
            }

            if (w >= m) continue;

#define F(a, b) if (x+a >= 0 && x+a < r && y+b >= 0 && y+b < c && !blocked(x+a, y+b, tst) && vis[x+a][y+b] == false) vis[x+a][y+b] = true, que.emplace(x+a, y+b, w+1)
            F(1, 0);
            F(0, 1);
            F(-1, 0);
            F(0, -1);
#undef F
		}
	}

}

int main()
{
	int T;
	scanf("%d", &T);
	for (int TT = 1; TT <= T; TT++)
	{
        fprintf(stderr, "%d\n", TT);
		sol.clear();
		tur.clear();
		printf("Case #%d: ", TT);
        memset(v, 0, sizeof(v));

		scanf("%d%d%d", &c, &r, &m);
		for (int i = 0; i < r; i++)
		{
			scanf("%s", dat[i]);
		}

		for (int i = 0; i < r; i++)
		{
			for (int j = 0; j < c; j++)
			{
				if (dat[i][j] == 'S')
				{
					idx[i][j] = sol.size();
					sol.emplace_back(i, j);
				}
				else if (dat[i][j] == 'T')
				{
					idx[i][j] = tur.size();
					tur.emplace_back(i, j);
				}
			}
		}

		printf("%d\n", D((1 << sol.size()) - 1, (1 << tur.size()) - 1));
		recur((1 << sol.size()) - 1, (1 << tur.size()) - 1);
	}
}

