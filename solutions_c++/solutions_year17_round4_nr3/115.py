#include <bits/stdc++.h>
using namespace std;
#define fo(i,a,b) for(int i=(a);i<(b);i++)
#define MOD 1000000007
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef long double ld;
#define PI ((ld)acos(-1.))
#define asdf(x...) fprintf(stderr, x)

namespace sat {
	int N, M, C, G, id[5500], lo[5500], g[5500], root[5500];
	vector<int> adj[5500], se[5500], in[5500], sc;
	bool tops[5500];
	int res[5500];
	stack<int> s;

	void clear () {
		N = M = C = G = 0;

		sc.clear();
		while (s.size()) s.pop();
		
		fo(i, 0, 5500) {
			id[i] = lo[i] = g[i] = root[i] = 0;
			adj[i].clear(), se[i].clear(), in[i].clear();
			tops[i] = false;
			res[i] = 0;
		}
	}

	int gt (int i, bool x) { return i + N*x; }
	int ac (int i) { return i - N * (i>=N); }

	void scc (int i) {
		id[i] = lo[i] = ++C, s.push(i);
		for (int j : adj[i]) {
			if (!id[j]) scc(j);
			if (!g[j] && lo[j] < lo[i]) lo[i] = lo[j];
		}
		if (lo[i] == id[i]) {
			G++;
			while (s.top() != i) g[s.top()] = G, s.pop();
			root[G] = i, g[i] = G, s.pop();
		}
	}

	void top (int i) {
		tops[i] = 1;
		for (int j : se[i]) if (!tops[j]) top(j);
		sc.PB(i);
	}

	void ass (int i) {
		res[ac(i)] = (i<N) ? 1 : 2;
		for (int j : in[i]) if (!res[ac(j)]) ass(j);
	}

	void edge (int a, int x, int b, int y) {
		adj[gt(a, !x)].PB(gt(b, y));
		adj[gt(b, !y)].PB(gt(a, x));
	}

	bool run () {
		fo(i, 0, 2*N) if (!id[i]) scc(i);
		fo(i, 0, N) if (g[i] == g[i+N]) return false;
		fo(i, 0, 2*N) for (int j : adj[i]) {
			if (g[i] == g[j]) in[i].PB(j);
			else se[g[i]].PB(g[j]);
		}
		fo(i, 1, G+1) if (!tops[i]) top(i);
		for (int i : sc) if (!res[ac(root[i])]) ass(root[i]);
		//res stores the result of all the guns
		return true;
	}
}

int T, R, C;
char g[55][55];
vector<pair<int,bool>> pass[55][55];

int id (vector<pair<int,int>>& v, int i, int j) {
	return int(lower_bound(v.begin(), v.end(), MP(i,j)) - v.begin());
}

bool in (int i, int j) {
	return i>=0 && j>=0 && i<R && j<C && g[i][j]!='#';
}

int dr[] = {-1, 0, 1, 0};
int dc[] = {0, 1, 0, -1};

bool ok (int i, int j, int d) {
	i += dr[d], j += dc[d];
	if (in(i,j)) {
		if (g[i][j] == '/') {
			d ^= 1;
		} else if (g[i][j] == '\\') {
			d = 3-d;
		}
		if (g[i][j] == '-') return false;
		return ok(i, j, d);
	} else return true;
}

void mark (int i, int j, int d, int z, bool b) {
	i += dr[d], j += dc[d];
	if (in(i,j)) {
		if (g[i][j] == '/') {
			d ^= 1;
		} else if (g[i][j] == '\\') {
			d = 3-d;
		}
		if (g[i][j] == '.') {
			pass[i][j].PB(MP(z,b));
		}
		assert(g[i][j] != '-');
		return mark(i, j, d, z, b);
	}
}

int main () {
	scanf("%d", &T);
	fo(t, 1, T+1) {
		//REMEMBER CLEAR DS
		sat::clear();
		fo(i, 0, 55) fo(j, 0, 55) pass[i][j].clear();
		//REMEMBER CLEAR DS
		asdf("Doing case %d... ", t);
		printf("Case #%d: ", t);

		vector<pair<int, int>> guns, cells;
		scanf("%d %d", &R, &C);
		fo(i, 0, R) {
			scanf(" %s", g[i]);
			fo(j, 0, C) {
				if (g[i][j] == '|' || g[i][j] == '-') {
					g[i][j] = '-';
					guns.PB(MP(i, j));
				}
				if (g[i][j] == '.') {
					cells.PB(MP(i, j));
				}
			}
		}
		sort(guns.begin(), guns.end());
		sort(cells.begin(), cells.end());

		sat::N = (int) guns.size();

		fo(z, 0, (int) guns.size()) {
			int i, j; tie(i,j) = guns[z];
			bool v = false, h = false;
			if (ok(i,j,0)&&ok(i,j,2)) v = true;
			if (ok(i,j,1)&&ok(i,j,3)) h = true;
			if (!v && !h) {
				puts("IMPOSSIBLE");
				asdf("printing impossible as both suicide");
				goto skip;
			}
			if (!h) sat::edge(z, true, z, true);//vertical = true
			if (!v) sat::edge(z, false, z, false);//must be horiz(false)

			asdf("gun %d can do %d %d\n", z, h, v);

			if (v) {
				mark(i,j,0,z,true);
				mark(i,j,2,z,true);
			}
			if (h) {
				mark(i,j,1,z,false);
				mark(i,j,3,z,false);
			}
		}

		for (auto k : cells) {
			int i, j; tie(i,j) = k;
			assert((int) pass[i][j].size() <= 2);
		}

		for (auto k : cells) {
			int i, j; tie(i,j) = k;
			if (pass[i][j].empty()) {
				puts("IMPOSSIBLE");
				asdf("printing impossible as cell unfufillable");
				goto skip;
			}
			if ((int) pass[i][j].size() == 1) {
				int a; bool x; tie(a,x) = pass[i][j][0];
				sat::edge(a,x,a,x);
			} else if ((int) pass[i][j].size() == 2) {
				int a,b; bool x,y;
				tie(a,x) = pass[i][j][0];
				tie(b,y) = pass[i][j][1];
				sat::edge(a,x,b,y);
			}
		}

		if (!sat::run()) {
			puts("IMPOSSIBLE");
			asdf("printing impossible as run failed\n");
			goto skip;
		}

		fo(i, 0, (int) guns.size()) {
			int r, c; tie(r,c) = guns[i];
			if (sat::res[i] == 2) {
				g[r][c] = '|';
			} else if (sat::res[i] == 1) {
				assert(g[r][c] == '-');
			} else assert(0);
		}

		puts("POSSIBLE");
		fo(i, 0, R) {
			fo(j, 0, C) printf("%c", g[i][j]);
			puts("");
		}

skip:;
		asdf("\n");
	}
	return 0;
}
