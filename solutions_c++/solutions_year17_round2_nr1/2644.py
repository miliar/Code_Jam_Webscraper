#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int i,j,t,n,cnt,s,k, Case = 1;
	double ans,val=0;
	scanf("%d",&t);
	while(t--) {
		val = 0;
		scanf("%d%d",&n,&cnt);
		while(cnt--) {
			scanf("%d%d",&s,&k);
			val = max(val, ((n-s)*1.000000) / k );
		}
		ans = n/val;
		printf("Case #%d: %0.6lf\n", Case++, ans);
	}
	return 0; 
}
