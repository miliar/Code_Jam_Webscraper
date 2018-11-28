#define HEADER_H
#define _GLIBCXX_DEBUG
#include <bits/stdc++.h>
using namespace std;
using ull          = unsigned long long;
using ll           = long long;
using ld           = long double;
using vi           = vector<ll>;
using vvi          = vector<vi>;
using vb           = vector<bool>;
using ii           = pair<int, int>;
constexpr bool LOG = false;
void Log() {
	if(LOG) cerr << "\n";
}
template <class T, class... S>
void Log(T t, S... s) {
	if(LOG) cerr << t << "\t", Log(s...);
} /* ============== END OF HEADER ============== */

struct Tarjan {
	vvi &edges;
	int V, counter = 0, C = 0;
	vi n, l;
	vb vs;
	stack<int> st;

	Tarjan(vvi &e) : edges(e), V(e.size()), n(V, -1), l(V, -1), vs(V, false) {}

	void visit(int u, vi &com) {
		l[u] = n[u] = counter++;
		st.push(u);
		vs[u] = true;
		for(auto &&v : edges[u]) {
			if(n[v] == -1) visit(v, com);
			if(vs[v]) l[u] = min(l[u], l[v]);
		}
		if(l[u] == n[u]) {
			while(true) {
				int v = st.top();
				st.pop();
				vs[v]  = false;
				com[v] = C; //<== ACT HERE
				if(u == v) break;
			}
			C++;
		}
	}

	int find_sccs(vi &com) { // component indices will be stored in 'com'
		com.assign(V, -1);
		C = 0;
		for(int u = 0; u < V; ++u)
			if(n[u] == -1) visit(u, com);
		return C;
	}

	// scc is a map of the original vertices of the graph
	// to the vertices of the SCC graph, scc_graph is its
	// adjacency list.
	// Scc indices and edges are stored in 'scc' and 'scc_graph'.
	void scc_collapse(vi &scc, vvi &scc_graph) {
		find_sccs(scc);
		scc_graph.assign(C, vi());
		set<ii> rec; // recorded edges
		for(int u = 0; u < V; ++u) {
			assert(scc[u] != -1);
			for(int v : edges[u]) {
				if(scc[v] == scc[u] || rec.find({scc[u], scc[v]}) != rec.end()) continue;
				scc_graph[scc[u]].push_back(scc[v]);
				rec.insert({scc[u], scc[v]});
			}
		}
	}
};
struct TwoSAT {
	int n;
	vvi imp; // implication graph
	Tarjan tj;

	TwoSAT(int _n) : n(_n), imp(2 * _n, vi()), tj(imp) {}

	// Only copy the needed functions:
	void add_implies(int c1, bool v1, int c2, bool v2) {
		int u = 2 * c1 + (v1 ? 1 : 0), v = 2 * c2 + (v2 ? 1 : 0);
		imp[u].push_back(v);         //  u =>  v
		imp[v ^ 1].push_back(u ^ 1); // -v => -u
	}
	void add_equivalence(int c1, bool v1, int c2, bool v2) {
		add_implies(c1, v1, c2, v2);
		add_implies(c2, v2, c1, v1);
	}
	void add_or(int c1, bool v1, int c2, bool v2) { add_implies(c1, !v1, c2, v2); }
	void add_and(int c1, bool v1, int c2, bool v2) {
		add_true(c1, v1);
		add_true(c2, v2);
	}
	void add_xor(int c1, bool v1, int c2, bool v2) {
		add_or(c1, v1, c2, v2);
		add_or(c1, !v1, c2, !v2);
	}
	void add_true(int c1, bool v1) { add_implies(c1, !v1, c1, v1); }

	// on true: a contains an assignment.
	// on false: no assignment exists.
	bool solve(vb &a) {
		vi com;
		tj.find_sccs(com);
		for(int i = 0; i < n; ++i)
			if(com[2 * i] == com[2 * i + 1]) return false;

		vvi bycom(com.size());
		for(int i = 0; i < 2 * n; ++i) bycom[com[i]].push_back(i);

		a.assign(n, false);
		vb vis(n, false);
		for(auto &&component : bycom) {
			for(int u : component) {
				if(vis[u / 2]) continue;
				vis[u / 2] = true;
				a[u / 2]   = (u % 2 == 1);
			}
		}
		return true;
	}
};

