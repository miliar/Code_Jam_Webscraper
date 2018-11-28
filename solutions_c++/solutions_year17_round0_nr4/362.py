#include <bits/stdc++.h>
using namespace std;

struct node {
	char c;
	int y, x;
};

const int MAX = 205;
int tc, N, M, Pair[2][MAX];
char bef[MAX][MAX];
bool ori[2][MAX], V[MAX];
vector<int> adj[2][MAX];

bool dfs(int cur, int P[], vector<int> adj[]) {
	if (V[cur]) return false;
	V[cur] = true;

	for (int next : adj[cur]) {
		if (P[next] == 0 || dfs(P[next], P, adj)) {
			P[next] = cur;
			return true;
		}
	}

	return false;
}

int main() {
	scanf("%d", &tc);
	for (int tt=1; tt<=tc; ++tt) {
		scanf("%d%d", &N, &M);

		memset(adj, 0, sizeof(adj));
		for (int y=1; y<=N; ++y) for (int x=1; x<=N; ++x) {
			adj[0][y].push_back(x);
			adj[1][y+x-1].push_back(y-x+N);
		}

		memset(bef, 0, sizeof(bef));
		memset(ori, 0, sizeof(ori));
		memset(Pair, 0, sizeof(Pair));
		int ans = 0;
		for (int i=0; i<M; ++i) {
			char c;
			int y, x;
			scanf(" %c%d%d", &c, &y, &x);
			bef[y][x] = c;
			if (c != '+') {
				ori[0][y] = true;
				Pair[0][x] = y;
				++ans;
			}
			if (c != 'x') {
				ori[1][y+x-1] = true;
				Pair[1][y-x+N] = y+x-1;
				++ans;
			}
		}

		for (int i=1; i<=N; ++i) {
			memcpy(V, ori[0], sizeof(V));
			if (dfs(i, Pair[0], adj[0])) ++ans;
		}

		for (int i=1; i<=2*N-1; ++i) {
			memcpy(V, ori[1], sizeof(V));
			if (dfs(i, Pair[1], adj[1])) ++ans;
		}

		vector<node> lis;
		for (int i=1; i<=N; ++i) for (int j=1; j<=N; ++j) {
			char cur = '\0';
			if (Pair[0][j] == i) cur = 'x';
			if (Pair[1][i-j+N] == i+j-1) cur = cur ? 'o' : '+';

			if (cur != bef[i][j])
				lis.push_back({cur, i, j});
		}

		printf("Case #%d: ", tt);
		printf("%d %d\n", ans, lis.size());
		for (int i=0; i<lis.size(); ++i)
			printf("%c %d %d\n", lis[i].c, lis[i].y, lis[i].x);

	}
	return 0;
}





