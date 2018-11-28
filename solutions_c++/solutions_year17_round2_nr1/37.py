#include<bits/stdc++.h>
using namespace std;
double d;int n;
int main(){
	int _,t;
	scanf("%d",&_);
	for(t=1; t<=_; t++){
		scanf("%lf%d",&d,&n);
		double T = 0;
		for(int i=0; i<n; i++){
			double x,y;
			scanf("%lf%lf",&x,&y);
			T = max(T, (d-x)/y);
		}
//		printf("%lf\n",d);
		printf("Case #%d: %lf\n",t,d/T);
	}
	return 0;
}