// - true
// | false
array<array<char, 50>, 50> board;
// cover[i][j][0]: laser index covering the cell horizontally
// cover[i][j][1]: laser index covering the cell vertically
array<array<array<pair<int, bool>, 2>, 50>, 50> cover;

array<int, 4> dr{{0, -1, 0, 1}};
array<int, 4> dc{{1, 0, -1, 0}};
int R, C;

// horizontal dir:
int orientation(int dir) {
	return (dir == 1 || dir == 3) ? 1 : 0;
}

struct P {
	// currently in r,c with direction dir
	int r, c, dir;

	// true if it lands in a valid cell
	bool advance() {
		Log("adv: ", r, c, dir, board[r][c]);
		if(board[r][c] == '\\') {
			dir = 3 - dir;
		}
		if(board[r][c] == '/') {
			dir ^= 1;
		}

		r += dr[dir];
		c += dc[dir];
		Log("to: ", r, c, dir);
		if(r < 0 || r >= R || c < 0 || c >= C) return false;
		if(board[r][c] == '#') return false;
		return true;
	}
};

// return true on success, false on collision with other laser
// p starts at the position of the laser
bool trace(P p, int laserid, int laserorientation) {
	Log("trace:", p.r, p.c, p.dir, laserid, laserorientation);
	while(p.advance()) {
		Log("p: ", p.r, p.c, p.dir);
		if(board[p.r][p.c] == '.') {
			int o = orientation(p.dir);
			/* // Premature optimization?
			if(cover[p.r][p.c][o] != -1) {
			    // this laser will hit another laser in this direction
			    return false;
			}
			*/
			cover[p.r][p.c][o] = {laserid, laserorientation};
		}
		if(board[p.r][p.c] == '-' || board[p.r][p.c] == '|') {
			// direct hit to other laser
			return false;
		}
	}
	return true;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);

	int T;
	cin >> T;
	for(int tc = 1; tc <= T; ++tc) {
		cout << "Case #" << tc << ": ";

		cin >> R >> C;
		for(auto &x : cover)
			for(auto &y : x) y.fill({-1, false});

		vector<ii> lasers;

		for(int r = 0; r < R; ++r) {
			for(int c = 0; c < C; ++c) {
				cin >> board[r][c];
				if(board[r][c] == '-' || board[r][c] == '|') lasers.push_back({r, c});
			}
		}

		TwoSAT ts(lasers.size());
		vb solution;

		Log("prevent laser collisions");

		// trace all laser paths
		for(int i = 0; i < lasers.size(); ++i) {
			auto &laser = lasers[i];
			for(int dir = 0; dir < 4; ++dir) {
				if(!trace(P{laser.first, laser.second, dir}, i, orientation(dir))) {
					// if the laser hits another laser, the other orientation must be true
					ts.add_true(i, !orientation(dir));
				}
			}
		}

		Log("cover all cells");

		// now make sure every cell is covered
		for(int r = 0; r < R; ++r) {
			for(int c = 0; c < C; ++c) {
				if(board[r][c] == '.') {
					// one of the two directions (if provided) must be true
					if(cover[r][c][0].first == -1 && cover[r][c][1].first == -1) {
						cout << "IMPOSSIBLE" << endl;
						goto end;
					}
					for(int i = 0; i <= 1; ++i) {
						if(cover[r][c][i].first == -1) {
							// the other one MUST be true
							ts.add_true(cover[r][c][1 - i].first, cover[r][c][1 - i].second);
							goto thisend;
						}
					}
					assert(cover[r][c][0].first != -1);
					assert(cover[r][c][1].first != -1);
					// both are valid, add OR
					ts.add_or(cover[r][c][0].first, cover[r][c][0].second, cover[r][c][1].first,
					          cover[r][c][1].second);
				thisend:;
				}
			}
		}

		Log("solve");

		if(ts.solve(solution)) {
			cout << "POSSIBLE" << endl;
			int i = 0;
			for(int r = 0; r < R; ++r) {
				for(int c = 0; c < C; ++c) {
					if(board[r][c] == '-' || board[r][c] == '|') {
						if(solution[i])
							cout << '|';
						else
							cout << '-';
						++i;
					} else {
						cout << board[r][c];
					}
				}
				cout << '\n';
			}
			cout.flush();
		} else {
			cout << "IMPOSSIBLE" << endl;
		}
	end:;
	}

	return 0;
}
