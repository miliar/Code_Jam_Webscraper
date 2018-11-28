#include <bits/stdc++.h>
using namespace std;
const int N = 30;
char s[N][N];
int main() {
	int T, zzz = 0;
	scanf("%d", &T);
	while (T --) {
		int n, m;
		scanf("%d%d", &n, &m);
		vector<pair<int, int>> all;
		for (int i = 0; i < n; ++ i) {
			scanf("%s", s[i]);
			for (int j = 0; j < m; ++ j) if (s[i][j] != '?') all.push_back({i, j});
		}
		sort(all.begin(), all.end());
		for (int i = 0; i < (int) all.size(); ++ i) {
			auto x = all[i];
			int h = 1;
			while (x.first - h >= 0 && s[x.first - h][x.second] == '?') h ++;
			int w = 1;
			while (x.second - w >= 0 && s[x.first][x.second - w] == '?') w ++;
			for (int i = 0; i < h; ++ i) {
				for (int j = 0; j < w; ++ j) {
					s[x.first - i][x.second - j] = s[x.first][x.second];
				}
			}
			if (i == (int) all.size() - 1 || all[i + 1].first != all[i].first) {
				for (int i = 0; i < h; ++ i) {
					for (int j = x.second + 1; j < m; ++ j) {
						s[x.first - i][j] = s[x.first][x.second];
					}
				}
			}
		}
		for (int i = 0; i < n; ++ i) {
			for (int j = 0; j < m; ++ j) if (s[i][j] == '?') {
				s[i][j] = s[i - 1][j]; // else s[i][j] = s[i - 1][j];
			}
		}
		printf("Case #%d:\n", ++ zzz);
		for (int i = 0; i < n; ++ i) puts(s[i]);
	}
}

