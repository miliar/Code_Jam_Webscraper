#include<stdio.h>
#include<stdlib.h>
long long ansx,ansy;
void DO(long long n,long long x,long long xn,long long y,long long yn){
	if(n<=xn){
		ansy = (x-1)/2;
		ansx = x-1-ansy;
		return;
	}
	n-=xn;
	if(n<=yn){
		ansy = (y-1)/2;
		ansx = y-1-ansy;
		return;
	}
	n-=yn;
	long long newx = x-1-(x-1)/2;
	long long newy = (y-1)/2;
	long long newxn = xn;
	long long newyn = yn;
	if((x-1)/2==newx)
		newxn+=xn;
	else
		newyn+=xn;
	if(y-1-(y-1)/2==newx)
		newxn+=yn;
	else
		newyn+=yn;
	DO(n,newx,newxn,newy,newyn);
}
int main(){
	int T,t;
	long long x,y;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		scanf("%lld%lld",&x,&y);
		DO(y,x,1,x,0);
		printf("Case #%d: %lld %lld\n",t,ansx,ansy);
	}
}
