#include <bits/stdc++.h>
#define int long long
using namespace std;
int n,k;
priority_queue<int> pq; 
int32_t main(){
	freopen("C-small-2.in","r",stdin); freopen("C.out","w",stdout);
	int t; scanf("%lld",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%lld %lld",&n,&k);
		pq.push(n);
		while (!pq.empty() && k>0){
			int cur=pq.top(); pq.pop();
			int l=(cur>>1)-(!(cur&1));
			int r=(cur>>1);
			pq.push(l);
			pq.push(r);
			if (k==1) printf("Case #%d: %lld %lld\n",tc,r,l);
			k--;
		}
		while (!pq.empty()) pq.pop();
	}
}
