#include <deque>
#include <vector>
#include <algorithm>
#include <iostream>

#include <map>
#include <set>

using namespace std;




void solve(int i0) {
	int n, p; 
	cin >> n >> p;
	vector<int> r(n);
	for (int i = 0; i < n; ++i)
		cin >> r[i];

	set<int> serv;
	vector<deque<int>> q(n);


	for (int i = 0; i < n; ++i) {
		q[i].resize(p);
		for (int j = 0; j < p; ++j) {
			cin >> q[i][j];
		};
		sort(q[i].begin(), q[i].end());
	};

	bool quit = false;
	int ans = 0;

	for (int serv = 1; serv <= 2000000; ++serv) {
		while (true) {
			bool flag = true;
			if (quit) break;
			for (int i = 0; i < n; ++i) {
				double lower = 0.9*serv*r[i] ;

				while (q[i].size() && lower > q[i].front()) q[i].pop_front();
				if (q[i].size() == 0) {
					quit = true;
					break;
				};
				
				if (1.1*serv*r[i] < q[i].front()) {
					flag = false;
					break;
				}
			};
			if (quit) break;

			if (flag) {
				ans++;
				for (int i = 0; i < n; ++i) {
					q[i].pop_front();
					if (q[i].size() == 0) {
						quit = true;
					};
				}; 
			}
			else 
				break;

		};

		if (quit) break;

	}

	printf("Case #%d: %d\n", i0, ans);
};

int main() {
	//freopen("B.in", "r", stdin);

//	freopen("B-small-attempt1.in", "r", stdin);
//	freopen("B-small-attempt1.out2", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out2", "w", stdout);

	int t;
	cin >> t;
	for (int i0=1; i0<=t; ++i0) {
		solve(i0);
	};

}