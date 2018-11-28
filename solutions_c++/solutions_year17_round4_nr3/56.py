#include<bits/stdc++.h>
using namespace std;
const int N(55);
char a[N][N];
const int N2(5555);
vector<int> v[N][N], adj[N2], rev[N2];
int comp[N2], vst[N2];
int dx[4] = {0, 1, 0, -1};
int dy[4] = {1, 0, -1, 0};
vector<int> ord;
void dfs1 (int v) {
	vst[v] = true;
	for(auto to : adj[v]) {
		if (!vst[to])
			dfs1 (to);
	}
	ord.push_back (v);
}

void dfs2 (int v, int cl) {
	comp[v] = cl;
	for(auto to : rev[v])
		if (comp[to] == -1)
			dfs2 (to, cl);
}

int main() {
	int tests;
	scanf("%d", &tests);
	for(int qq(1); qq <= tests; qq++) {
		int n, m;
		scanf("%d%d", &n, &m);
		int cb(0);
		for(int i(0); i < n; i++) {
			scanf("%s", a[i]);
			for(int j(0); j < m; j++)
				v[i][j].clear();
		}
		for(int i(0); i < n; i++) {
			for(int j(0); j < m; j++) {
				if(a[i][j] != '-' && a[i][j] != '|') continue;
				adj[cb * 2].clear();
				adj[cb * 2 + 1].clear();
				rev[cb * 2].clear();
				rev[cb * 2 + 1].clear();
				for(int _(0); _ < 4; _++) {
					int d = _;
					int x(i + dx[_]), y(j + dy[_]);
					bool ok(true);
					while(x >= 0 && x < n && y >= 0 && y < m) {
						if(a[x][y] == '.') {
							//cout << i << ' ' << j << ' ' << x << ' ' << y << ' ' << _ << endl;
							v[x][y].push_back(cb * 2 + _ % 2);
						}else if(a[x][y] == '/') {
							if(d == 0) d = 3; 
							else if(d == 3) d = 0;
							else if(d == 1) d = 2;
							else d = 1;
						}else if(a[x][y] == '\\') {
							d ^= 1;
						}else if(a[x][y] == '#') {
							break;
						}else {
							assert(a[x][y] == '|' || a[x][y] == '-');
							ok = false;
							break;
						}
						x += dx[d];
						y += dy[d];
					}
					if(!ok) adj[cb * 2 + _ % 2].push_back(cb * 2 + (_ + 1) % 2);
				}
				cb++;
			}
		}
		bool flag(true);
		for(int i(0); i < n && flag; i++) {
			for(int j(0); j < m && flag; j++) {
				if(a[i][j] != '.') continue;
				if(v[i][j].empty()) {
					flag = false;
				}else if(v[i][j].size() == 1) {
					adj[v[i][j][0] ^ 1].push_back(v[i][j][0]);
				}else {
					//cout << i << ' ' << j << ' ' << v[i][j][0] << ' ' << v[i][j][1] << endl;
					adj[v[i][j][0] ^ 1].push_back(v[i][j][1]);
					adj[v[i][j][1] ^ 1].push_back(v[i][j][0]);
				}
			}
		}
		ord.clear();
		fill(comp, comp + cb * 2, -1);
		fill(vst, vst + cb * 2, 0);
		for(int i(0); i < cb * 2; i++)
			for(int j : adj[i]){
				//printf("%d->%d\n", i, j);
				rev[j].push_back(i);
			}
		for(int i(0); i < cb * 2; i++)
			if(!vst[i])
				dfs1(i);
		for (int i(0), j(0); i < cb * 2; i++) {
			int v = ord[cb * 2 - i - 1];
			if (comp[v] == -1)
				dfs2 (v, j++);
		}
		for(int i(0); i < cb * 2; i++)
			if(comp[i] == comp[i ^ 1]) {
				flag = false;
				break;
			}
		printf("Case #%d: ", qq);
		if(flag) {
			printf("POSSIBLE\n");
			int cur(0);
			for(int i(0); i < n; i++) {
				for(int j(0); j < m; j++) {
					if(a[i][j] == '|' || a[i][j] == '-') {
						if(comp[cur * 2] > comp[cur * 2 + 1])
							a[i][j] = '-';
						else
							a[i][j] = '|';
						cur++;
					}
					printf("%c", a[i][j]);
				}
				printf("\n");
			}
		}else {
			printf("IMPOSSIBLE\n");
		}
	}

}
