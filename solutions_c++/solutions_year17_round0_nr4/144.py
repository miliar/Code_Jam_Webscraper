#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <queue>

using namespace std;

typedef long long int64;

int MSB(int64 x) {
	for (int i = 60; i >= 0; --i) {
		if ((x>>i)&1) {
			return i;
		}
	}
}

int score(char c) {
	map<char, int> m;
	m['o'] = 2;
	m['+']  = m['x']  = 1;
	return m[c];
}

class FordFulkerson {
	struct Edge {
		int from, to, flow, cap, revInd;
		Edge(int from, int to, int flow, int cap, int revInd) : from(from), to(to), 
		flow(flow), cap(cap), revInd(revInd) {}
	};

	int n, src, dest;
	vector<Edge> edge;
	vector<vector<int>> G;
	bool sortedLists;

	vector<int> lastEdge;

	virtual bool findPath() {
		for (int i = 1; i <= n; ++i) {
			lastEdge[i] = -2;
		}
		queue<int> Q;
		lastEdge[src] = -1;
		Q.push(src);

		while (!Q.empty()) {
			int x = Q.front();
			Q.pop();

			for (auto ind : G[x]) {
				auto& e = edge[ind];
				if (e.flow != e.cap && lastEdge[e.to] == -2) {
					Q.push(e.to);
					lastEdge[e.to] = ind;

					if (e.to == dest) {
						return true;
					}
				}
			}
		}

		return false;
	}

  public:
	FordFulkerson(int n, int src, int dest) : n(n), src(src), dest(dest) {
		sortedLists = false;
		G.resize(n+1);
		lastEdge.resize(n+1, -2);
	}

	int runPath() {
		int flow = 0;
		if (findPath()) {
			int minFlow = ((1<<31)-1);
			for (int x = dest; x != src; x = edge[lastEdge[x]].from) {
				auto& e = edge[lastEdge[x]];
				minFlow = min(minFlow, e.cap - e.flow);
			}
			flow += minFlow;
			for (int x = dest; x != src; x = edge[lastEdge[x]].from) {
				auto& e = edge[lastEdge[x]];
				e.flow += minFlow;
				edge[e.revInd].flow -= minFlow;
			}
		}
		return flow;
	}

	void addEdge(int x, int y, int flow, int cap) {
		while (x > n) {
			++n;
			G.push_back(vector<int>());
			lastEdge.push_back(-2);
		}

		int sz = edge.size();
		edge.push_back(Edge(x, y, flow, cap, sz+1));
		edge.push_back(Edge(y, x, -flow, 0, sz));

		G[x].push_back(sz);
		G[y].push_back(sz+1);

		sortedLists = false;
	}

	int runFlow() {
		int flow = 0;
		int add = 0;
		for (;add = runPath(); flow += add);

		// cerr << "Here" << endl;
		// for (auto& e : edge) {
		// 	cerr << e.from << " " << e.to << " " << e.flow << " " << e.cap << "\n";
		// }


		return flow;
	}

	int getFlow(int x, int y) {
		// cerr << "Q " << x << " " << y << " ";
		if (!sortedLists) {
			auto cmp = [&](int i, int j) {
				return edge[i].to < edge[j].to;
			};

			for (int i = 1; i <= n; ++i) {
				sort(G[i].begin(), G[i].end(), cmp);
			}
			sortedLists = true;
		}

		auto cmp2 = [&](int i, int y) {
			return edge[i].to < y;
		};
		auto it = lower_bound(G[x].begin(), G[x].end(), y, cmp2);
		// cerr << edge[*it].to << "\n";
		if (it == G[x].end() || edge[*it].to != y) {
			// cerr << 0 << "\n";
			return 0;
		}
		// cerr << edge[*it].flow << "\n";
		return edge[*it].flow;
	}
};

int n, m;

int diag1(int i, int j) {
	return i + j - 1;
}

int diag2(int i, int j) {
	return i - j + n;
}

int rowInd(int i) {
	return 2 + i;
}

int colInd(int i) {
	return 2 + n + i;
}

int diag1Ind(int i) {
	return 2 + n + n + i;
}

int diag2Ind(int i) {
	return 2 + n + n + (2*n - 1) + i;
}

void solve(int test) {
	cout << "Case #" << test << ": ";

	cin >> n >> m;

	vector<vector<int>> mat(n+1, vector<int>(n+1, 0));
	vector<bool> usedRow(n+1), usedCol(n+1), usedDiag1(2*n), usedDiag2(2*n);

	vector<vector<char>> s(n+1, vector<char>(n+1, '.'));

	int nodes = 2 + 2*n + 2*(2*n-1);
	int src = 1;
	int dest = 2;
	FordFulkerson mf(nodes, src, dest);
	int sc = 0;

	for (int i = 1; i <= m; ++i) {
		char c;
		int x, y;
		cin >> c >> x >> y;
		s[x][y] = c;
		sc += score(c);
		if (c == '+' || c == 'o') {
			usedDiag1[diag1(x, y)] = true;
			usedDiag2[diag2(x, y)] = true;
		}
		if (c == 'x' || c == 'o') {
			usedRow[x] = true;
			usedCol[y] = true;
		}
	}

	for (int i = 1; i <= n; ++i) {
		if (!usedRow[i]) {
			mf.addEdge(src, rowInd(i), 0, 1);
		}
		if (!usedCol[i]) {
			mf.addEdge(colInd(i), dest, 0, 1);
		}
	}
	for (int i = 1; i <= 2*n-1; ++i) {
		if (!usedDiag1[i]) {
			mf.addEdge(src, diag1Ind(i), 0, 1);
		}
		if (!usedDiag2[i]) {
			mf.addEdge(diag2Ind(i), dest, 0, 1);
		}
	}

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			mf.addEdge(rowInd(i), colInd(j), 0, 1);
			mf.addEdge(diag1Ind(diag1(i, j)), diag2Ind(diag2(i, j)), 0, 1);
		}
	}

	cout << sc + mf.runFlow() << " ";
	vector<tuple<char, int, int>> sol;

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= n; ++j) {
			int f1 = mf.getFlow(rowInd(i), colInd(j));
			int f2 = mf.getFlow(diag1Ind(diag1(i, j)), diag2Ind(diag2(i, j)));
			if ((f1 == 1 && f2 == 1) || (f1 == 1 && s[i][j] == '+') || (f2 == 1 && s[i][j] == 'x')) {
				sol.emplace_back('o', i, j);
			} else if (f1 == 1) {
				sol.emplace_back('x', i, j);
			} else if (f2 == 1) {
				sol.emplace_back('+', i, j);
			}
		}
	}

	cout << sol.size() << "\n";
	for (auto el : sol) {
		cout << get<0>(el) << " " << get<1>(el) << " " << get<2>(el) << "\n"; 
	}
}

int main() {
	int tests;
	cin >> tests;

	for (int k = 1; k <= tests; ++k) {
		solve(k);
	}
}