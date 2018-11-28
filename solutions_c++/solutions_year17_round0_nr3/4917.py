#include <stdio.h>
#include <algorithm>
#include <queue>
#define FOR(i,n) for(int (i)=0; (i)<(n); (i)++)
#define SD(x) scanf("%d", &x); 
#define SDD(x,y) scanf("%d %d", &x, &y);
#define W first
#define LO second.first
#define HI second.second
using namespace std;
typedef unsigned long long llu;
typedef pair<llu, llu> pdd;
typedef pair<llu, pdd> tdd;
int lsb(llu x){
	int ans = 0;
	while(! (x&1)){
		x /= 2;
		ans++;
	}
	return ans;
}
int msb(llu x){
	int ans = 0;
	while(x){
		x /= 2;
		ans++;
	}
	return ans;
}
tdd solve(llu n, llu k){
	priority_queue<tdd> q;
	q.push(tdd(n, pdd(1, n+2)));
	FOR(i, k-1){
		tdd v = q.top(); q.pop();
		int mid = (v.LO + v.HI) / 2;
		q.push(tdd(mid - v.LO - 1, pdd(v.LO, mid)));
		q.push(tdd(v.HI - mid - 1, pdd(mid, v.HI)));
	}

	return q.top();
}
int main(){
	int t; SD(t);
	FOR(c, t){
		llu n, k;
		scanf("%llu %llu", &n, &k);
		tdd v = solve(n, k);
		llu mid = (v.LO + v.HI) / 2;
		llu ans1 = mid - v.LO - 1;
		llu ans2 = v.HI - mid - 1;
		printf("Case #%d: %llu %llu\n", c+1, max(ans1, ans2), min(ans1, ans2));
	}
}
