#include<iostream>
#include<algorithm>
#include<vector>
#include<cmath>
#include<string>
typedef long long ll;
using namespace std;
const int N = 25 + 5;
char g[N][N];
int r, c;
int main() {
#ifndef ONLINE_JUDGE
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int t;
	scanf("%d", &t);
	for(int cas=1;cas<=t;++cas) {
		printf("Case #%d:\n", cas);
		scanf("%d%d", &r, &c);
		vector<pair<int, int> > p;
		for (int i = 0; i < r; ++i) {
			scanf("%s", g[i]);
			for (int j = 0; j < c; ++j)
				if (isalpha(g[i][j]))
					p.push_back({ i,j });
		}
		for (int k = 0; k < p.size(); ++k) {
			int i = p[k].first, j = p[k].second;
			int x1 = i, x2 = i, y1 = j, y2 = j;
			while (y1 > 0 && g[i][y1-1] == '?')
				g[i][--y1] = g[i][j];
			while (y2 + 1 < c && g[i][y2+1] == '?')
				g[i][++y2] = g[i][j];

			while (x1 > 0) {
				--x1;
				bool can = true;
				for (int t = y1; t <= y2 && can; ++t)
					if (g[x1][t] != '?') 
						can = false;
				if (!can) {
					++x1;
					break;
				}
				for (int t = y1; t <= y2 && can; ++t)
					g[x1][t] = g[i][j];

			}
			while (x2+1 <r) {
				++x2;
				bool can = true;
				for (int t = y1; t <= y2 && can; ++t)
					if (g[x2][t] != '?')
						can = false;
				if (!can) {
					--x2;
					break;
				}
				for (int t = y1; t <= y2 && can; ++t)
					g[x2][t] = g[i][j];
			}

		}

		for (int i = 0; i < r; ++i)
			printf("%s\n", g[i]);


	}


	return 0;
}
