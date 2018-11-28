#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef long double Double;
char G[105][105];
bool E[2][205][205], used[205], bad[2][2][205];
int n, match[205], tt, ans;
char NG[105][105];
bool path(int x) {
	if (x == -1) return true;
	if (used[x]) return false;
	used[x] = true;
	for (int i = 0; i < n; ++i)
		if (!bad[tt][1][i] && E[tt][x][i] && path(match[i])) {
			match[i] = x;
			return true;
		}
	return false;
}
void getMaxMatching(int _n, int _tt) {
	n = _n;
	tt = _tt;
	memset(match, -1, sizeof(match));
	for (int i = 0; i < n; ++i) {
		if (bad[tt][0][i]) continue;
		memset(used, 0, sizeof(used));
		if (path(i)) ++ans;
	}
}
int main() {
	int TC;
	scanf("%d", &TC);
	for (int cn = 1; cn <= TC; ++cn) {
		int N, M;
		scanf("%d%d", &N, &M);
		memset(E, 0, sizeof(E));
		memset(bad, 0, sizeof(bad));
		memset(G, '.', sizeof(G));
		memset(NG, '.', sizeof(NG));
		ans = 0;
		for (int i = 0; i < M; ++i) {
			char ch;
			int r, c;
			scanf(" %c%d%d", &ch, &r, &c);
			G[r][c] = ch;
			if (ch == 'x' || ch == 'o') {
				bad[0][0][r - 1] = true;
				bad[0][1][c - 1] = true;
				++ans;
			}
			if (ch == '+' || ch == 'o') {
				bad[1][0][r + c - 2] = true;
				bad[1][1][r - c + N - 1] = true;
				++ans;
			}
		}
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j) {
				E[0][i - 1][j - 1] = true;
				E[1][i + j - 2][i - j + N - 1] = true;
			}
		getMaxMatching(N, 0);
		for (int i = 0; i < N; ++i)
			if (match[i] != -1) {
				NG[match[i] + 1][i + 1] = 'x';
			}	
		getMaxMatching(N + N - 1, 1);
		for (int i = 0; i < N + N - 1; ++i)
			if (match[i] != -1) {
				int r = (i + match[i] - N + 3) / 2;
				int c = match[i] - r + 2;
				NG[r][c] = NG[r][c] == 'x' ? 'o' : '+';
			}
		vector<pair<char, pair<int, int>>> outp;
		for (int i = 1; i <= N; ++i)
			for (int j = 1; j <= N; ++j)
				if (NG[i][j] != '.') {
					if (G[i][j] == '.') outp.push_back({NG[i][j], {i, j}});
					else outp.push_back({'o', {i, j}});
				}
		printf("Case #%d: %d %d\n", cn, ans, outp.size());
		for (auto x : outp)
			printf("%c %d %d\n", x.first, x.second.first, x.second.second);
	}
}
