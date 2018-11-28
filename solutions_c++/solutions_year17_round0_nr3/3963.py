#include <bits/stdc++.h>

using namespace std;

#define fi first
#define se second


void solve(){
	priority_queue<pair<int, pair<int, int> > > pq;
	
	int n, k;
	scanf("%d%d", &n, &k);
	pq.push({n, {-1, -n}});
	while(k--){
		int l = -pq.top().se.fi;
		int d = -pq.top().se.se;
		pq.pop();


		int mid = (l + d) / 2;
		int nalevo = (mid - 1) - l + 1;
		int nadesno = d - (mid + 1) + 1;

		//printf("%d %d: %d\n", l, d, mid);


		if(k == 0){
			printf("%d %d\n", max(nalevo, nadesno), min(nalevo, nadesno));
		}

		if(mid - 1 >= l)
			pq.push({nalevo, {-l, -(mid - 1)}});

		if(mid + 1 <= d)
			pq.push({nadesno, {-(mid + 1), -d}});
	}	
}

int main(){
	int t;
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		printf("Case #%d: ", i);
		solve();
	}
}