#include <fstream>
#include <iomanip>
#include <vector>
#include <queue>

using namespace std;

ifstream fin("C-large.in");
ofstream fout("out.txt");

double e[100], s[100], x[100][100];
int n;
const double INF = 1000000000000000;

double dijkstra(vector<vector<pair<double, int>>> a, int start, int fin)
{
	vector<double> d(n, INF), p(n);
	d[start] = 0.0;
	priority_queue<pair<double, int>> q;
	q.push(make_pair (0, start));
	while (!q.empty()) {
		int v = q.top().second;
		double cur_d = -q.top().first;
		q.pop();
		if (cur_d > d[v])  continue;
 
		for (size_t j = 0; j < a[v].size(); ++j) {
			int to = a[v][j].second;
			double len = a[v][j].first;
			if (d[v] + len < d[to]) {
				d[to] = d[v] + len;
				p[to] = v;
				q.push(make_pair (-d[to], to));
			}
		}
	}
	return d[fin];
}

vector<double> dijkstra0(int start, int fin)
{
	vector<double> d(n, INF), p(n);
	d[start] = 0.0;
	priority_queue<pair<double, int>> q;
	q.push(make_pair (0, start));
	while (!q.empty()) {
		int v = q.top().second;
		double cur_d = -q.top().first;
		q.pop();
		if (cur_d > d[v])  continue;
 
		for (size_t j = 0; j < n; ++j) {
			int to = j;
			double len = x[v][j];
			if (d[v] + len < d[to] && len != -1) {
				d[to] = d[v] + len;
				p[to] = v;
				q.push(make_pair (-d[to], to));
			}
		}
	}
	return d;
}

int main() {
	int tests;
	fin >> tests;
	for (int test = 0; test < tests; ++test) {
		vector<vector<pair<double, int>>> a;
		int q;
		fin >> n >> q;
		int h;
		for (int i = 0; i < n; ++i) {
			fin >> e[i] >> s[i];
			vector<pair<double, int>> o;
			a.push_back(o);
		}
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < n; ++j) {
				fin >> x[i][j];
			}
		}
		for (int i = 0; i < n; ++i) {
			vector<double> dist = dijkstra0(i, n);
			for (int j = 0; j < n; ++j) {
				if (i != j) {
					if (dist[j] > e[i]) {
					} else {
						double t = dist[j] / s[i];
						a[i].push_back(make_pair(t, j));
					}
				}
			}
		}

		fout << fixed << setprecision(8) << "Case #" << test + 1 << ": ";
		for (int i = 0; i < q; ++i) {
			int st, fini;
			fin >> st >> fini;
			fout << fixed << setprecision(8) << dijkstra(a, st - 1, fini - 1) << " ";
		}
		fout << endl;
	}
	return 0;
}