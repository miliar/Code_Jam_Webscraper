#include <stdio.h>

long long list[1000];
long long quant[1000];
long long n,q;

int main(){
	int t;
	int ini,fim=-1;
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		
		for(int i=0;i<=fim;i++) list[i]=quant[i]=0;
		ini=fim=0;
		
		scanf("%lld %lld",&n,&q);
		list[0]=n;
		quant[0]=1;
		for( ;quant[ini]>0;ini++){
			long long add1=list[ini]/2,add2=(list[ini]-1)/2;
			if(list[fim]!=add1){
				fim++;
				list[fim]=add1;
			}
			quant[fim]+=quant[ini];
			if(list[fim]!=add2){
				fim++;
				list[fim]=add2;
			}
			quant[fim]+=quant[ini];
		}
//		for(int i=0;i<fim;i++) printf("%lld %lld\n",list[i],quant[i]);
		for(int i=0;q>0;i++){
			if(q<=quant[i]){
				printf("Case #%d: %lld %lld\n",tt,list[i]/2,(list[i]-1)/2);
			}
			q-=quant[i];
		}
	}
	return 0;
}
