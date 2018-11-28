#include <bits/stdc++.h>


#define ff first
#define ss second
#define puba push_back


using namespace std;


typedef long long LL;
typedef pair<int, int> pii;


const int MAXV = 2010;
const int MAXE = (int) 2 * 1e6;
const int MAXN = 1010;


int sum[MAXN], g[MAXN][MAXN];
int cap[MAXE], f[MAXE], cost[MAXE], to[MAXE], fr[MAXE];
int num_e, n, m, c;
int dist[MAXV], label[MAXV], q[MAXV], par[MAXV];
vector<int> gr[MAXV];


void clear_flow() {
	memset(f, 0, sizeof(int) * num_e);
}


void add_edge(int _fr, int _to, int _cap, int _cost) {
	fr[num_e] = _fr;
	to[num_e] = _to;
	cap[num_e] = _cap;
	cost[num_e] = _cost;
	f[num_e] = 0;
	gr[_fr].puba(num_e++);

	fr[num_e] = _to;
	to[num_e] = _fr;
	cap[num_e] = 0;
	cost[num_e] = -_cost;
	f[num_e] = 0;
	gr[_to].puba(num_e++);
} 

void set_cap(int val) {
	int cur = num_e - 2;
	for (int i = 0; i < n; ++i) {
		cap[cur] = val;
		cur -= 2;
	}
}


bool bfs() {
	memset(label, 0, sizeof(label));
	memset(dist, -1, sizeof(dist));

	dist[0] = 0;
	q[0] = 0;

	for (int l = 0, r = 1; l < r; ++l) {
		int v = q[l];

		for (int e : gr[v]) {
			int tov = to[e];
			if (dist[tov] == -1 && cap[e] != f[e]) {
				q[r++] = tov;
				dist[tov] = dist[v] + 1;
			}
		}
	}
	return dist[1] != -1;
}


bool dfs(int v, int ed, int flow) {
	if (v == ed) return flow;

	int sz = gr[v].size();
	for (; label[v] < sz; ++label[v]) {
		int e = gr[v][label[v]];
		int tov = to[e];
		if (dist[tov] == dist[v] + 1 && cap[e] != f[e]) {
			int pushed = dfs(tov, ed, min(flow, cap[e] - f[e]));
			if (pushed) {
				f[e] += pushed;
				f[e ^ 1] -= pushed;
				return pushed;
			}
		}
	}
	return 0;
}


int get_max_flow() {
	int ans = 0;
	while (bfs()) {

		int pushed = dfs(0, 1, m);
		//cout << pushed << " " << m << endl;
		while (pushed != 0) {
			ans += pushed;
			pushed = dfs(0, 1, m);
		}
	}
	return ans;
}


void get_min_path() {
	memset(dist, -1, sizeof(dist));
	deque<int> deq;
	dist[0] = 0;

	deq.push_back(0);

	for (; !deq.empty(); ) {
		int v = deq.front();
		deq.pop_front();

		for (int e : gr[v]) {
			int len = cost[e];
			int tov = to[e];

			if ((dist[tov] == -1 || dist[tov] > dist[v] + len) && (cap[e] != f[e])) {
				dist[tov] = dist[v] + len;
				par[tov] = e;
				if (len == 0) {
					deq.push_front(tov);					
				}
				else {
					deq.push_back(tov);
				}
			}
		}
	}
}

int get_min_cost_flow() {
	int ans = 0;


	for (int i = 0; i < m; ++i) {
		get_min_path();
		ans += dist[1];
		int v = 1;
		while (v != 0) {
			int e = par[v];
			f[e] += 1;
			f[e ^ 1] -= 1;
			v = fr[e];
		}
	}

	return ans;
}


void print() {
	for (int i = 0; i < num_e; ++i) {
		cout << fr[i] << " " << to[i] << " " << cap[i] << " " << f[i] << " " << cost[i] << endl;
	}

	cout << endl;

	for (int i = 0; i < 2 + n + c; ++i) {
		for (int e : gr[i]) {
			cout << e << " ";
		}
		cout << endl;
	}
	cout << endl;

}


int main() {
	int t;
	cin >> t;
	for (int q = 0; q < t; ++q) {
		

		cin >> n >> c >> m;
		num_e = 0;

		for (int i = 0; i < MAXV; ++i) {
			gr[i].clear();
		}

		for (int i = 0; i < c; ++i) {
			sum[i] = 0;
			for (int j = 0; j < n; ++j) {
				g[i][j] = 0;
			}
		}

		for (int i = 0; i < m; ++i) {
			int p, b;
			cin >> p >> b;
			--p, --b;
			g[b][p]++;
			sum[b]++;			
		}

		int mx = 0;
		for (int i = 0; i < c; ++i) {
			mx = max(sum[i], mx);
			add_edge(0, i + 2, sum[i], 0);
		}

		for (int i = 0; i < c; ++i) {
			for (int j = 0; j < n; ++j) {
				if (g[i][j] != 0) {
					add_edge(i + 2, 2 + c + j, g[i][j], 0);
				}
			}
		}

		for (int i = 0; i < c; ++i) {
			for (int j = n - 2; j >= 0; --j) {
				int cur = g[i][j];
				g[i][j] += g[i][j + 1];
				if (g[i][j] - cur != 0) {
					add_edge(i + 2, 2 + c + j, g[i][j] - cur, 1);
				}
			}
		}

		for (int i = 0; i < n; ++i) {
			add_edge(2 + c + i, 1, 0, 0);
		}

		int l = mx - 1;
		int r = m;

		while (r - l > 1) {
			int dm = (r + l) / 2;

			clear_flow();

			set_cap(dm);

			//print();

			int cans = get_max_flow();

			//cout << cans << " " << dm << endl;
			if (cans == m) {
				r = dm;
			}
			else {
				l = dm;
			}
		}



		clear_flow();

		set_cap(r);
		cout << "Case #" << q + 1 << ": ";
		cout << r << " " << get_min_cost_flow();

		cout << endl;
	}
	return 0;
}