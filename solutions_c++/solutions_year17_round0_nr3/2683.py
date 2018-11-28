#include<stdio.h>
typedef unsigned long long uint64;
uint64 f(uint64 num)
{
	uint64 n = 1;
	/*if( num < 0XFF)
	n = 1;
	else if( num < 0XFFFF)
	n = 0x1FF;
	else if( num < 0XFFFFFF)
	n = 0X1FFFF;
	else if( num < 0XFFFFFFFF)
	n = 0x1FFFFFF;
	else if( num < 0XFFFFFFFFFF)
	n = 0X1FFFFFFFF;
	else if( num < 0XFFFFFFFFFFFF)
	n = 0x1FFFFFFFFFF;
	else if( num < 0XFFFFFFFFFFFFFF)
	n = 0X1FFFFFFFFFFFF;
	else
	n = 0xFFFFFFFFFFFFFF;
	*/
	while(n <= num)
	{
		n = n*2;
	}
	n =n/2;
	return n;
}

int main()
{
	int T;
	scanf("%d",&T);
	for(int index = 1; index <= T; index++)
	{
		uint64 N,M;
		scanf("%lld",&N);
		scanf("%lld",&M);
		
		uint64 base = f(M);
		//printf("%lld\n",base);
		uint64 val = (N-M + base)/base;
		//printf("%lld\n",val);
		uint64 x = val/2;
		uint64 y = (val-1)/2;
		printf("Case #%d: %lld %lld\n",index, x ,y);
	}
	return 0;
}
