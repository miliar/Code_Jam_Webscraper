#include <bits/stdc++.h>
#define SZ(v) ((int)(v).size())

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<int, ll> pil;

int n, m;

struct tmp {
	int x, y, b;
} a[103];

bool cmp(tmp &t1, tmp &t2){
	return t1.x < t2.x;
}

int main(){
	int T;
	scanf("%d", &T);
	for (int t=1; t<=T; t++){
		scanf("%d%d", &n, &m);
		int ans = 0;
		int nt = 0, mt = 0;
		for (int i=0; i<n; i++){
			int u, v;
			scanf("%d%d", &u, &v);
			a[i] = {u, v, 0};
			nt += (v - u);
		}
		for (int i=0; i<m; i++){
			int u, v;
			scanf("%d%d", &u, &v);
			a[i+n] = {u, v, 1};
			mt += (v - u);
		}
		if (n+m == 1){
			printf("Case %d: 2\n", t);
			continue;
		}
		sort(a, a+n+m, cmp);
		vector<int> na, nb;
		for (int i=0; i<n+m-1; i++){
			if (a[i].b == a[i+1].b){
				ans += 2;
				if (a[i].b == 0){
					na.push_back(a[i+1].x - a[i].y);
				}
				else {
					nb.push_back(a[i+1].x - a[i].y);
				}
			}
			else ans ++;
		}
		if (a[0].b == a[n+m-1].b){
			ans += 2;
			if (a[0].b == 0){
				na.push_back(a[0].x + 1440 - a[n+m-1].y);
			}
			else {
				nb.push_back(a[0].x + 1440 - a[n+m-1].y);
			}
		}
		else ans ++;
		sort(na.begin(), na.end());
		sort(nb.begin(), nb.end());
		for (int i=0; i<SZ(na); i++){
			if (nt + na[i] > 720) break;
			nt += na[i];
			ans -= 2;
		}
		for (int i=0; i<SZ(nb); i++){
			if (mt + nb[i] > 720) break;
			mt += nb[i];
			ans -= 2;
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}