#include <bits/stdc++.h>
using namespace std;

long long t,n,k,a1,b1;

long long msb(long long x){
    long long b=1;
    x/=2;
    while(x>0){
        x/=2;
        b*=2;
    }
    return b;
}

int main(){
	freopen("C-large.in","r",stdin);
	freopen("Q3-large.out","w",stdout);
	scanf("%lld",&t);
	for(int tc=1;tc<=t;tc++){
		scanf("%lld%lld",&n,&k);
		//printf("%lld %lld\n",n,k);
		long long fac=msb(k);
		n-=k;
		n-=(n%fac);
		long long s=n/fac;
		b1=s/2;
		a1=s-b1;
		if(s==0) a1=0,b1=0;
		printf("Case #%d: %lld %lld\n",tc,a1,b1);
	}
}
