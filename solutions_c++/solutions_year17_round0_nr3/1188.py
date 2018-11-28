#include<iostream>
#include<cstdio>
using namespace std;
int main(){
	int T,I;
	cin>>T;
	for(I=1;I<=T;I++){
		long long n,k;
		long long a,b=0,na=1,nb=0;
		long long nexta,nextb,nextna,nextnb;
		cin>>n>>k;
		a=n;
		printf("Case #%d: ",I);
		if(k==1){
			if(n%2==0){
				printf("%lld %lld\n",n/2,n/2-1);
			}
			else{
				printf("%lld %lld\n",n/2,n/2);
			}
			continue;
		}
		long long now=1;
		while(k > now*2-1){
			nextna=nextnb=0;
			nexta=a/2;
			nextb=a/2-1;
			nextna+=na;
			if(a%2==0){
				nextnb+=na;
			}
			else{
				nextna+=na;
			}
			nextnb+=nb;
			if(b%2==0){
				nextna+=nb;
			}
			else{
				nextnb+=nb;
			}
			//printf("%lld: %lld , %lld: %lld\n",nexta,nextna,nextb,nextnb);
			a=nexta;
			b=nextb;
			na=nextna;
			nb=nextnb;
			now=now*2;
		}
		//printf("\n%lld %lld %lld %lld %lld %lld %lld\n",n,k,now,a,na,b,nb);
		long long t;
		if(k-now+1 <= na)t=a;
		else t=b;
		if(t%2==0)printf("%lld %lld\n",t/2,t/2-1);
		else printf("%lld %lld\n",t/2,t/2);
	}
	return 0;
}