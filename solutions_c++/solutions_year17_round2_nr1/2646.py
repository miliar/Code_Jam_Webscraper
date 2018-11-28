#include<stdio.h>

int main(){

	int t,n,m,x,y,i;
	double max;
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d %d",&n,&m);
		max=0;
		while(m--){
			scanf("%d %d",&x,&y);
			if(max<(double)(n-x)/y)
				max=(double)(n-x)/y;
		}
		printf("Case #%d: %lf\n",i,n/max);
	}
	return 0;
}