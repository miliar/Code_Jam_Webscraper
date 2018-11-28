#include <stdio.h>
#include <algorithm>

using namespace std;

int main(){
	int T;
	scanf("%d",&T);
	for(int t = 1;t<=T;t++){
		double D;
		int N;
		scanf("%lf%d",&D,&N);
		double k;
		double m;
		double mt = 0;
		double tt;
		for(int i=0;i<N;i++){
			scanf("%lf%lf",&m,&k);
			tt = (D-m)/k;
			if (tt > mt)
				mt = tt;
		}
		printf("Case #%d: %.6lf\n",t,D/mt);
	}
	return 0;
}
