#include <cstdio>
#include <vector>
#include <unordered_map>
#include <queue>
#include <algorithm>
using namespace std;

int hd, ad, hk, ak, bb, dd;
unordered_map<long long, int> cache, visit;

inline long long makekey(int a, int b, int c, int d) {
	return ((a * 401ll + b) * 401ll + c) * 401ll + d;
}

const int INF = 0x7ffffff0;
int ans;

void gogo() {
	ans = INF;
	long long initkey = makekey(hd, hk, 0, 0);
	visit[initkey] = 0;
	queue<long long> q;
	q.push(initkey);
	while (!q.empty()) {
		long long k = q.front();
		q.pop();

		long long tk = k;
		int curseStack = tk % 401ll;
		tk /= 401ll;
		int attackStack = tk % 401ll;
		tk /= 401ll;
		int b = tk % 401ll;
		tk /= 401ll;
		int a = tk % 401ll;
		tk /= 401ll;

		//// Attack
		{
			int nxtb = b - (ad + attackStack);
			if (nxtb <= 0) ans = min(ans, visit[k] + 1);
			int nxta = a - max(ak - curseStack, 0);
			if (nxta > 0 && nxtb > 0) {
				long long nxtkey = makekey(nxta, nxtb, attackStack, curseStack);
				if (visit.count(nxtkey) == 0) {
					visit[nxtkey] = visit[k] + 1;
					q.push(nxtkey);
				}
			}
		}
		//// Buff
		if (attackStack < hk && bb > 0) {
			int nxtAttackStack = attackStack + bb;
			int nxta = a - max(ak - curseStack, 0);
			if (nxta > 0) {
				long long nxtkey = makekey(nxta, b, nxtAttackStack, curseStack);
				if (visit.count(nxtkey) == 0) {
					visit[nxtkey] = visit[k] + 1;
					q.push(nxtkey);
				}
			}
		}
		//// Cure
		{
			int nxta = hd - max(ak - curseStack, 0);
			if (nxta > 0) {
				long long nxtkey = makekey(nxta, b, attackStack, curseStack);
				if (visit.count(nxtkey) == 0) {
					visit[nxtkey] = visit[k] + 1;
					q.push(nxtkey);
				}
			}
		}
		//// Debuff
		if (curseStack < ak && dd > 0) {
			int nxtCurseStack = curseStack + dd;
			int nxta = a - max(ak - nxtCurseStack, 0);
			if (nxta > 0) {
				long long nxtkey = makekey(nxta, b, attackStack, nxtCurseStack);
				if (visit.count(nxtkey) == 0) {
					visit[nxtkey] = visit[k] + 1;
					q.push(nxtkey);
				}
			}
		}

	}

}

void proc(int caseidx) {
	cache.clear();
	visit.clear();
	scanf("%d %d %d %d %d %d", &hd, &ad, &hk, &ak, &bb, &dd);
	printf("Case #%d: ", caseidx);
	gogo();
	if (ans >= INF) {
		printf("IMPOSSIBLE\n");
	}
	else {
		printf("%d\n", ans);
	}
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		fprintf(stderr, "%d ", i);
		proc(i);
	}
	return 0;
}