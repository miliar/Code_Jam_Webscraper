#include <bits/stdc++.h>

using namespace std;

int main(){
	int t,n,d,k,s;
	double vm;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		vm=DBL_MAX;
		scanf("%d %d",&d,&n);
		for(int j=0;j<n;j++){
			scanf("%d %d",&k,&s);
			vm=min(vm,(double)(s)/(double)(d-k)*(double)d);
		}
		printf("Case #%d: %.6f\n",i,vm);
	}
	return 0;
}