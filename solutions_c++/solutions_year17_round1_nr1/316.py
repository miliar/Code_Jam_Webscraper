#include <bits/stdc++.h>
using namespace std;
#define ULL unsigned long long
#define LL long long
#define rep(i,n) for(int i = 0; i < n; ++i)
#define Rep(i,n) for(int i = 1; i <= n; ++i)

const int INF = 0x3f3f3f3f;

char s[31][31];

int main()
{
	int t, cas = 0;
	cin >> t;
	while(cas++ < t) {
		int n, m;
		cin >> n >> m;
		Rep(i, n) scanf("%s", s[i]+1);
		vector<pair<int, int>> c;
		Rep(i, n) Rep(j, m) if(s[i][j] >= 'A' && s[i][j] <= 'Z') {
			c.emplace_back(i, j);
		}
		int cur = 0;
		Rep(i, n) Rep(j, m) if(i == c[cur].first && j == c[cur].second) {
			++cur;
			int l = j, r = j;
			while(l > 1 && s[i][l-1] == '?') --l;
			while(r < m && s[i][r+1] == '?') ++r;
			int u = i, b = n;
			while(u > 1 && s[u-1][j] == '?') --u;
			for(int k = cur; k < c.size(); ++k) {
				if(c[k].first > i) { b = c[k].first-1; break; }
			}
			for(int ii = u; ii <= b; ++ii) {
				for(int jj = l; jj <= r; ++jj) {
					s[ii][jj] = s[i][j];
				}
			}
		}
		printf("Case #%d:\n", cas);
		Rep(i, n) puts(s[i]+1);
	}
	return 0;
}

