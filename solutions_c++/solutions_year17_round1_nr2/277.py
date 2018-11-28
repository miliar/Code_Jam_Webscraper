#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>
#include <algorithm>
#include <functional>
using namespace std;

int n, p;
int r[100];
int q[100][100];
pair<double, double> lr[100];

void proc(int caseidx) {
	scanf("%d %d", &n, &p);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &r[i]);
	}
	vector<priority_queue<int, vector<int>, greater<int>>> pqs(n);
	for (int i = 0; i < n; ++i) {
		for (int j = 0; j < p; ++j) {
			scanf("%d", &q[i][j]);
			pqs[i].push(q[i][j]);
		}
	}

	int ans = 0;
	for (int g = 1; g <= 1000000; ++g) {
		bool ok = true;
		for (int i = 0; i < n; ++i) {
			if (pqs[i].empty()) {
				ok = false;
				break;
			}
			while (!pqs[i].empty() && pqs[i].top() * 10ll < (long long)g * r[i] * 9) {
				pqs[i].pop();
			}

			if (!pqs[i].empty() && pqs[i].top() * 10ll <= (long long)g * r[i] * 11) {

			}
			else {
				ok = false;
				break;
			}
		}
		if (!ok) continue;

		for (int i = 0; i < n; ++i) {
			pqs[i].pop();
		}
		++ans;
		--g;
	}

	printf("Case #%d: %d\n", caseidx, ans);
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