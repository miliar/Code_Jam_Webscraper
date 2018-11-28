#include<bits/stdc++.h>
using namespace std;
#define pb push_back
#define mkp make_pair
#define fi first
#define se second
#define ll long long
#define all(a) a.begin(), a.end()

int N, C, M;
int p[1010], c[1010];
int cnt[1010], a[1010];
int ans;

bool check(int d){
	int re = 0; ans = 0;
	for(int i = N; i >= 1; --i){
		int t = min(d, a[i]);
		ans += a[i] - t;
		re += a[i] - t;
		re -= min(re, d - t);
	}
	return re == 0;
}

int main(){
	freopen("B-large.in", "r", stdin);
	freopen("x.out", "w", stdout);
	int T, ca = 0;
	scanf("%d", &T);
	while(T--){
		printf("Case #%d: ", ++ca);
		scanf("%d%d%d", &N, &C, &M);
		memset(a, 0, sizeof(a));
		memset(cnt, 0, sizeof(cnt));
		int l = 0, r = M; ans = 0;
		for(int i = 1; i <= M; ++i){
			scanf("%d%d", p + i, c + i);
			a[p[i]]++;
			cnt[c[i]]++;
			l = max(l, cnt[c[i]] - 1);
		}
		while(l + 1 < r){
			int d = (l + r + 1) / 2;
			if(check(d)) r = d;
			else l = d;
		}
		check(r);
		printf("%d %d\n", r, ans);
	}
	return 0;
}
