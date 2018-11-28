#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <map>
#include <queue>
#include <algorithm>
using namespace std;


typedef long long i64;
const i64 inf = 1.05e9;
typedef vector<int> vertex;
typedef vector<vertex> graph;

const int dxs[] = {-1, 0, 1, 0};
const int dys[] = {0, 1, 0, -1};

struct q_info {
	int x, y, d, id;
};

void scc_dfs(int v, int k, vector<bool>& used, vector<int>& vs, vector<int>& cmp, graph& g)
{
	used[v] = true;
	cmp[v] = k;
	for(auto w : g[v]) {
		if(!used[w]) scc_dfs(w, k, used, vs, cmp, g);
	}
	vs.push_back(v);
}

vector<int> scc(graph& g)
{
	const int n = g.size();
	graph rg(n);

	for(int v = 0; v < n; ++v) {
		for(auto w : g[v])
			rg[w].push_back(v);
	}

	vector<bool> used(n);
	vector<int> vs, dummy_vs;
	vector<int> cmp(n), dummy_cmp(n);
	int k = 0;

	for(int v = 0; v < n; ++v) {
		if(!used[v])
			scc_dfs(v, -1, used, vs, dummy_cmp, g);
	}

	fill(used.begin(), used.end(), false);

	for(int i = vs.size() - 1; i >= 0; --i) {
		const int v = vs[i];
		if(!used[v])
			scc_dfs(v, k++, used, dummy_vs, cmp, rg);
	}

	return cmp;
}

void solve(int casenum)
{
	int h, w;
	vector<vector<char>> board;

	scanf("%d%d", &h, &w);
	board.resize(h);
	for(int i = 0; i < h; ++i) {
		char buf[64];
		scanf("%s", buf);
		for(int k = 0; buf[k] != '\0'; ++k) {
			if(buf[k] == '-' || buf[k] == '|')
				buf[k] = '*';
			board[i].push_back(buf[k]);
		}
	}

	pair<int,int> beams_init = {-1, -1};
	vector<pair<int,int>> beams(w * h, beams_init);
	vector<pair<bool,bool>> bad;
	int mac = 0;
	for(int sy = 0; sy < h; ++sy) {
		for(int sx = 0; sx < w; ++sx) {

			char sc = board[sy][sx];
			if(sc != '*')
				continue;

			queue<q_info> q;

			for(int d = 0; d < 4; ++d) {
				int x = sx + dxs[d];
				int y = sy + dys[d];
				q.push({x, y, d, d});
			}

			bool d_bad[4] = {false};

			while(!q.empty()) {

				auto v = q.front();
				q.pop();

				int x = v.x;
				int y = v.y;
				int dir = v.d;
				int idir = v.id;

				if(x < 0 || x >= w || y < 0 || y >= h)
					continue;
				char c = board[y][x];

				if(c == '#')
					continue;
				if(c == '*') {
					d_bad[idir] = true;
					continue;
				}

				if(c == '/' || c == '\\') {
					if(c == '\\') dir = 3 - dir;
					if(c == '/') dir = dir ^ 1;
					x = x + dxs[dir];
					y = y + dys[dir];
					q.push({x, y, dir, idir});
					continue;
				}

				int vert = (dir & 1);
				int i_vert = (idir & 1);

				if(vert)
					beams[y * w + x].first = mac * 2 + (i_vert ? 0 : 1);
				else
					beams[y * w + x].second = mac * 2 + (i_vert ? 0 : 1);

				x = x + dxs[dir];
				y = y + dys[dir];
				q.push({x, y, dir, idir});
			}

			bad.push_back({d_bad[1] || d_bad[3], d_bad[0] || d_bad[2]});
			mac += 1;
		}
	}

	const int n = mac;
	vector<vector<bool>> edges(n * 2, vector<bool>(n * 2));

	for(int x = 0; x < w; ++x) {
		for(int y = 0; y < h; ++y) {

			if(board[y][x] == '.') {
				int a = beams[y * w + x].first;
				int b = beams[y * w + x].second;
				//printf("beam: %d %d\n", a, b);
				if(a != -1 && b != -1) {
					edges[a^1][b] = true;
					edges[b^1][a] = true;
				} else if(a != -1) {
					edges[a^1][a] = true;
				} else if(b != -1) {
					edges[b^1][b] = true;
				} else {
					edges[0][1] = edges[1][0] = true;
				}
			}
		}
	}

	for(int i = 0; i < n; ++i) {
		if(bad[i].first) edges[i * 2 + 0][i * 2 + 1] = true;
		if(bad[i].second) edges[i * 2 + 1][i * 2 + 0] = true;
	}

	graph g(n * 2);

	for(int i = 0; i < n * 2; ++i) {
		for(int j = 0; j < n * 2; ++j) {
			if(edges[i][j]) {
				g[i].push_back(j);
				//printf("%d -> %d\n", i, j);
			}
		}
	}

	auto cmp = scc(g);

	for(int i = 0; i < n; ++i) {
		if(cmp[i * 2 + 0] == cmp[i * 2 + 1]) {
			//printf("%d %d\n", i * 2 + 0, i * 2 + 1);
			printf("Case #%d: IMPOSSIBLE\n", casenum);
			return;
		}
	}

	int b_idx = 0;

	printf("Case #%d: POSSIBLE\n", casenum);
	for(int y = 0; y < h; ++y) {
		char buf[64] = {0};
		for(int x = 0; x < w; ++x) {
			char c = board[y][x];
			if(c == '*') {
				bool vert = cmp[b_idx * 2 + 0] > cmp[b_idx * 2 + 1];
				c = (vert ? '|' : '-');
				b_idx += 1;
			}
			buf[x] = c;
		}
		printf("%s\n", buf);
	}
}

int main()
{
	int testcase;

	scanf("%d", &testcase);
	for(int i = 1; i <= testcase; ++i)
		solve(i);

	return 0;
}
