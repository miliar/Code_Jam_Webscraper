#include <bits/stdc++.h>
using namespace std;
const int MAXN = 1005;
typedef long long int LL;

struct Horses{
	int pos, spd;
	inline bool operator < (const Horses &rhs) const{
		return pos < rhs.pos;
	}
}h[MAXN];
int d, n;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("test.out", "w", stdout);
	int testcase, i, kase = 0, slow;
	scanf("%d", &testcase);
	while(testcase --){
		scanf("%d%d", &d, &n);
		for(i = 1; i <= n; ++ i)
			scanf("%d%d", &h[i].pos, &h[i].spd);
		sort(h + 1, h + 1 + n);
		for(i = n - 1, slow = n; i; -- i){
			if(h[i].spd <= h[slow].spd) slow = i;
			else if(LL(d - h[i].pos) * h[slow].spd >= LL(d - h[slow].pos) * h[i].spd) slow = i;
		} printf("Case #%d: %.10lf\n", ++ kase, 1.0 * d * h[slow].spd / (d - h[slow].pos));
	}
	return 0;
}
