#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cmath>

using namespace std;

struct range {
	int l, m;
	range(int l = 0, int m = 0):l(l),m(m){}
};

range intact(range a, range b){
	int lm = max(a.l, b.l);
	int lM = min(a.m, b.m);
	return range(lm,lM);
}

int r[888];
range q[888][888];
int c[888];

bool cmp(const range&l, const range &r){
	return (l.l < r.l) || (l.l == r.l && l.m < r.m);
}

void work(){
	int n, p;
	scanf("%d%d", &n, &p);
	for (int i = 0; i < n; i++)
		scanf("%d", r + i);
	memset(c,0,sizeof(c));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < p; j++) {
			int x;
			scanf("%d", &x);

			double rough_less = x / (r[i]*0.9);
			double rough_upper = x / (r[i]*1.1);
			q[i][j].m = floor(rough_less);
			q[i][j].l = ceil(rough_upper);
			
		}
		sort(q[i], q[i] + p, cmp);
	}
	int cnt = 0;
	bool ended = false;
	while (!ended){
		bool pushed = false;
		while (!pushed) {
			for (int qx = max(1, q[0][c[0]].l); qx <= q[0][c[0]].m; qx++){
				bool push = true;
				for (int i = 1; i < n; i++)
					if (!(q[i][c[i]].l <= qx && qx <= q[i][c[i]].m))
						push = false;
				if (push) {
					pushed = true;
					break;
				}
			}
			if (pushed) break;
			else {
				int sm = 0x7fffffff, id = -1;
				for (int i = 0; i < n; i++){
					if (q[i][c[i]].m < sm){
						sm = q[i][c[i]].m;
						id = i;
					}
				}
				if (id == -1){
					ended = true;
					break;
				} else {
					c[id]++;
					if (c[id] >= p){
						ended = true; break;
					}
				}
			}
			if (ended) break;
		}
	//	puts("x");
		if (ended) break;
		if (q[0][c[0]].m != 0 && pushed) {
			cnt++;
		}
		for (int i = 0; i < n; i++)
			c[i]++;
		if (c[0] >= p)
			break;
	}
	printf("%d\n", cnt);
}

int main(){
	freopen("B.in", "r", stdin);
	int T; scanf("%d", &T);
	for (int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		work();
	}
}