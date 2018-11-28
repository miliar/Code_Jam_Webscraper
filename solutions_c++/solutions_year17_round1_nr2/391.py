#include <cstdio>
#include <cstdlib>
#include <cstring>

#include <algorithm>
#include <vector>

using namespace std;

const int N = 60;
int r[N][N], a[N], ptr[N];
vector<pair<int, int> > range[N];

void run(int cas) {
	int n, p;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
		scanf("%d", a + i);
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++)
			scanf("%d", r[i] + j);
		range[i].clear();
		for (int j = 0; j < p; j++) {
			int hi = 10 * r[i][j] / (9 * a[i]);
			int lo = 10 * r[i][j] / (11 * a[i]);
			if (lo * a[i] * 11 < 10 * r[i][j]) lo++;
			if (lo <= hi)
				range[i].push_back(make_pair(lo, hi));
		}
		sort(range[i].begin(), range[i].end());
	}
	memset(ptr, 0, sizeof(ptr));
	int ans = 0;
	for (int j = 0; j < range[0].size(); j++) {
		bool succ = false;
		for (int cur = range[0][j].first; !succ && 
				cur <= range[0][j].second; cur++) {
			bool ok = true;
			for (int i = 1; i < n; i++) {
				while (ptr[i] < range[i].size() && range[i][ptr[i]].second < cur)
					ptr[i]++;
				if (ptr[i] == range[i].size() || range[i][ptr[i]].first > cur)
					ok = false;
			}
			if (ok) {
				succ = true;
				for (int i = 1; i < n; i++)
					ptr[i] += 1;
			}
		}
		if (succ)
			ans += 1;
	}
	printf("Case #%d: %d\n", cas, ans);
}

int main() {
	int cas, tt;
	scanf("%d", &tt);
	for (cas = 1; cas <= tt; cas++)
		run(cas);
	return 0;
}