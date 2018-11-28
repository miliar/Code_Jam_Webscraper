#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cstdio>
#include <map>
#include <stack>

using namespace std;

class StronglyConnectedComponents {
private:
	const vector<vector<int>> &graph;
	vector<vector<int>> reversedGraph;
	vector<vector<int>> compressedGraph;
	vector<int> componentID;
	vector<int> postOrder;
	vector<bool> visited;
	stack<int> adjacent;

public:
	StronglyConnectedComponents(const vector<vector<int>> &graph) :
		graph(graph),
		reversedGraph(graph.size()),
		componentID(graph.size(), -1),
		visited(graph.size()) {
		for (int i = 0; i < graph.size(); i++) {
			for (int j : graph[i]) {
				reversedGraph[j].push_back(i);
			}
		}
		for (int i = 0; i < graph.size(); i++) {
			dfs(i);
		}
		reverse(postOrder.begin(), postOrder.end());
		for (int i : postOrder) {
			if (componentID[i] == -1) {
				dfs2(i);
				while (!adjacent.empty()) {
					visited[adjacent.top()] = true;
					adjacent.pop();
				}
				compressedGraph.emplace_back(vector<int>());
			}
		}
	}

	vector<vector<int>> &getCompressedGraph() {
		return compressedGraph;
	}

	int operator[](int u) {
		return componentID[u];
	}

private:
	void dfs(int u) {
		if (visited[u]) {
			return;
		}
		visited[u] = true;
		for (int v : graph[u]) {
			dfs(v);
		}
		postOrder.push_back(u);
	}

	void dfs2(int u) {
		componentID[u] = compressedGraph.size();
		for (int v : reversedGraph[u]) {
			if (componentID[v] == -1) {
				dfs2(v);
			} else if (componentID[v] != componentID[u] && visited[componentID[v]]) {
				compressedGraph[componentID[v]].push_back(componentID[u]);
				visited[componentID[v]] = false;
				adjacent.push(componentID[v]);
			}
		}
	}
};

class TwoSatisfiability {
private:
	vector<vector<int>> g;
	vector<bool> var;
	bool satisfiable;

public:
	TwoSatisfiability(int n) : g(n * 2), var(n) {}

	// i or j
	void add(int i, int ii, int j, int jj) {
		g[i * 2 + 1 - ii].push_back(j * 2 + jj);
		g[j * 2 + 1 - jj].push_back(i * 2 + ii);
	}

	bool isSatisfiable() {
		return satisfiable;
	}

	void build() {
		StronglyConnectedComponents scc(g);

		satisfiable = true;
		for (int i = 0; i < var.size(); i++) {
			if (scc[i * 2] == scc[i * 2 + 1]) {
				satisfiable = false;
			}
			var[i] = scc[i * 2] < scc[i * 2 + 1];
		}
	}

	bool operator[](int k) {
		return var[k];
	}
};

void solve() {
	int h, w;
	std::cin >> h >> w;

	std::vector<std::string> grid(h);
	for (int i = 0; i < h; i++) {
		std::cin >> grid[i];
	}

	std::vector<std::vector<int>> id(h, std::vector<int>(w, -1));
	int now = 0;
	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (grid[i][j] == '|' || grid[i][j] == '-') {
				id[i][j] = now++;
			}
		}
	}

	auto outside = [&](int i, int j) {
		return i < 0 || j < 0 || i >= h || j >= w || grid[i][j] == '#';
	};

	TwoSatisfiability sat(now);

	for (int i = 0; i < h; i++) {
		for (int j = 0; j < w; j++) {
			if (grid[i][j] == '#') {
				continue;
			}
			std::vector<int> hor;
			std::vector<int> ver;
			for (int d = 1; !outside(i + d, j); d++) {
				if (id[i + d][j] >= 0) {
					ver.push_back(id[i + d][j]);
				}
			}
			for (int d = 1; !outside(i - d, j); d++) {
				if (id[i - d][j] >= 0) {
					ver.push_back(id[i - d][j]);
				}
			}
			for (int d = 1; !outside(i, j + d); d++) {
				if (id[i][j + d] >= 0) {
					hor.push_back(id[i][j + d]);
				}
			}
			for (int d = 1; !outside(i, j - d); d++) {
				if (id[i][j - d] >= 0) {
					hor.push_back(id[i][j - d]);
				}
			}
			if (id[i][j] >= 0) {
				if (hor.size() >= 1) {
					sat.add(id[i][j], 1, id[i][j], 1);
				}
				if (ver.size() >= 1) {
					sat.add(id[i][j], 0, id[i][j], 0);
				}
			} else {
				if (ver.size() >= 2 && hor.size() >= 2) {
					puts("IMPOSSIBLE");
					return;
				}
				if (ver.size() == 1 && hor.size() == 1) {
					sat.add(ver[0], 1, hor[0], 0);
				} else if (ver.size() == 1) {
					sat.add(ver[0], 1, ver[0], 1);
				} else if (hor.size() == 1) {
					sat.add(hor[0], 0, hor[0], 0);
				} else {
					puts("IMPOSSIBLE");
					return;
				}
			}
		}
	}
	sat.build();
	if (sat.isSatisfiable()) {
		puts("POSSIBLE");
		for (int i = 0; i < h; i++) {
			for (int j = 0; j < w; j++) {
				if (id[i][j] >= 0) {
					putchar(sat[id[i][j]] ? '|' : '-');
				} else {
					putchar(grid[i][j]);
				}
			}
			puts("");
		}
	} else {
		puts("IMPOSSIBLE");
	}
}

int main() {
	int T;
	std::cin >> T;
	for (int i = 0; i < T; i++) {
		printf("Case #%d: ", i + 1);
		solve();
	}
}
