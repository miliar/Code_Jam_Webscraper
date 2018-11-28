#include "bits/stdc++.h"
using namespace std;
#define rep(i,n) for(int (i)=0;(i)<(int)(n);++(i))
#define rer(i,l,u) for(int (i)=(int)(l);(i)<=(int)(u);++(i))
#define reu(i,l,u) for(int (i)=(int)(l);(i)<(int)(u);++(i))
static const int INF = 0x3f3f3f3f; static const long long INFL = 0x3f3f3f3f3f3f3f3fLL;
typedef vector<int> vi; typedef pair<int, int> pii; typedef vector<pair<int, int> > vpii; typedef long long ll;
template<typename T, typename U> static void amin(T &x, U y) { if (y < x) x = y; }
template<typename T, typename U> static void amax(T &x, U y) { if (x < y) x = y; }

struct StaticGraph {
	typedef int Arc;
	typedef pair<int, Arc> Edge;

	struct ArcList {
		ArcList() : arcBegin(), arcEnd() {}
		ArcList(const Arc *arcBegin, const Arc *arcEnd) : arcBegin(arcBegin), arcEnd(arcEnd) {}

		const Arc *begin() const { return arcBegin; }
		const Arc *end() const { return arcEnd; }
		int size() const { return (int)(arcEnd - arcBegin); }
		bool empty() const { return arcBegin == arcEnd; }
		Arc operator[](int i) const { return arcBegin[i]; }

	private:
		const Arc * const arcBegin, * const arcEnd;
	};

	int size() const { return (int)offsets.size() - 1; }

	ArcList operator[](int i) const {
		return ArcList(arcs.data() + offsets[i], arcs.data() + offsets[i + 1]);
	}

	void init(int n, const vector<Edge> &edges) {
		int m = (int)edges.size();
		arcs.resize(m + 1);
		offsets.assign(n + 1, 0);
		for (int ei = 0; ei < m; ++ ei)
			++ offsets[edges[ei].first];
		for (int i = 0; i < n; ++ i)
			offsets[i + 1] += offsets[i];
		for (int ei = m - 1; ei >= 0; -- ei)
			arcs[-- offsets[edges[ei].first]] = edges[ei].second;
	}


	vector<Arc> arcs;
	vector<int> offsets;
};

class StronglyConnectedComponents {
public:
	//typedef vector<vector<int>> Graph;
	typedef StaticGraph Graph;

	int run(const Graph &graph) {
		int n = (int)graph.size();
		stack.resize(n);
		S.resize(n);
		B.resize(n);
		I.assign(n, 0);
		int sp = 0, topS = 0, topB = 0, c = n;
		for (int start = 0; start < n; ++ start) if (I[start] == 0) {
			stack[sp ++] = make_pair(start, 0);
			for (; sp != 0; ) {
				int u, ei;
				tie(u, ei) = stack[-- sp];
				if (ei == 0) {
					S[topS ++] = u;
					B[topB ++] = I[u] = topS;
				}
				if (ei != graph[u].size()) {
					stack[sp ++] = make_pair(u, ei + 1);
					int v = graph[u][ei];
					if (I[v] == 0) {
						stack[sp ++] = make_pair(v, 0);
					} else {
						while (I[v] < B[topB - 1])
							-- topB;
					}
				} else if (I[u] == B[topB - 1]) {
					-- topB, ++ c;
					while (I[u] <= topS)
						I[S[-- topS]] = c;
				}
			}
		}
		for (int u = 0; u < n; ++ u)
			I[u] -= n + 1;
		return c - n;
	}

	int getColor(int u) const {
		return I[u];
	}

private:
	vector<pair<int, int>> stack;
	vector<int> S, B, I;
};

class TwoSatisfiability {
public:
	void init(int variables) {
		variableID.assign(variables, -1);
	}

	bool run(const vector<pair<int, int>> &clauses) {
		currentVariables.clear();
		edges.clear();
		for (const auto &clause : clauses) {
			int u = getVertex(clause.first);
			int v = getVertex(clause.second);
			edges.emplace_back(u ^ 1, v);
			edges.emplace_back(v ^ 1, u);
		}
		int n = (int)currentVariables.size();
		for (int var : currentVariables)
			variableID[var] = -1;

		graph.init(n * 2, edges);
		scc.run(graph);
		bool satisfiable = true;
		for (int i = 0; i < n; ++i)
			satisfiable &= scc.getColor(i * 2) != scc.getColor(i * 2 + 1);
		return satisfiable;
	}

