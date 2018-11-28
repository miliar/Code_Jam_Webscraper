#include <stdio.h>
#include <queue>
#include <algorithm>
#include <map>

typedef long long lli;

int main() {
	int test;
	scanf("%d", &test);
	for(int tc=1;tc<=test;tc++) {
		lli n,k;
		scanf("%lld %lld",&n,&k);

		std::map<lli, lli> m;
		m[n]+=1;

		lli sum=0;
		std::priority_queue<lli> que;
		que.push(n);
		while(!que.empty()) {
			lli now=que.top();que.pop();
			lli val=m[now],mx=now/2, mn=now/2-(now%2==0);
			if(sum+val>=k) {
				printf("Case #%d: %lld %lld\n",tc,mx,mn);
				break;
			}
			sum+=val;

			if(m[mx]==0) 
				que.push(mx);
			m[mx]+=val;

			if(m[mn]==0)
				que.push(mn);
			m[mn]+=val;
		}
	}
	return 0;
}