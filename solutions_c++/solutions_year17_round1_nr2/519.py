#include <cstdio>
#include <cmath>
#include <queue>
#include <utility>
#include <algorithm>
using namespace std;

const int MAXN = 55, MAXP = 55, INFTY = 0x3fffffff;
int N, P, R[MAXN];
priority_queue<pair<int, int>, vector<pair<int, int> >, greater<pair<int, int> > > q[MAXN];
pair<int, int> head[MAXN];

bool check() {
	int l = -1, r = INFTY;
	for (int i = 1; i <= N; ++i)
		l = max(l, head[i].first), r = min(r, head[i].second);
	return l <= r;
}

bool discard() {
	pair<int, int> p = head[1];
	int choice = 1;
	for (int i = 2; i <= N; ++i)
		if (head[i] < p)
			p = head[choice = i];
	if (q[choice].empty()) return true;
	head[choice] = q[choice].top(), q[choice].pop();
	return false;
}

int solve() {
	int Q, ans = 0;
	for (int i = 1; i <= N; ++i)
		while (!q[i].empty()) q[i].pop();
	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= P; ++j) {
			scanf("%d", &Q);
			int l = ceil(Q / (R[i] * 1.1)), r = floor(Q / (R[i] * 0.9));
			l = max(l, 1);
			if (l <= r) q[i].push(make_pair(l, r));
		}
	for (int i = 1; i <= N; ++i) {
		if (q[i].empty()) return 0;
		head[i] = q[i].top(), q[i].pop();
	}
	bool finish = false;
	while (!finish) {
		if (check()) {
			++ans;
			for (int i = 1; i <= N; ++i) {
				if (q[i].empty()) {
					finish = true;
					break;
				}
				else
					head[i] = q[i].top(), q[i].pop();
			}
		}
		else
			finish = discard();
	}
	return ans;
}

int main() {
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		scanf("%d%d", &N, &P);
		for (int i = 1; i <= N; ++i)
			scanf("%d", &R[i]);
		printf("Case #%d: %d\n", t, solve());
	}
	return 0;
}
