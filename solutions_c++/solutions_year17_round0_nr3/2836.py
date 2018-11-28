#include <stdio.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <map>

using namespace std;
typedef long long LL;
typedef pair<LL,LL> PLL;

int INT(){int x;scanf("%d",&x);return x;}

PLL solve(LL n, LL k) {
	map<LL,LL> m;
	m[-n]=1;

	while(1){
		auto b = m.begin();
		LL sz = -b->first; sz-=1;
		LL cnt = b->second;
		if (cnt >= k) return PLL(sz/2,sz-(sz/2));
		LL x = sz/2;
		LL y = sz-x;
		m[-x]+=cnt;m[-y]+=cnt;
		m.erase(b);
		k-=cnt;
	}
	return PLL(-1,-1);
}

int main() {
	int T=INT();

	for(int t=1;t<=T;++t){
		LL n, k;
		cin>>n>>k;
		printf("Case #%d: ", t);
		PLL soln = solve(n,k);
		cout << soln.second << " " << soln.first << "\n";
	}
	return 0;
}
