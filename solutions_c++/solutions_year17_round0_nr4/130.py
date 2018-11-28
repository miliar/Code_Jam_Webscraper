#include <vector>
#include <queue>
#include <cstdio>
#include <cassert>
using namespace std;

// in: n, m, graph
// out: match, matched
// vertex cover: (reached[0][left_node] == 0) || (reached[1][right_node] == 1)
struct BipartiteMatching
{
	int n, m;
	vector<vector<int> > graph;
	vector<int> matched, match;
	vector<int> edgeview;
	vector<int> level;
	vector<int> reached[2];
	BipartiteMatching(int n, int m) : n(n), m(m), graph(n), matched(m, -1), match(n, -1) {}

	bool assignLevel()
	{
		bool reachable = false;
		level.assign(n, -1);
		reached[0].assign(n, 0);
		reached[1].assign(m, 0);
		queue<int> q;
		for (int i = 0; i < n; i++) {
			if (match[i] == -1) {
				level[i] = 0;
				reached[0][i] = 1;
				q.push(i);
			}
		}
		while (!q.empty()) {
			auto cur = q.front(); q.pop();
			for (auto adj : graph[cur]) {
				reached[1][adj] = 1;
				auto next = matched[adj];
				if (next == -1) {
					reachable = true;
				}
				else if (level[next] == -1) {
					level[next] = level[cur] + 1;
					reached[0][next] = 1;
					q.push(next);
				}
			}
		}
		return reachable;
	}

	int findpath(int nod) {
		for (int &i = edgeview[nod]; i < graph[nod].size(); i++) {
			int adj = graph[nod][i];
			int next = matched[adj];
			if (next >= 0 && level[next] != level[nod] + 1) continue;
			if (next == -1 || findpath(next)) {
				match[nod] = adj;
				matched[adj] = nod;
				return 1;
			}
		}
		return 0;
	}

	int solve()
	{
		int ans = 0;
		while (assignLevel()) {
			edgeview.assign(n, 0);
			for (int i = 0; i < n; i++)
				if (match[i] == -1)
					ans += findpath(i);
		}
		return ans;
	}
};

char board[111][111];
int N;
struct data{
	char c;
	int x, y;
};

void process(){
	BipartiteMatching PLUS(N, N), CROSS(2 * N - 1, 2 * N - 1);
	vector<bool> R(N), C(N), POS(2 * N - 1), NEG(2 * N - 1);

	for (int i = 0; i < N; i++){
		R[i] = true;
		for (int j = 0; j < N; j++) if (board[i][j] == 'x' || board[i][j] == 'o') R[i] = false;
	}
	for (int i = 0; i < N; i++){
		C[i] = true;
		for (int j = 0; j < N; j++) if (board[j][i] == 'x' || board[j][i] == 'o') C[i] = false;
	}
	for (int i = 0; i < 2 * N - 1; i++){ // i = x-y+(N-1)
		POS[i] = true;
		for (int x = 0; x < N; x++){
			int y = x - i + (N - 1);
			if (0 <= y && y < N){
				if (board[x][y] == '+' || board[x][y] == 'o') POS[i] = false;
			}
		}
	}
	for (int i = 0; i < 2 * N - 1; i++){ // i = x+y
		NEG[i] = true;
		for (int x = 0; x < N; x++){
			int y = i - x;
			if (0 <= y && y < N){
				if (board[x][y] == '+' || board[x][y] == 'o') NEG[i] = false;
			}
		}
	}

	for (int i = 0; i < N; i++) for (int j = 0; j < N; j++)
		if (R[i] && C[j]) PLUS.graph[i].push_back(j);
	for (int i = 0; i < 2 * N - 1; i++)for (int j = 0; j < 2 * N - 1; j++){
		// i=x-y+(N-1), j=x+y
		int x = (i + j - (N - 1)) / 2, y = j - x;
		if ((((i - (N - 1)) + 2 * N) % 2) == (j % 2) && POS[i] && NEG[j] && 0 <= x&&x < N && 0 <= y&&y < N) CROSS.graph[i].push_back(j);
	}

	int p = PLUS.solve();
	int c = CROSS.solve();

	vector<vector<bool>> G1(N, vector<bool>(N)), G2(N, vector<bool>(N));
	for (int i = 0; i < N; i++) if (PLUS.match[i] != -1){
		G1[i][PLUS.match[i]] = true;
	}
	for (int i = 0; i < 2 * N - 1; i++) if (CROSS.match[i] != -1){
		int j = CROSS.match[i]; // x+y=j, x-y+(N-1)=i
		int x = (i - (N - 1) + j) / 2, y = j - x;
		if (0 <= x && x < N && 0 <= y && y < N)
			G2[x][y] = true;
	}

	int diff = 0;
	vector<data> ans;

	for (int i = 0; i < N; i++) for (int j = 0; j < N; j++){
		if (G1[i][j] || G2[i][j]) diff++;
		if (G1[i][j] && G2[i][j]){
			ans.push_back({ 'o', i + 1, j + 1 });
			board[i][j] = 'o';
		}
		else if (G1[i][j]){
			if (board[i][j] == '.')
				ans.push_back({ 'x', i + 1, j + 1 }), board[i][j] = 'x';
			else ans.push_back({ 'o', i + 1, j + 1 }), board[i][j] = 'o';
		}
		else if (G2[i][j]){
			if (board[i][j] == '.')
				ans.push_back({ '+', i + 1, j + 1 }), board[i][j] = '+';
			else ans.push_back({ 'o', i + 1, j + 1 }), board[i][j] = 'o';
		}
	}

	int cost = 0;
	for (int i = 0; i < N; i++)for (int j = 0; j < N; j++){
		if (board[i][j] == 'o') cost += 2;
		else if (board[i][j] != '.') cost++;
	}
	printf("%d %d\n", cost, diff);
	for (auto& d : ans){
		printf("%c %d %d\n", d.c, d.x, d.y);
	}
}

int main(){
	freopen("large.in", "r", stdin);
	freopen("large.out", "w", stdout);

	int T; scanf("%d", &T);
	for (int tc = 1; tc <= T; tc++){
		printf("Case #%d: ", tc);
		int M; scanf("%d%d", &N, &M);
		for (int i = 0; i < N; i++)for (int j = 0; j < N; j++) board[i][j] = '.';

		for (int i = 0; i < M; i++){
			char buff[2]; int x, y;
			scanf("%s%d%d", buff, &x, &y);
			board[x - 1][y - 1] = buff[0];
		}
		process();
	}
}