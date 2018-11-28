#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <queue>

using namespace std;

const int N = 50;
const int P = 50;

int r[N];
int q[N][P];
vector<pair<pair<int, int>, int> > a;
queue<int> que[N];
int n, p;

int main() {
	int testCases;
	scanf("%d", &testCases);
	for (int _ = 1; _ <= testCases; ++_) {
		scanf("%d%d", &n, &p);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &r[i]);
		}

		a.clear();
		for (int i = 0; i < n; ++i) {
			for (int j = 0; j < p; ++j) {
				scanf("%d", &q[i][j]);
				int kMin = int(ceil(q[i][j] / (1.1 * r[i])) + 0.5), kMax = int(floor(q[i][j] / (0.9 * r[i])) + 0.5);
//				cerr << r[i] << ' ' << q[i][j] << ' ' << kMin << ' ' << kMax << endl;
				if (kMin <= kMax) {
					a.push_back(make_pair(make_pair(kMin, kMax), i));
				}
			}
		}
		sort(a.begin(), a.end());
		for (int i = 0; i < n; ++i) {
			for (; !que[i].empty(); que[i].pop());
		}
		int ret = 0;
		for (int i = 0; i < (int)a.size(); ++i) {
			int kMin = a[i].first.first;
			int kMax = a[i].first.second;
			int c = a[i].second;
			que[c].push(kMax);

			bool flag = true;
			for (int j = 0; j < n; ++j) {
				for (; !que[j].empty() && que[j].front() < kMin; que[j].pop());
				if (que[j].empty()) {
					flag = false;
				}
			}

			if (flag) {
				++ret;
				for (int j = 0; j < n; ++j) {
					que[j].pop();
				}
			}
		}

		printf("Case #%d: %d\n", _, ret);
	}
	return 0;
}
