#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
#define min(a,b) (a<b?a:b)
#define max(a,b) (a>b?a:b)
int main() {
	int t,test;
	scanf("%d",&t);
	for(test=1;test<=t;test++){
		int i,n;
		double d,ans = 0;
		scanf("%lf%d",&d,&n);
		for(i=0;i<n;i++){
			double k,s;
			scanf("%lf%lf",&k,&s);
			double time = (d-k)/s;
			ans = max(ans, time);
		}
		printf("Case #%d: %0.6lf\n",test,d/ans);
	}
	return 0;
}