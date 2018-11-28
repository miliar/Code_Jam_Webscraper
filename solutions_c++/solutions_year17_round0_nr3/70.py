#include<stdio.h>

typedef long long lld;
lld N, K, bl, b1, b2, cnt;

void test(int tn){
	scanf("%lld%lld", &N, &K);
	bl = N, b1 = 1, b2 = 0, cnt = 0;

	while(b1+b2){
		if(K <= cnt + b1+b2){
			if(K <= cnt + b2)printf("Case #%d: %lld %lld\n", tn, (bl+1)/2, bl/2);
			else printf("Case #%d: %lld %lld\n", tn, bl/2, (bl-1)/2);
			break;
		}
		cnt += b1+b2;
		if(bl%2 == 0)bl = bl/2-1, b2 = b1 + 2*b2;
		else bl = bl/2, b1 = 2*b1 + b2;
		if(bl == 0)bl = 1, b1 = b2, b2 = 0;
	}
}

int main(){
	int t;
	freopen("C-large.in","r",stdin); freopen("output.txt","w",stdout);
	scanf("%d", &t);
	for(int i=1; i<=t; i++)test(i);
	return 0;
}
