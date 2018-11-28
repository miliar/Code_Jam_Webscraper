#include<bits/stdc++.h>
#define LIM 1050
using namespace std;

int n , m , c , peo[LIM] , pos[LIM] , cur , change;

bool ok(int x){
	long long tmp = 0 , req = 0;
	change = 0;
	for(int i = 1 ; i <= n ; i++){
		tmp += x;
		req += pos[i];
		if(req > tmp)	return false;
		change += (pos[i] > x ? pos[i] - x : 0);
	}
	return true;
}


void solve(int Tc){
	scanf("%d %d %d",&n,&c,&m);
	memset(peo , 0 , sizeof peo);
	memset(pos , 0 , sizeof pos);
	cur = 0;
	for(int i = 1 ; i <= m ; i++){
		int p, b;
		scanf("%d %d",&p,&b);
		peo[b]++;
		pos[p]++;
		cur = max(cur , peo[b]);
	}
	cur = max(cur , m / min(n , c) + (m % min(n , c) != 0));
	int ll = cur , rr = m;
	while(ll < rr){
		int mid = (ll + rr)/2;
		if(ok(mid))	rr = mid;
		else ll = mid + 1;
	}
	int xxx = ok(ll);
	printf("Case #%d: %d %d\n",Tc,ll,change);
}

int main(){
	freopen("test.inp","r",stdin);
	freopen("test.out","w",stdout);
	int Tc;
	scanf("%d",&Tc);
	for(int i = 1 ; i <= Tc ; i++) solve(i);
}



