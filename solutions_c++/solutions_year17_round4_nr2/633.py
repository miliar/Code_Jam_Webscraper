#include <bits/stdc++.h>

using namespace std;

const int N = 1e3 + 7;
const int INF = 1e9 + 7;

int n, m, c;
vector<pair<int, int>> tick;
int visit[N][N];

int got(int num) {
	vector<int> seats(num, n);
	for (int i = 1; i <= c; i++) {
		for (int j = 0; j < num; j++) {
			visit[i][j] = false;
		}
	}
	int ret = 0;
	for (auto t : tick) {
		int pos = t.first, who = t.second;
		cout << " pos = " << pos << " who = " << who << endl;
		int which = -1, back = 0;
		for (int i = 0; i < num; i++) {
			if (visit[who][i]) continue;
			seats[i] = min(seats[i], pos);
			if (seats[i] > back) {
				back = seats[i];
				which = i;
			}
		}
		if (which == -1) return INF;
		seats[which]--;
		visit[who][which] = true;
		if (back != pos) ++ret;
	}
	return ret;
}

int cnt[N], s[N];

pair<int, int> solve() {
	scanf("%d %d %d", &n, &c, &m);
	for (int i = 0; i <= c; i++) cnt[i] = 0;
	for (int i = 0; i <= n; i++) s[i] = 0;
	tick.clear();
	int first = 0, second = 0;
	for (int i = 0; i < m; i++) {
		int pos, who;
		scanf("%d %d", &pos, &who);
		tick.push_back({pos, who});
		first = max(first, ++cnt[who]);
		s[pos]++;
	}
	int ss = 0;
	for (int i = 1; i <= n; i++) {
		ss += s[i];
		first = max(first, (ss + i - 1) / i);
	}
	for (int i = 1; i <= n; i++) {
		second += max(0, s[i] - first);
	}
	return {first, second};
}

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		static int testCount = 0;
		auto w = solve();
		printf("Case #%d: %d %d\n", ++testCount, w.first, w.second);
	}
	return 0;
}