	void getAssignment(vector<bool> &res) {
		int n = graph.size();
		makeCondensation();
		int S = condensation.size();
		vector<int> deg(S);
		rep(i, S) for (int j : condensation[i])
			deg[j] ++;
		vector<int> que(S, -1);
		int qt = 0;
		rep(i, S) if (deg[i] == 0)
			que[qt++] = i;
		for (int qh = 0; qh < qt; ++qh) {
			int i = que[qh];
			for (int j : condensation[i])
				if (--deg[j] == 0)
					que[qt++] = j;
		}
		vector<int> index(S, -1);
		rep(i, S)
			index[que[i]] = i;
		rep(i, (int)currentVariables.size()) {
			int ix0 = index[scc.getColor(i * 2 + 0)];
			int ix1 = index[scc.getColor(i * 2 + 1)];
			res[currentVariables[i]] = ix0 < ix1;
		}
	}

private:
	void makeCondensation() {
		int n = graph.size();
		vector<pair<int, int>> edges;
		rep(i, n) for (int j : graph[i]) if (scc.getColor(i) != scc.getColor(j))
			edges.emplace_back(scc.getColor(i), scc.getColor(j));
		int S = 0;
		rep(i, n)
			amax(S, scc.getColor(i) + 1);
		condensation.init(S, edges);
	}

	int getVertex(int lit) {
		int &id = variableID[lit >> 1];
		if (id == -1) {
			id = (int)currentVariables.size();
			currentVariables.push_back(lit >> 1);
		}
		return id << 1 | (lit & 1);
	}

	vector<int> variableID;
	vector<int> currentVariables;
	vector<pair<int, int>> edges;
	StronglyConnectedComponents::Graph graph;
	StronglyConnectedComponents scc;
	StronglyConnectedComponents::Graph condensation;
	int sccS;
};

int main() {
	int T;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ++ ii) {
		int H; int W;
		scanf("%d%d", &H, &W);
		vector<string> field(H);
		rep(i, H) {
			char buf[101];
			scanf("%s", buf);
			field[i] = buf;
		}
		auto simulate = [H, W, &field](int y, int x, int dy, int dx) -> int {
			vector<vector<bool>> vis(H, vector<bool>(W));
			while (1) {
				if (vis[y][x]) return -1;
				vis[y][x] = true;
				y += dy, x += dx;
				if (y < 0 || y >= H || x < 0 || x >= W || field[y][x] == '#') return -1;
				if (field[y][x] == '-' || field[y][x] == '|') {
					int a = y * W + x;
					bool dir = field[y][x] == '-' ? (dy == 0) : (dx == 0);
					return a * 2 + (dir ? 1 : 0);
				}
				if (field[y][x] == '/') {
					int ndy = -dx, ndx = -dy;
					dy = ndy, dx = ndx;
				} else if (field[y][x] == '\\') {
					int ndy = dx, ndx = dy;
					dy = ndy, dx = ndx;
				}
			}
		};
		bool ok = true;
		vector<pair<int, int>> clauses;
		rep(i, H) rep(j, W) if (field[i][j] == '-' || field[i][j] == '|') {
			rep(rot, 2) {
				int dy = 0, dx = 1;
				if ((field[i][j] == '-') != (rot != 0)) swap(dy, dx);
				int a = simulate(i, j, dy, dx);
				int b = simulate(i, j, -dy, -dx);
				if (a != -1 || b != -1) {
					int x = (i * W + j) * 2 + rot;
					clauses.emplace_back(x ^ 1, x ^ 1);
				}
			}
		}
		rep(i, H) rep(j, W) if (field[i][j] == '.') {
			vi cs;
			rep(xy, 2) {
				int dy = 0, dx = 1;
				if (xy != 0) swap(dy, dx);
				int a = simulate(i, j, dy, dx);
				int b = simulate(i, j, -dy, -dx);
				if (a != -1 && b != -1) {
					//‚±‚±‚É—ˆ‚½‚ç‚¾‚ß
					clauses.emplace_back(a ^ 1, a ^ 1);
					clauses.emplace_back(b ^ 1, b ^ 1);
				} else if (a != -1 || b != -1) {
					cs.push_back(a != -1 ? a : b);
				}
			}
			if (cs.empty()) {
				ok = false;
				break;
			} else {
				clauses.emplace_back(cs.front(), cs.back());
			}
		}
		TwoSatisfiability sat;
		sat.init(H * W);
		ok &= sat.run(clauses);
		printf("Case #%d: ", ii + 1);
		if (!ok) {
			puts("IMPOSSIBLE");
		} else {
			puts("POSSIBLE");
			vector<bool> xs(H * W);
			sat.getAssignment(xs);
			vector<string> ans = field;
			rep(i, H) rep(j, W) if (!xs[i * W + j]) {
				char c = field[i][j];
				if (c != '-' && c != '|') continue;
				ans[i][j] = c == '-' ? '|' : '-';
			}
			rep(i, H)
				puts(ans[i].c_str());
		}
	}
	return 0;
}
