#include <cstdio>

int n,t;
long long a,b,c,k;

int main()
{
//	freopen("output.txt","w",stdout);

	scanf("%d",&n);

	for(t=1;t<=n;t++){
		scanf("%lld%lld",&a,&k);
		b=1, c=0;
		for(;;){
			if(b+c<k){
				k -= b+c;
				if(a%2){
					a = a/2;
					b = b+b+c;
				}
				else{
					a = --a/2;
					c = b+c+c;
				}
			}
			else{
				if(k<=c){
					printf("Case #%d: %lld %lld\n",t,(a+1)/2,a/2);
				}
				else{
					printf("Case #%d: %lld %lld\n",t,a/2,(a-1)/2);
				}
				break;
			}
		}
	}

	return 0;
}