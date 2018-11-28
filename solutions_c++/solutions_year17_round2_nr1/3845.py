#include<stdio.h>
#include<conio.h>

int main(){
	int testcases;
	int d,n;
//	float time;
//	float maxspeed;
	scanf("%d",&testcases);
	for(int i=1;i<=testcases;i++){
		scanf("%d",&d);
		scanf("%d",&n);
		float count=0;
		for(int i=0;i<n;i++){
			int ki;
			int si;
			scanf("%d",&ki);
			scanf("%d",&si);
			float l=(float)(d-ki)/si;
			if(l>count){
				count=l;
			}
		}
		printf("Case #%d: %f\n",i,d/count);
	}
	return 0;
}
