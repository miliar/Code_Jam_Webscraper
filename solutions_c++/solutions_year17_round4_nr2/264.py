#include <bits/stdc++.h>
using namespace std;

int Test, N, C, M, res;
int du[2010];

bool check(int p){
	int remain = 0;
	res = 0;
	for (int i = 1; i <= N; i++)
		if (du[i] <= p)
			remain += p - du[i];
		else{
			remain -= du[i] - p;
			res += du[i] - p;
			if (remain < 0) return 0;
		}
	return 1;
}

int main(){
//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);
	scanf("%d", &Test);
	for (int tt = 1; tt <= Test; tt++){
		scanf("%d%d%d", &N, &C, &M);
		memset(du, 0, sizeof(du));
		for (int i = 1; i <= M; i++){
			int x, y;
			scanf("%d%d", &x, &y);
			du[x]++;
			du[N + y]++;
		}
		int l = 0, r = 1000;
		for (int i = 1; i <= C; i++)
			l = max(l, du[N + i]);
		while (l < r){
			int mid = (l + r) >> 1;
			if (check(mid)) r = mid;
			else l = mid + 1;
		}
		res = 0;
		check(l);
		printf("Case #%d: %d %d\n", tt, l, res);
	}
}
