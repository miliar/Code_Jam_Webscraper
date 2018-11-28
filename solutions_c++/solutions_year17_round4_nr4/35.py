#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int W; int H; int D;
		scanf("%d%d%d", &W, &H, &D);
		vector<string> field(H);
		rep(i, H) {
			char buf[101];
			scanf("%s", buf);
			field[i] = buf;
		}
		vector<int> posS, posC;
		rep(i, H) rep(j, W) {
			if (field[i][j] == 'S')
				posS.push_back(i * W + j);
			if (field[i][j] == 'T')
				posC.push_back(i * W + j);
		}
		int S = (int)posS.size(), C = (int)posC.size();
		vector<vector<int>> ranges(C);
		rep(c, C) {
			int i = posC[c] / W, j = posC[c] % W;
			ranges[c].push_back(i * W + j);
			for (int y = i + 1; y < H && field[y][j] != '#'; ++ y)
				ranges[c].push_back(y * W + j);
			for (int y = i - 1; y >= 0 && field[y][j] != '#'; -- y)
				ranges[c].push_back(y * W + j);
			for (int x = j + 1; x < W && field[i][x] != '#'; ++ x)
				ranges[c].push_back(i * W + x);
			for (int x = j - 1; x >= 0 && field[i][x] != '#'; -- x)
				ranges[c].push_back(i * W + x);
		}
		vector<vector<vector<bool>>> possible(S, vector<vector<bool>>(C, vector<bool>(1 << C)));
		rep(s, S) rep(c, C) rep(setC, 1 << C) if(~setC >> c & 1) {
			vector<bool> inrange(H * W);
			rep(c, C) if (~setC >> c & 1)
				for (int u : ranges[c])
					inrange[u] = true;
			vector<bool> goal(H * W);
			for (int u : ranges[c])
				goal[u] = true;
			vi q, nq;
			vector<bool> vis(H * W);
			nq.push_back(posS[s]);
			vis[nq[0]] = true;
			bool ok = false;
			rep(k, D + 1) {
				q.swap(nq);
				nq.clear();
				for (int u : q) {
					if (goal[u]) {
						ok = true;
						break;
					}
					if (inrange[u])
						continue;
					int i = u / W, j = u % W;
					static const int dy[4] = { 0, 1, 0, -1 }, dx[4] = { 1, 0, -1, 0 };
					for (int d = 0; d < 4; ++ d) {
						int yy = i + dy[d], xx = j + dx[d];
						if (yy < 0 || yy >= H || xx < 0 || xx >= W) continue;
						if (field[yy][xx] == '#') continue;
						int v = yy * W + xx;
						if (vis[v]) continue;
						vis[v] = true;
						nq.push_back(v);
					}
				}
				if (ok) break;
			}
			possible[s][c][setC] = ok;
		}
		vector<pii> dp(1 << (S + C), make_pair(-1, -1));
		dp[0] = { 0, -1 };
		rep(setS, 1 << S) rep(setC, 1 << C) {
			int x = dp[setS << C | setC].first;
			if (x == -1) continue;
			rep(s, S) if(~setS >> s & 1) rep(c, C) if(~setC >> c & 1) {
				if(possible[s][c][setC])
					amax(dp[(setS | 1 << s) << C | (setC | 1 << c)], make_pair(x + 1, setS << C | setC));
			}
		}
		int ans = max_element(dp.begin(), dp.end())->first;
		printf("Case #%d: %d\n", ii + 1, ans);
		vpii moves;
		for (int setSC = (int)(max_element(dp.begin(), dp.end()) - dp.begin()); ; setSC = dp[setSC].second) {
			int psetSC = dp[setSC].second;
			if (psetSC == -1) break;
			int setS = setSC >> C, setC = setSC & ((1 << C) - 1);
			int psetS = psetSC >> C, psetC = psetSC & ((1 << C) - 1);
			rep(s, S) rep(c, C) {
				if (((setS ^ psetS) >> s & 1) && ((setC ^ psetC) >> c & 1)) {
					moves.emplace_back(s, c);
				}
			}
		}
		reverse(moves.begin(), moves.end());
		for (int i = 0; i < (int)moves.size(); ++ i)
			printf("%d %d\n", moves[i].first + 1, moves[i].second + 1);
	}
	return 0;
}
