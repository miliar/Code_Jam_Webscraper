#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstring>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

vector<int> G[1010];

vector<int> ta;
vector<int> tb;

int P[1010];
int X[1010];
int tm = 0;

bool find(int pos) {
	if (X[pos] == tm) {
		return false;
	}
	X[pos] = tm;
	for (int i = 0; i < (int)G[pos].size(); ++i) {
		int nxt = G[pos][i];
		if (P[nxt] == -1 || find(P[nxt])) {
			P[nxt] = pos;
			return true;
		}
	}
	return false;
}

void solve() {
	int N, C, M;
	scanf("%d%d%d", &N, &C, &M);
	ta.clear();
	tb.clear();
	for (int i = 0; i < M; ++i) {
		G[i].clear();
		P[i] = -1;
	}
	for (int i = 0; i < M; ++i) {
		int pos, b;
		scanf("%d%d", &pos, &b);
		--pos;
		--b;
		if (b == 0) {
			ta.push_back(pos);
		}
		else {
			tb.push_back(pos);
		}
	}
	for (int i = 0; i < (int)ta.size(); ++i) {
		for (int j = 0; j < (int)tb.size(); ++j) {
			if (ta[i] != tb[j]) {
				G[i].push_back(j);
			}
		}
	}
	int ans = 0;
	for (int i = 0; i < (int)ta.size(); ++i) {
		++tm;
		if (find(i)) {
			ans += 1;
		}
	}
	int cnta = ta.size() - ans;
	int cntb = tb.size() - ans;
	if (cnta == 0 && cntb == 0) {
		printf("%d 0\n", ans);
		return;
	}
	int val = -1;
	for (int i = 0; i < tb.size(); ++i) {
		if (P[i] == -1) {
			val = tb[i];
			break;
		}
	}
	if (val == 0) {
		ans += cnta + cntb;
		printf("%d 0\n", ans);
	}
	else {
		printf("%d %d\n", ans + max(cnta, cntb), min(cnta, cntb));
	}
}

int main() {
	freopen("bin.txt", "r", stdin);
	freopen("bout.txt", "w", stdout);

	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		fprintf(stderr, "%d\n", i + 1);
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}