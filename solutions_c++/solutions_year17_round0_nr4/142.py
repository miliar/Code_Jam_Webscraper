#include <cstdio>
#include <cstring>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

template <typename flowT>
struct MaxFlowDinic {
	struct Edge {
		int next, inv;
		flowT res;
	};
	int n;
	vector<vector<Edge>> graph;
	vector<int> l; // assigned level.  if l[i] == 0, i is unreachable.
	vector<int> q, start;
	void init(int _n) {
		n = _n;
		graph.clear();
		graph.resize(n);
	}
	void add_edge(int s, int e, flowT cap, flowT caprev = 0) {
		Edge forward{ e, graph[e].size(), cap };
		Edge reverse{ s, graph[s].size(), caprev };
		graph[s].push_back(forward);
		graph[e].push_back(reverse);
	}
	bool assign_level(int source, int sink) {
		l.assign(l.size(), 0);
		l[source] = 1;
		int t = 0;
		q[t++] = source;
		for (int h = 0; h < t && !l[sink]; ++h) {
			int cur = q[h];
			for (const auto& e : graph[cur]) {
				if (l[e.next] || e.res == 0) continue;
				l[e.next] = l[cur] + 1;
				q[t++] = e.next;
			}
		}
		return l[sink] != 0;
	}
	flowT block_flow(int cur, int sink, flowT current) {
		if (cur == sink) return current;
		for (int& i = start[cur]; i < graph[cur].size(); ++i) {
			auto& e = graph[cur][i];
			if (e.res == 0 || l[e.next] != l[cur] + 1) continue;
			if (flowT res = block_flow(e.next, sink, min(e.res, current))) {
				e.res -= res;
				graph[e.next][e.inv].res += res;
				return res;
			}
		}
		return 0;
	}
	flowT solve(int source, int sink) {
		q.resize(n);  l.resize(n);  start.resize(n);
		flowT ans = 0;
		while (assign_level(source, sink)) {
			start.assign(start.size(), 0);
			while (flowT flow = block_flow(source, sink, numeric_limits<flowT>::max()))
				ans += flow;
		}
		return ans;
	}
};

int n, m;
bool set0[100][100], set1[100][100];
bool matchedRow[100], matchedCol[100], matchedLeftDiag[200], matchedRightDiag[200];

inline int getCellNode(int i, int j) {
	return 1 + i * n + j;
}

inline int getRowFrontNode(int i) {
	return 1 + n * n + i;
}

inline int getRowNode(int i) {
	return 1 + n * n + n + i;
}

inline int getColNode(int j) {
	return 1 + n * n + n + n + j;
}

inline int getLeftDiagFrontNode(int id) {
	return 1 + n * n + n + n + n + id;
}

inline int getLeftDiagNode(int id) {
	//int id = i + j;
	return 1 + n * n + n + n + n + n * 2 + id;
}

inline int getRightDiagNode(int id) {
	//int id = i - j + n - 1;
	return 1 + n * n + n + n + n + n * 2 + n * 2 + id;
}

inline int getSink() {
	return 1 + n * n + n + n + n + n * 2 + n * 2 + n * 2;
}

void proc(int caseidx) {
	memset(set0, 0, sizeof(set0));
	memset(set1, 0, sizeof(set1));
	memset(matchedRow, 0, sizeof(matchedRow));
	memset(matchedCol, 0, sizeof(matchedCol));
	memset(matchedLeftDiag, 0, sizeof(matchedLeftDiag));
	memset(matchedRightDiag, 0, sizeof(matchedRightDiag));
	scanf("%d %d", &n, &m);

	int oldpoint = 0;
	for (int i = 0; i < m; ++i) {
		int a, b;
		char c;
		scanf(" %c %d %d", &c, &a, &b);
		--a; --b;
		if (c == 'x' || c == 'o') {
			set0[a][b] = true;
			matchedRow[a] = matchedCol[b] = true;
			++oldpoint;
		}
		if (c == '+' || c == 'o') {
			set1[a][b] = true;
			matchedLeftDiag[a + b] = matchedRightDiag[a - b + n - 1] = true;
			++oldpoint;
		}
	}

	MaxFlowDinic<int> mf;
	mf.init(n * n + n * 4 + n * 8 + 2);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			int need = 2;
			if (set0[i][j]) --need;
			if (set1[i][j]) --need;
			mf.add_edge(0, getCellNode(i, j), need);

			if (!matchedRow[i] && !matchedCol[j]) {
				mf.add_edge(getCellNode(i, j), getRowFrontNode(i), 1);
				mf.add_edge(getRowNode(i), getColNode(j), 1);
			}

			if (!matchedLeftDiag[i + j] && !matchedRightDiag[i - j + n - 1]) {
				mf.add_edge(getCellNode(i, j), getLeftDiagFrontNode(i + j), 1);
				mf.add_edge(getLeftDiagNode(i + j), getRightDiagNode(i - j + n - 1), 1);
			}
		}
	}
	for (int i = 0; i < n; ++i) {
		mf.add_edge(getRowFrontNode(i), getRowNode(i), 1);
		if (!matchedCol[i]) {
			mf.add_edge(getColNode(i), getSink(), 1);
		}
	}
	for (int i = 0; i < n * 2; ++i) {
		mf.add_edge(getLeftDiagFrontNode(i), getLeftDiagNode(i), 1);
		if (!matchedRightDiag[i]) {
			mf.add_edge(getRightDiagNode(i), getSink(), 1);
		}
	}

	printf("Case #%d: %d ", caseidx, oldpoint + mf.solve(0, getSink()));
	vector<tuple<char, int, int>> anslist;
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < n; ++j) {
			int nod0 = getRowNode(i);
			bool ok0 = false;
			int nxt0 = getColNode(j);
			for (auto& edge : mf.graph[nod0]) {
				if (edge.next == nxt0 && mf.graph[edge.next][edge.inv].res > 0) {
					ok0 = true;
					break;
				}
			}

			int nod1 = getLeftDiagNode(i + j);
			bool ok1 = false;
			int nxt1 = getRightDiagNode(i - j + n - 1);
			for (auto& edge : mf.graph[nod1]) {
				if (edge.next == nxt1 && mf.graph[edge.next][edge.inv].res > 0) {
					ok1 = true;
					break;
				}
			}

			if ((ok0 && ok1) || (set0[i][j] && ok1) || (set1[i][j] && ok0)) {
				anslist.emplace_back('o', i + 1, j + 1);
			}
			else if (ok0) {
				anslist.emplace_back('x', i + 1, j + 1);
			}
			else if (ok1) {
				anslist.emplace_back('+', i + 1, j + 1);
			}
		}
	}

	printf("%d\n", anslist.size());
	for (const auto& p : anslist) {
		char c;
		int i, j;
		tie(c, i, j) = p;
		printf("%c %d %d\n", c, i, j);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}