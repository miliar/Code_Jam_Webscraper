#include <bits/stdc++.h>

using namespace std;
using ll = long long;
constexpr int MAXN = 1005;

//int g [MAXN][MAXN];
int n, r, o, y, gr, b, v;
int data [64];
int ans [1005];
char ch [10];

inline int is_best(int cur, int fst, int a, int b) {
	if (a == (fst >> 1 << 1)) {
		if (data[a]) return a;
		else return b;
	}
	if (b == (fst >> 1 << 1)) {
		if (data[b]) return b;
		else return a;
	}

	if (data[a] > data[b]) {
		return a;
	}
	return b;
}

int dfs(int cur, int remaining, int fst) {
	ans[remaining] = cur;
	data[cur]--;
	if (remaining == 1) return 1;
	if (cur & 1) {
		if (data[cur^1]) {
			return dfs(cur^1, remaining-1, fst);
		}
		return 0;
	} else {
		if (data[cur|1]) {
			return dfs(cur|1, remaining-1, fst);
		} else {
			int best = 0;
			if (cur == 2) best = is_best(cur, fst, 4, 8);
			if (cur == 4) best = is_best(cur, fst, 2, 8);
			if (cur == 8) best = is_best(cur, fst, 2, 4);
			if (best[data]) return dfs(best, remaining-1, fst);
			return 0;
		}
	}
}

string solve() {
	scanf("%d%d%d%d%d%d%d", &n, &r, &o, &y, &gr, &b, &v);

	ch[0] = '#';
	ch[2] = 'R';
	ch[3] = 'G';
	ch[4] = 'B';
	ch[5] = 'O';
	ch[8] = 'Y';
	ch[9] = 'V';

	data[2] = r;
	data[4] = b;
	data[8] = y;

	data[2|1] = gr;
	data[4|1] = o;
	data[8|1] = v;

	int res = 0;

	for (int i = 0; i < 10; i++) {
		if (data[i]) {
			int in_res = dfs(i, n, i);
			if (!in_res) {
				// pass
			} else if (ans[1] == ans[n]) {
				// pass
			} else if ((ans[1] & 1) && (ans[1] ^ 1) != ans[n]) {
				// pass
			} else if ((ans[n] & 1) && (ans[n] ^ 1) != ans[i]) {
				// pass
			} else {
				res = 1;
				break;
			}
		}

		data[2] = r;
		data[4] = b;
		data[8] = y;

		data[2|1] = gr;
		data[4|1] = o;
		data[8|1] = v;
	}

	if (!res) return "-1";

	string rr;

	for (int i = n; i > 0; i--) {
		rr += ch[ans[i]];
	}

	return rr;
}

void report(int i, const string &ans) {
	printf("Case #%d: %s\n", i, (ans == "-1" ? "IMPOSSIBLE" : ans.c_str()));
}

int main(void) {
	int t;
	scanf("%d", &t);

	for (int i = 0; i < t; i++) {
		auto ans = solve();
		report(i+1, ans);
	}

	return 0;
}