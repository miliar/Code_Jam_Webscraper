#include <cstdio>
#include <cstring>

int t,d,n;

int main(){
	//freopen("A-large1.in","r",stdin);

	scanf("%d",&t);
	
	for(int tc=1; tc<=t; tc++){
		scanf("%d %d",&d,&n);

		double a,b;
		double max=0.0;
		for(int i=0; i<n; i++){
			scanf("%lf %lf",&a,&b);
			if(max < (d-a)/b) max = (d-a)/b;
		}
		
		printf("Case #%d: %0.6lf\n",tc,d/max);

	}

	return 0;
}