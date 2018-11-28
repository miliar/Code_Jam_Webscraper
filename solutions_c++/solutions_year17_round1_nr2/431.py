#include <bits/stdc++.h>
using namespace std;

const int dx[5] = {1, -1, 0, 0};
const int dy[5] = {0, 0, 1, -1};
const int maxn = 55;
int n, m;
int ret;

int main() {
	freopen("in", "r", stdin);
	freopen("out", "w", stdout);
	int T, _ = 1;
	scanf("%d", &T);
	while(T--) {
		scanf("%d%d",&n,&m);
		vector<vector<int>> b(n, vector<int>(m));
		vector<int> a(n);
		for(int i = 0; i < n; i++) scanf("%d", &a[i]);
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) scanf("%d", &b[i][j]);
			sort(b[i].begin(), b[i].end());
		}
		ret = 0;
		vector<int> h(n, 0);
		for(int z = 0; ; z++) {
			int flag = 1;
			for(int i = 0; i < n; i++) {
				while(h[i] < m && b[i][h[i]] * 10 < a[i] * z * 9) h[i]++;
				if(h[i] == m) {
					flag = -1;
					break;
				}
				if(b[i][h[i]] * 10 > a[i] * z * 11) {
					flag = 0;
					break;
				}
			}
			if(flag == -1) break;
			if(flag == 1) {
				ret++;
				for(auto& x : h) x++;
				z--;
			}
		}
		printf("Case #%d: %d\n", _++, ret);
	}
	return 0;
}

