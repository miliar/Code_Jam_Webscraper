#include <bits/stdc++.h>

using namespace std;

/*
Steps:
1. horses -> cities, weights
2. floyd warshall on new graph
*/

struct Rat {
	long long a, b;

	bool operator < (Rat& rhs) {
		return a * rhs.b < rhs.a * b;
	}
};

struct City {
	int e, s;

	vector<int> edges;
	vector<int> costs;
};

int n, q;
vector<City> cities;

vector<vector<Rat>> mgraph;
vector<vector<double>> mgraph2;

void meta(int v) {
	int mdist = cities[v].e;
	int speed = cities[v].s;

	queue<pair<int, long long>> bfs;
	bfs.push(make_pair(v, 0));

	while(bfs.size() > 0) {
		int cur = bfs.front().first;
		long long dist = bfs.front().second;
		bfs.pop();

		//asdfasfa
		if(dist > mdist) {
			continue;
		}

		Rat cost;
		cost.a = dist;
		cost.b = speed;

		if(mgraph[v][cur].b == 0 || !(mgraph[v][cur] < cost)) {
			mgraph[v][cur] = cost;

			for(int i = 0; i < cities[cur].edges.size(); i++) {
				int edge = cities[cur].edges[i];
				int edist = cities[cur].costs[i];

				bfs.push(make_pair(edge, dist + edist));
			}
		}
	}
}

void runTestCase(int t) {
	cin >> n >> q;

	cities = vector<City>(n);
	mgraph = vector<vector<Rat>>(n, vector<Rat>(n));
	mgraph2 = vector<vector<double>>(n, vector<double>(n, 0));

	for(int i = 0; i < n; i++) {
		cin >> cities[i].e >> cities[i].s;
	}

	for(int i = 0; i < n; i++) {
		for(int j = 0; j < n; j++) {
			int cost;
			cin >> cost;

			if(cost != -1) {
				cities[i].edges.push_back(j);
				cities[i].costs.push_back(cost);
			}
		}
	}

	/*
	for(int i = 0; i < n; i++) {
		Rat zero;
		zero.a = 0;
		zero.b = 1;

		mgraph[i][i] = zero;
	}
	*/

	for(int i = 0; i < n; i++) {
		meta(i);
	}
	
	cout << "Case #" << t << ": ";

	for(int i = 0; i < n; i++) {
		//cerr << endl;
		for(int j = 0; j < n; j++) {
			if(mgraph[i][j].b == 0) {
				mgraph2[i][j] = -1;
			}
			else {
				mgraph2[i][j] = mgraph[i][j].a / (double) mgraph[i][j].b;
			}
			//cerr << mgraph2[i][j] << " ";
			//cerr << mgraph[i][j].a << "/" << mgraph[i][j].b << " ";
		}
	}
	//cerr << endl;

	for(int k = 0; k < n; k++) {
		for(int i = 0; i < n; i++) {
			if(mgraph2[i][k] == -1) continue;
			for(int j = 0; j < n; j++) {
				if(mgraph2[k][j] == -1) continue;
				//cout << i << " " << k << " " << j << endl;

				if(mgraph2[i][j] > mgraph2[i][k] + mgraph2[k][j] || mgraph2[i][j] == -1) {
					mgraph2[i][j] = mgraph2[i][k] + mgraph2[k][j];
					//cout << "upd: " << mgraph2[i][j] << endl;
				}
			}
		}
	}

	string sep = "";
	for(int i = 0; i < q; i++) {
		int u, v;
		cin >> u >> v;
		u--;
		v--;

		cout << sep << mgraph2[u][v];
		sep = " ";
	}
	cout << endl;
}

int main() {
	int t;
	cin >> t;

	cout << fixed << setprecision(16);

	for(int i = 1; i <= t; i++) {
		runTestCase(i);
	}

	return 0;
}
