#include<stdio.h>
double com(double k,double s,double d){
	return (d-k)/s;
}
int main(){
	int T,t,d,n,i,k,s;
	double max;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%d%d",&d,&n);
		max = 0;
		for(i=0;i<n;i++){
			scanf("%d%d",&k,&s);
			if(com((double)k,(double)s,(double)d)>max)
				max = com((double)k,(double)s,(double)d);
		}
		printf("Case #%d: %.6lf\n",t,(double)d/max);
		
	}
}
