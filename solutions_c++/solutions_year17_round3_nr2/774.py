#include <iostream>
#include <fstream>
#include <cstdio>
#include <vector>
#include <iomanip>
#include <set>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <list>


using namespace std;

typedef pair<int, int> ii;

int main() {
#ifdef _DEBUG
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
#endif
	ios::sync_with_stdio(false);
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		cout << "Case #" << t << ": ";

		int n, m;
		cin >> n >> m;

		vector<ii> e;

		for (int i = 0; i < n; i++) {
			int s, f;
			cin >> s >> f;
			e.push_back(ii(s, 1));
			e.push_back(ii(f, -1));
		}

		for (int i = 0; i < m; i++) {
			int s, f;
			cin >> s >> f;
			e.push_back(ii(s, 2));
			e.push_back(ii(f, -2));
		}

		sort(e.begin(), e.end());

		ii z = e.front();
		z.first += 1440;
		e.push_back(z);
		int last = 0;
		int sw = 0;

		vector<int> r[3];
		vector<int> rr[3];
		int tt[3] = { 0, 0, 0 };
		last = abs(e[0].second);
		for (int i = 1; i < e.size(); i++) {
			int dt = e[i].first - e[i - 1].first;
			if (e[i].second < 0) {
				tt[last] += dt;
			}
			else {
				tt[last] += dt;
				if (abs(e[i].second) != last) {
					sw++;
					r[last].push_back(dt);
				}
				else {
					rr[last].push_back(dt);
				}
			}
			last = abs(e[i].second);
		}

		int g1 = 1;
		int g2 = 2;
		if (tt[g1] > tt[g2]) {
			swap(g1, g2);
		}

		for (int i = 0; i < 3; i++) {
			sort(rr[i].begin(), rr[i].end()); 
		}

		while (tt[g1] < tt[g2]) {
			if (r[g2].size() > 0) {
				tt[g1] += r[g2].back();
				tt[g2] -= r[g2].back();
				r[g2].pop_back();
			}
			else {
				tt[g1] += rr[g2].back();
				tt[g2] -= rr[g2].back();
				sw += 2;
				rr[g2].pop_back();
			}
		}

		cout << sw << endl;
	}

	return 0;
}