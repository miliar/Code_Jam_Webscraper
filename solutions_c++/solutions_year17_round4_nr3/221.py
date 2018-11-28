#include <bits/stdc++.h>

using namespace std;

const int dr[] = {0, -1, 0, 1};
const int dc[] = {1, 0, -1, 0};
const string imp = "IMPOSSIBLE";

const int MAXN = 5010;

char mat[100][100];
bool mark[MAXN];
int r,c;
int comp[MAXN];
vector<int> q[100][100];
pair<int,int> where[MAXN];
vector<int> topol;
vector<int> adj[MAXN], bak[MAXN];

bool go (int i, int j, int d, vector< pair<int,int> > &e) {
	if (i < 0 || i >= r || j < 0 || j >= c)
		return true;
	if (mat[i][j] == '-' || mat[i][j] == '|')
		return false;
	if (mat[i][j] == '.')
		e.push_back(pair<int,int>(i,j));
	if (mat[i][j] == '/')
		d = d^1;
	if (mat[i][j] == '\\')
		d = d^3;
	if (mat[i][j] == '#')
		return true;
	return go(i + dr[d], j + dc[d], d, e);
}

void add_edge(int x, int y) {
	adj[x].push_back(y^1);
	bak[y^1].push_back(x);
	adj[y].push_back(x^1);
	bak[x^1].push_back(y);
}

void add_empty(vector< pair<int,int> > empty, int who) {
	for (int i = 0; i < (int)empty.size(); i++)
		q[empty[i].first][empty[i].second].push_back(who);
}

void dfs (int v) {
	mark[v] = true;
	for (int i = 0; i < (int)adj[v].size(); i++)
		if (!mark[adj[v][i]])
			dfs(adj[v][i]);
	topol.push_back(v);
}

void dfs2(int v, int c) {
	comp[v] = c;
	for (int i = 0; i < (int)bak[v].size(); i++)
		if (comp[bak[v][i]] == -1)
			dfs2(bak[v][i], c);
}

void main2() {
	cin >> r >> c;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			cin >> mat[i][j];
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++)
			q[i][j].clear();
	for (int i = 0; i < MAXN; i++) {
		adj[i].clear();
		bak[i].clear();
	}
	int n = 0;
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) {
			if (mat[i][j] == '-' || mat[i][j] == '|') {
				vector< pair<int,int> > el;
				vector< pair<int,int> > er;
				vector< pair<int,int> > eu;
				vector< pair<int,int> > ed;
				bool ok_r = go(i, j+1, 0, er);
				bool ok_l = go(i, j-1, 2, el);
				bool ok_u = go(i-1, j, 1, eu);
				bool ok_d = go(i+1, j, 3, ed);
				if (ok_l && ok_r) {
					add_empty(el, 2*n);
					add_empty(er, 2*n);
				} else {
					add_edge(2*n+1, 2*n+1);
				}
				if (ok_u && ok_d) {
					add_empty(eu, 2*n+1);
					add_empty(ed, 2*n+1);
				} else {
					add_edge(2*n, 2*n);
				}
				where[n] = pair<int,int>(i,j);
				n++;
			}
		}
	for (int i = 0; i < r; i++)
		for (int j = 0; j < c; j++) if (mat[i][j] == '.') {
			if (q[i][j].empty()) {
				cout << imp << endl;
				return;
			}
			sort(q[i][j].begin(), q[i][j].end());
			q[i][j].resize(unique(q[i][j].begin(), q[i][j].end()) - q[i][j].begin());
			bool ok = false;
			for (int k = 0; k + 1 < (int)q[i][j].size(); k++)
				if (q[i][j][k] == (q[i][j][k+1] ^ 1)) {
					ok = true;
				}
			if (ok == false) {
				assert(q[i][j].size() <= 2);
				if (q[i][j].size() == 1)
					add_edge(q[i][j][0], q[i][j][0]);
				else
					add_edge(q[i][j][0], q[i][j][1]);
			}
		}
	memset(mark, 0, sizeof mark);
	topol.clear();
	for (int i = 0; i < 2*n; i++) if (!mark[i])
		dfs(i);
	memset(comp, -1, sizeof comp);
	int cnt_comp = 0;
	for (int i = (int)topol.size() - 1; i >= 0; i--) if (comp[topol[i]] == -1) {
		dfs2(topol[i], cnt_comp);
		cnt_comp++;
	}
	for (int i = 0; i < n; i++)
		if (comp[2*i] == comp[2*i+1]) {
			cout << imp << endl;
			return;
		} else {
			mat[where[i].first][where[i].second] = (comp[2*i] < comp[2*i+1]) ? ('-') : ('|');
		}
	cout << "POSSIBLE" << endl;
	for (int i = 0; i < r; i++) {
		for (int j = 0; j < c; j++)
			cout << mat[i][j];
		cout << endl;
	}
}

int main() {
	int t; cin >> t;
	for (int o = 1; o <= t; o++) {
		cout << "Case #" << o << ": ";
		main2();
	}
	return 0;
}
