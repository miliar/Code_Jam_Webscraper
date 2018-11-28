#include <iostream>
#include <cstdio>
#include <string>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <sstream>
#include <cstring>
#include <set>
using namespace std;
long long n,k;
int main() {
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++) {
		scanf("%lld",&n);
		scanf("%lld",&k);
		priority_queue<long long> q;
		q.push(n-1);
		long long ans1,ans2,temp;
		for(long long j=1;j<=k;j++) {
			temp = q.top();
			q.pop();
			ans2 = temp/2;
			ans1 = temp - ans2;
			if(ans1>=1)
				q.push(ans1-1);
			if(ans2>=1)
				q.push(ans2-1);
		}
		printf("Case #%d: %lld %lld\n",i,ans1,ans2);
	}
	return 0;
}