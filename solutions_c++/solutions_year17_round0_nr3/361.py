#include <map>
#include <cstdio>
#include <cstring>
#include <iostream>

#define MaxN 10010

using namespace std;

int T;
long long n, k;
map<long long, long long> cnt;
int qtail, qhead;
long long que[MaxN];

bool cmp(long long a, long long b) {
	return a > b;
}

void Inque(long long ind, long long dt) {
	if (cnt[ind] == 0)
		que[++qtail] = ind;
	cnt[ind] += dt;
}

void bfs() {
	cnt.clear();
	qhead = qtail = 0;
	que[qtail] = n;
	cnt[n] = 1;
	for ( ; qhead <= qtail; ++qhead) {
		sort(que + qhead, que + qtail + 1, cmp);
		long long now = que[qhead];
		if (now & 1) {
			Inque(now >> 1LL, cnt[now] * 2LL);
		}
		else {
			Inque(now >> 1LL, cnt[now]);
			Inque((now - 1) >> 1LL, cnt[now]);
		}
	}
	sort(que, que + qtail + 1, cmp);
	for (int i = 0; i <= qtail; ++i) {
		k -= cnt[que[i]];
		if (k <= 0) {
			cout << (que[i] >> 1LL) << " " << ((que[i] - 1) >> 1LL) << endl;
			return;
		}
	}
}

int main() {
	scanf("%d", &T);
	int T0 = 0;
	for ( ; T; --T) {
		cin >> n >> k;
		printf("Case #%d: ", ++T0);
		bfs();
	}
	return 0;
}