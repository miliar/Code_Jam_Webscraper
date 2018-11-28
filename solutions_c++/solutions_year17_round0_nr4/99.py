#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

#define each(it,o) for(auto it = (o).begin(); it != (o).end(); ++ it)
int bipartiteMatching(const vector<vector<int> > &g, vector<int> &match) {
	int nleft = g.size(), nright = 0;
	each(es, g) if (!es->empty()) nright = max(nright, *max_element(es->begin(), es->end()) + 1);
	vi matchL(nleft, -1), matchR(nright, -1), prev(nleft), seen(nleft, -1);
	rep(i, nleft) {
		vi stk; stk.push_back(i);
		seen[i] = i; prev[i] = -1;
		while (!stk.empty()) {
			int v = stk.back(); stk.pop_back();
			each(ui, g[v]) {
				int u = *ui;
				int j = matchR[u];
				if (j == -1) {
					while (v != -1) {
						matchR[u] = v;
						swap(u, matchL[v]);
						v = prev[v];
					}
					goto break_;
				} else if (seen[j] < i) {
					seen[j] = i; prev[j] = v;
					stk.push_back(j);
				}
			}
		}
	break_:;
	}
	match.assign(matchL.begin(), matchL.end());
	return (int)matchL.size() - count(matchL.begin(), matchL.end(), -1);
}


int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int N; int K;
		scanf("%d%d", &N, &K);
		vector<bool> row(N), col(N), diag1(N * 2 - 1), diag2(N * 2 - 1);
		int ans = 0;
		vector<vector<int>> original(N, vector<int>(N, 0));
		rep(i, K) {
			char buf[101];
			scanf("%s", buf);
			int y; int x;
			scanf("%d%d", &y, &x), -- y, -- x;
			if (*buf == 'x' || *buf == 'o') {
				row[y] = true;
				col[x] = true;
				original[y][x] |= 1;
				++ ans;
			}
			if (*buf == '+' || *buf == 'o') {
				diag1[y + x] = true;
				diag2[y + (N - 1 - x)] = true;
				original[y][x] |= 2;
				++ ans;
			}
		}
		vector<vector<int>> board = original;
		{
			vector<vi> g(N);
			rep(i, N) if(!row[i]) {
				rep(j, N) if (!col[j])
					g[i].push_back(j);
			}
			vector<int> match;
			ans += bipartiteMatching(g, match);
			rep(i, N) if (match[i] != -1)
				board[i][match[i]] |= 1;
		}
		{
			vector<vi> g(N * 2 - 1);
			rep(i, N) rep(j, N) {
				int a = i + j, b = i + (N - 1 - j);
				if (!diag1[a] && !diag2[b])
					g[a].push_back(b);
			}
			vector<int> match;
			ans += bipartiteMatching(g, match);
			rep(i, N) rep(j, N) {
				int a = i + j, b = i + (N - 1 - j);
				if (match[a] == b)
					board[i][j] |= 2;
			}
		}
		vector<pair<int, int>> list;
		rep(i, N) rep(j, N) if (original[i][j] != board[i][j])
			list.emplace_back(i, j);
		printf("Case #%d: ", ii + 1);
		printf("%d %d\n", ans, (int)list.size());
		for (auto p : list)
			printf("%c %d %d\n", ".x+o"[board[p.first][p.second]], p.first + 1, p.second + 1);
	}
	return 0;
}
