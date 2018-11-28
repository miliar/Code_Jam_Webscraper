#include <bits/stdc++.h>

using namespace std;
int t,n,tc=0;
double d, ans;
int main(){
	scanf("%d",&t);
	while(t--){
		ans=0.0;
		scanf("%lf%d",&d,&n);
	    double _max=0.0;
		for (int i=0;i<n;i++){
			double u,v;
			scanf("%lf%lf",&u,&v);
			_max=max(_max,(d-u)/v);
		}
		ans=d/_max;
		printf("Case #%d: %lf\n",++tc,ans);
	}
	return 0;
}
