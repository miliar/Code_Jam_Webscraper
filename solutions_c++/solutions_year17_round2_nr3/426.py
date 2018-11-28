#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const double MINZ = -1e-3;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tc;
	cin >> tc;
	for (int t = 1; t <= tc; ++t) {
		int n, q;
		cin >> n >> q;
		vector <pair <double, double> > arr(n);
		for (int i = 0; i < n; ++i)
			cin >> arr[i].first >> arr[i].second;
		vector <vector <double> > gr(n, vector <double>(n));
		for (int i = 0; i < n; ++i)
			for (int j = 0; j < n; ++j)
				cin >> gr[i][j];

		for (int j = 0; j < n; ++j)
			gr[j][j] = 0;
		for (int k = 0; k < n; ++k)
			for (int i = 0; i < n; ++i)
				for (int j = 0; j < n; ++j)
					if (gr[i][k] > MINZ && gr[k][j] > MINZ)
						if (gr[i][j] < MINZ || gr[i][j] > gr[i][k] + gr[k][j])
							gr[i][j] = gr[i][k] + gr[k][j];

		cout << "Case #" << t << ": ";
		for (int i = 0; i < q; ++i) {
			int a, b;
			cin >> a >> b;
			--a;
			--b;
			
			set <pair <double, int> > q;
			vector <double> dp(n + 1, 1e18);
			dp[a] = 0;
			q.insert({ 0, a });
			while (!q.empty()) {
				auto p = *q.begin();
				q.erase(q.begin());
				for (int j = 0; j < n; ++j)
					if (   gr[p.second][j] > MINZ
						&& gr[p.second][j] < arr[p.second].first - MINZ
						&& dp[j] > p.first + gr[p.second][j] / arr[p.second].second) {
						pair <double, int> to = {dp[j], j};
						auto it = q.find(to);
						if (it != q.end())
							q.erase(it);
						dp[j] = p.first + gr[p.second][j] / arr[p.second].second;
						q.insert({ dp[j], j });
					}
			}

			printf("%.9lf ", dp[b]);
			//solve small end
		}
		cout << endl;
	}
}