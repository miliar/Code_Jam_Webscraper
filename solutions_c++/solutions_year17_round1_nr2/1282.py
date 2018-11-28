#include <bits/stdc++.h>
using namespace std;

#define F first
#define S second
#define INF 0x3f3f3f3f
#define eps 1e-9

int a[55] , b[55][55];
pair<int , int> p[55][55];

bool cmp(pair<int , int> p , pair<int , int> p2) {
	return p.S == p2.S ? p.F < p2.F : p.S < p2.S;
}

int main() {
	int t , kase = 0;
	scanf("%d" , &t);
	for( ; t--; ) {
		int n , m;
		vector<int> v;
		scanf("%d%d" , &n , &m);
		for(int i = 0; i < n; i++) {
			scanf("%d" , &a[i]);
		}
		for(int i = 0; i < n; i++) {
			for(int j = 0; j < m; j++) {
				scanf("%d" , &b[j][i]);
				p[i][j].F = ceil(b[j][i] / (1.1 * a[i]));
				p[i][j].S = floor(b[j][i] / (0.9 * a[i]));
				v.push_back(p[i][j].F);
				v.push_back(p[i][j].S);
			}
		}

		for(int i = 0; i < n; i++) {
			sort(p[i] , p[i] + m , cmp);
		}
		sort(v.begin() , v.end());

		int ans = 0;
		for(int i = 0; i < v.size(); i++) {
			int u = v[i] , ook = 1;
			vector<int> G;
			for(int j = 0; j < n; j++) {
				int ok = 0;
				for(int k = 0; k < m && !ok; k++) {
					if(p[j][k].F != -1 && u >= p[j][k].F && u <= p[j][k].S) {
						ok = 1;
						G.push_back(k);
					}
				}

				if(ok == 0) {
					ook = 0;
					break;
				}
			}

			if(ook) {
				ans++;
				for(int i = 0; i < n; i++) {
					p[i][G[i]].F = -1;
				}
			}
		}

		printf("Case #%d: %d\n" , ++kase , ans);
	}
	return 0;
}