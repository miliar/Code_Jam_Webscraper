#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <stack>
#include <queue>
#include <set>
#include <map>
using namespace std;
typedef long long i64; typedef vector<int> ivec; typedef vector<string> svec;
const i64 MOD = 0;
template <typename T> void ADD(T &a, const T b) { a = (a + b) % MOD; }
int Tca;

int H, W, M;
char in[110][110];
int id[110][110]; int whosees[110][110];

int killable[1024][10];
vector<pair<int, int> > S, T;

int dy[] = { -1,0,1,0 }, dx[] = { 0,-1,0,1 };
bool vis[110][110];
int dp[1 << 10][1 << 10];
pair<int, int> fro[1 << 10][1 << 10];

int main()
{
	scanf("%d", &Tca);
	for (int ttt = 0; ttt++ < Tca;) {
		scanf("%d%d%d", &W, &H, &M);
		for (int i = 0; i < H; ++i) {
			scanf("%s", in[i]);
		}
		S.clear(); T.clear();
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) {
				if (in[i][j] == 'S') {
					id[i][j] = S.size();
					S.push_back({ i, j });
				}
				if (in[i][j] == 'T') {
					id[i][j] = T.size();
					T.push_back({ i, j });
				}
				whosees[i][j] = 0;
			}
		}
		for (int i = 0; i < H; ++i) {
			for (int j = 0; j < W; ++j) if (in[i][j] == 'T') {
				for (int d = 0; d < 4; ++d) {
					int y = i, x = j;
					for (;y >= 0 && y < H && x >= 0 && x < W; y += dy[d], x += dx[d]) {
						if (in[y][x] == '#') break;
						whosees[y][x] |= 1 << id[i][j];
					}
				}
			}
		}

		for (int m = 0; m < (1 << T.size()); ++m) {
			// m: alive
			for (int i = 0; i < S.size(); ++i) {
				killable[m][i] = 0;
				for (int i = 0; i < H; ++i) {
					for (int j = 0; j < W; ++j) {
						vis[i][j] = false;
					}
				}

				queue<pair<int, pair<int, int> > > Q;
				Q.push({ M, S[i] });
				while (!Q.empty()) {
					int dist = Q.front().first;
					auto loc = Q.front().second;
					Q.pop();
					//printf("%d %d, %d %d %d\n", m, i, dist, loc.first, loc.second);
					if (vis[loc.first][loc.second]) continue;
					vis[loc.first][loc.second] = true;
					if (m & whosees[loc.first][loc.second]) {
						killable[m][i] |= whosees[loc.first][loc.second] & m;
						continue;
					}
					if (dist == 0) continue;

					for (int d = 0; d < 4; ++d) {
						int y = loc.first + dy[d], x = loc.second + dx[d];
						if (y >= 0 && y < H && x >= 0 && x < W && in[y][x] != '#') {
							Q.push({ dist - 1, {y, x} });
						}
					}
				}
			}
		}
	//	printf("%d\n", killable[(1 << T.size()) - 1][0]);
		for (int i = 0; i < (1 << S.size()); ++i) {
			for (int j = 0; j < (1 << T.size()); ++j) {
				dp[i][j] = 0;
				for (int k = 0; k < S.size(); ++k) if (i & (1 << k)) {
					for (int l = 0; l < T.size(); ++l) if (killable[j][k] & (1 << l)) {
						int dp2 = dp[i ^ (1 << k)][j ^ (1 << l)] + 1;
						if (dp[i][j] < dp2) {
							dp[i][j] = dp2;
							fro[i][j] = make_pair(k, l);
						}
					}
				}
			}
		}

		printf("Case #%d: %d\n", ttt, dp[(1 << S.size()) - 1][(1 << T.size()) - 1]);
		vector<pair<int, int> > seq;
		int s = (1 << S.size()) - 1, t = (1 << T.size()) - 1;
		while (dp[s][t] > 0) {
			seq.push_back(fro[s][t]);
			auto f = fro[s][t];
			s ^= 1 << f.first;
			t ^= 1 << f.second;
		}
		for (auto a : seq) printf("%d %d\n", a.first + 1, a.second + 1);
	}

	return 0;
}
