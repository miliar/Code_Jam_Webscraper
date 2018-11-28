#include<stdio.h>
typedef unsigned long long uint64;
uint64 index(uint64 num)
{
	if(num == 0)
		return 0;
	uint64 v = 1000000000000000000;
	while(num/v == 0)
		v= v/10;
	return v;
}
uint64 f(uint64 num)
{
	uint64 base = index(num);
	//printf(" \nf called : num %lld base %lld",num,base);
	uint64 last_digit = 1;
	uint64 var = 0;
	while(base > 0)
	{
	uint64  current_digit;
	if(base == 1)
		current_digit = num;
	else
		current_digit = num/base;
	if(current_digit >= last_digit)
	{
		last_digit = current_digit;
		var = (var*10) + current_digit;
		num = num % base;
	}
	else
	{
		var = f(var -1);
		var = var * (base *10);
		var += ((base*10) -1);
		base = 0;
	}
	base = base/10;
}
//printf("returning from f : var %lld",var);
return var;
}
int main()
{
	uint64 T;
	scanf("%d",&T);
	for(int  j = 1; j <= T; j++)
	{
		uint64 N;
		scanf("%lld",&N);
		uint64 result = f(N);
		printf("Case #%d: %lld\n",j,result);
	}
	return 0;
}