#include <bits/stdc++.h>

using namespace std;

const int N = 211;
char buf[] = ".x+o";
int n, m;
vector<pair<int,int>> O, X;
char Map[N][N];
int row[N], col[N], mark[N][N];
int ans = 0;
void solveO() {
	memset(row, 0, sizeof row);
	memset(col, 0, sizeof col);
	for (auto x: O) {
		mark[x.first][x.second] |= 1;
		row[x.first] = true;
		col[x.second] = true;
	}
	vector<int> remrow, remcol;
	for (int i = 1; i <= n; ++i) if (!row[i]) remrow.push_back(i);
	for (int i = 1; i <= n; ++i) if (!col[i]) remcol.push_back(i);
	while (remrow.size()) {
		++ans;
		int x = remrow.back();
		int y = remcol.back();
		mark[x][y] |= 1;
		remrow.pop_back();
		remcol.pop_back();
	}
}

namespace HK {
	const int N = 65536, inf = 0x3fffffff;
	int n,m,x,y,match[N*2],dist[N*2], p;
	vector<int> e[N];
	queue<int> q;
	bool bfs() {
		dist[0]=inf;
		for (int i=1;i<=n;i++)
			if (match[i]==0) dist[i]=0,q.push(i);
			else dist[i]=inf;
		while (!q.empty()) {
			int now=q.front();
			q.pop();
			for (auto i: e[now])
				if (dist[match[i]]==inf)
					dist[match[i]]=dist[now]+1,q.push(match[i]);
		}
		return dist[0]!=inf;
	}
	bool dfs(int x) {
		if (x==0) return true;
		for (auto i: e[x])
			if (dist[x]+1==dist[match[i]]) {
				if (dfs(match[i])) {
					match[x]=i;
					match[i]=x;
					return true;
				}
				else dist[match[i]]=inf;
			}
		return false;
	}
	int Hopcroft_Karp() {
		int ans=0;
		memset(match,0,sizeof(match));
		while (bfs()) {
			for (int i=1;i<=n;i++)
				if (dist[i]==0)
					if (dfs(i)) ans++;
		}
		return ans;
	}
	void add_edge(int x, int y) {
		e[x].push_back(y + n);
	}
	void init(int tn, int tm) {
		n = tn; m = tm;
		for (int i = 1; i <= n; ++i) e[i].clear();
	}
};

int occupy[N][N];
void solveX() {
	memset(occupy, 0, sizeof occupy);
	for (auto x: X) {
		mark[x.first][x.second] |= 2;
		for (int ti = -n; ti <= n; ++ti) {
			if (1 <= x.first + ti && x.first + ti <= n && 1 <= x.second + ti && x.second + ti <= n) {
				occupy[x.first + ti][x.second + ti] = true;
			}
			if (1 <= x.first + ti && x.first + ti <= n && 1 <= x.second - ti && x.second - ti <= n) {
				occupy[x.first + ti][x.second - ti] = true;
			}
		}
	}
	HK::init(n + n - 1, n + n - 1);
	for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) if (!occupy[i][j]) {
		HK::add_edge(i + j - 1, i + n - j);
	}
	ans += HK::Hopcroft_Karp();
	for (int i = 1; i <= n + n - 1; ++i) if (HK::match[i]) {
		int tx = i + 1, ty = HK::match[i] - n - (n + n - 1);
		int y =  (tx - ty) / 2;
		int x = tx - y;
		assert(1 <= x && x <= n && 1 <= y && y <= n);
		mark[x][y] |= 2;
	}
}

int main() {
	int T; cin >> T;
	for (int TK = 1; TK <= T; ++TK) {
		cin >> n >> m;
		O.clear();
		X.clear();
		for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) Map[i][j] = '.';
		for (int i = 0; i < m; ++i) {
			char c;
			int x, y;
			scanf(" %c %d %d", &c, &x, &y);
			if (c == '+' || c == 'o') {
				X.emplace_back(x, y);
			}
			if (c == 'x' || c == 'o') {
				O.emplace_back(x, y);
			}
			Map[x][y] = c;
		}
		memset(mark, 0, sizeof mark);
		solveO();
		solveX();
		vector<pair<int,int>> out;
		for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) if (Map[i][j] != buf[mark[i][j]]) {
			out.emplace_back(i, j);
		}
		int total_score = 0;
		for (int i = 1; i <= n; ++i) for (int j = 1; j <= n; ++j) {
			total_score += mark[i][j] >= 1;
			total_score += mark[i][j] == 3;	
		}
		for (int i = 1; i <= n; ++i) {
			for (int x = 1; x <= n; ++x) for (int y = 1; y <= n; ++y) if (x != y) {
				if (mark[i][x] && mark[i][y]) assert(mark[i][x] == 2 || mark[i][y] == 2);
				if (mark[x][i] && mark[y][i]) assert(mark[x][i] == 2 || mark[y][i] == 2);
			}
		}
		
		printf("Case #%d: %d %d\n", TK, total_score, out.size());
		for (auto x: out) {
			printf("%c %d %d\n", buf[mark[x.first][x.second]], x.first, x.second);
		}
	}
	return 0;
}