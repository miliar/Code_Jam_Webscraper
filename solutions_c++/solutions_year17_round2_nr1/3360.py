#include <stdio.h>
using namespace std;
int main(){
	int t,D,N,K,S;
	double max=0, tmp, tmp2;
	scanf("%d",&t);
	for(int i=1;i<=t;i++){
		scanf("%d %d",&D,&N);
		max=0;
		for(int j=0;j<N;j++){
			scanf("%d %d",&K,&S);
			tmp=D-K;
			tmp2=S;
			tmp=tmp/tmp2;
			if(tmp>max)max=tmp;
		}
		tmp=D;
		tmp=tmp/max;
		printf("Case #%d: %.6lf\n",i,tmp);
	}
	return 0;
}