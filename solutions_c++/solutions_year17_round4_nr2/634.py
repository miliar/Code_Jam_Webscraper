#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int n, c, m, frc[1001], ds, lf[1001];
pair<int, int> cp[1000];

bool ok(int x){
	f(i, 1, n + 1)lf[i] = x;
	vector<int> bad;
	f(i, 0, m)if (lf[cp[i].first])--lf[cp[i].first];
	else bad.push_back(cp[i].first);
	sort(bad.begin(), bad.end());
	int j = 1;
	f(i, 0, bad.size()){
		while (j <= n && !lf[j])++j;
		if (j == n + 1)return false;
		if (bad[i] <= j)return false;
		--lf[j];
	}
	ds = bad.size();
	return true;
}

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		scanf("%d%d%d", &n, &c, &m);
		f(i, 1, c + 1)frc[i] = 0;
		int l = 0, r = m;
		f(i, 0, m)scanf("%d%d", &cp[i].first, &cp[i].second), l = max(l, ++frc[cp[i].second]);
		while (r > l){
			int m = l + r >> 1;
			if (ok(m))r = m;
			else l = m + 1;
		}
		ok(l);
		printf("%d %d\n", l, ds);
	}
}