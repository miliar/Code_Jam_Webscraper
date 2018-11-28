#include <fstream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>

#pragma comment(linker, "/STACK:64000000")
typedef long long ll;

using namespace std;

const int MAXK = -1;
const int MAXN = -1;
const int MOD = 1; // 1000 * 1000 * 1000 + 7;
const int INF = (int)(1e9);

struct Graph {
private:
	struct Edge {
		int from, to, cap, flow, cost;

		Edge() {}
		Edge(int from, int to, int cap, int cost) : from(from), to(to), cap(cap), flow(0), cost(cost) {}
	};

	int n;
	int S, T;
	vector<vector<int> > e;
	vector<Edge> edges;
	vector<int> d, c;

	vector<int> p, pr, fl;

	int dijkstra() {
		d.assign(n, 1e9);
		pr.assign(n, -1);
		fl.assign(n, 0);
		set<pair<int, int> > st;
		d[0] = 0;
		fl[0] = 1e9;
		for (int i = 0; i < n; i++) st.insert(make_pair(d[i], i));

		while (!st.empty()) {
			int v = st.begin()->second;
			st.erase(st.begin());

			for (int i = 0; i < e[v].size(); i++) {
				Edge cur = edges[e[v][i]];
				if (d[cur.to] > d[v] + cur.cost + p[v] - p[cur.to] && cur.flow < cur.cap) {
					st.erase(make_pair(d[cur.to], cur.to));
					d[cur.to] = d[v] + cur.cost + p[v] - p[cur.to];
					st.insert(make_pair(d[cur.to], cur.to));
					fl[cur.to] = min(fl[v], cur.cap - cur.flow);
					pr[cur.to] = e[v][i];
				}
			}
		}
		for (int i = 0; i < n; i++) {
			p[i] += d[i];
			if (p[i] > 1e9) p[i] = 1e9;
		}
		return fl[n - 1];
	}

public:
	Graph() {}
	Graph(int N) {
		n = N;
		e.resize(n);
	}

	void addEdge(int from, int to, int cap, int cost = 0) {
		e[from].push_back(edges.size());
		edges.push_back(Edge(from, to, cap, cost));
		e[to].push_back(edges.size());
		edges.push_back(Edge(to, from, 0, -cost));
	}

	pair<int, int> minCost() {
		p.assign(n, 0);
		pair<int, int> res;

		while (1) {
			int fl = dijkstra();
			res.first += fl;
			if (!fl) break;
			int v = n - 1;
			while (v != 0) {
				int o = pr[v];
				edges[o].flow += fl;
				res.second += edges[o].cost * fl;
				edges[o ^ 1].flow -= fl;
				v = edges[o].from;
			}
		}
		return res;
	}
};

int main(int argc, char * argv[]) {
	int L, R;
	string s;
	if (1) {
		L = atoi(argv[1]);
		R = atoi(argv[2]);
		s = argv[3];
		cerr << L << " " << R << " " << s << endl;
	}
	else {
		L = 1, R = 100;
		s = "output1.txt";
	}
	freopen("input.txt", "r", stdin);
	freopen(s.c_str(), "w", stdout);
	/*ofstream fout;
	fout.open(s.c_str(), fstream::out);
	fout << 1 << endl;
	fout.close();
	return 0;*/

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		if (test >= L && test <= R) {
			cout << "Case #" << test << ": ";
			cerr << "Case #" << test << ": ";
		}
	
		int n, c, m;
		cin >> n >> c >> m;
		//c = 1000;
		vector<pair<int, int> > a(m);
		for (int i = 0; i < m; i++) {
			cin >> a[i].first >> a[i].second;
		}
		if (!(test >= L && test <= R)) {
			continue;
		}
		for (int i = 0; i < m; i++) {
			//a[i].second = rand() % c + 1;
			a[i].first--;
			a[i].second--;
		}
		vector<int> b1(n);
		vector<int> b2(c);
		for (int i = 0; i < m; i++) {
			b2[a[i].second]++;
			b1[a[i].first]++;
		}
		
		int mx = 0;
		//for (int i = 0; i < n; i++) mx = max(mx, b1[i]);
		for (int i = 0; i < c; i++) mx = max(mx, b2[i]);

		int L = mx - 1, R = m;
		auto solve = [&](int M) {
			int sz = 1 + c + n + n + 1;

			Graph gr(sz);
			for (int i = 0; i < m; i++) {
				gr.addEdge(0, 1 + a[i].second, 1, 0);
				gr.addEdge(1 + a[i].second, 1 + c + a[i].first, 1, 0);
			}
			for (int i = 0; i < n; i++) {
				gr.addEdge(1 + c + i, 1 + c + n + n, M, 0);
				gr.addEdge(1 + c + i, 1 + c + n + i, m, 1);
				gr.addEdge(1 + c + n + i, 1 + c + i, m, 0);
				if (i) {
					gr.addEdge(1 + c + n + i, 1 + c + n + i - 1, m, 0);
				}
			}
			return gr.minCost();
		};

		while (R - L > 1) {
			int M = (L + R) >> 1;
			
			auto o = solve(M);
			if (o.first == m) R = M;
			else L = M;
		}
		auto o = solve(R);

		cout << R << " " << o.second << endl;
		cerr << R << " " << o.second << endl;
	}
	fclose(stdout);

	return 0;
}