#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define f(i, x, n) for(int i = x; i < (int)(n); ++i)

int main(){
	freopen("main.in", "r", stdin);
	freopen("main.out", "w", stdout);
	int t;
	scanf("%d", &t);
	f(tc, 1, t + 1){
		printf("Case #%d: ", tc);
		int n, p;
		scanf("%d%d", &n, &p);
		int fr[4] = { 0 };
		f(i, 0, n){
			int t;
			scanf("%d", &t);
			++fr[t % p];
		}
		int an = fr[0];
		if (p == 2)an += fr[1] + 1 >> 1;
		else if (p == 3){
			int mn = min(fr[1], fr[2]), mx = max(fr[1], fr[2]);
			an += mn + (mx - mn + 2) / 3;
		}else {
			int mn = min(fr[1], fr[3]), mx = max(fr[1], fr[3]);
			an += fr[2] >> 1;
			if (fr[2] & 1)++mn, --mx;
			an += mn + (mx - mn + 3) / 4;
		}
		printf("%d\n", an);
	}
}