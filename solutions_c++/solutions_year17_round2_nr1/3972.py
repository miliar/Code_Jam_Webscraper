#include<stdio.h>
#include<stdlib.h>
#define ll long long 
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int xx=1;xx<=T;xx++){
		int D,n;
		scanf("%d%d",&D,&n);
		ll sp,st;
		scanf("%lld%lld",&st,&sp);
		for(int i=1;i<n;i++){
			ll a,b;//a start
			scanf("%lld%lld",&a,&b);
			if((D-st)*b < (D-a)*sp){
				st = a;
				sp = b;
			} 
		}
		printf("Case #%d: %.6f\n",xx,(double)D*sp/(D-st));
		//system("pause");
	}
	return 0;
}
