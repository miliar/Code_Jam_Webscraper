#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
struct horse{
	int k,s;
};

int main(){
	int T,I;
	scanf("%d",&T);
	for(I=1;I<=T;I++){
		int d,n,i,j;
		horse h[1005];
		scanf("%d %d",&d,&n);
		for(i=0;i<n;i++){
			scanf("%d %d",&h[i].k,&h[i].s);
		}
		double max=-1.0;
		for(i=0;i<n;i++){
			double time=1.0*(d-h[i].k)/h[i].s;
			if(time>max)max=time;
		}
		printf("Case #%d: ",I);
		printf("%lf\n",1.0*d/max);
	}
	return 0;
}