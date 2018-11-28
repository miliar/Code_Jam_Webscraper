#include <stdio.h>
#include <assert.h>

int main()
{
	static const size_t size = 64;
	unsigned long long exps[size] = { 1 };
	for(size_t i = 1;i < size;++i) exps[i] = exps[i-1]*2;
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned long long n = 0,p = 0,x = 0;scanf("%I64d%I64d",&n,&p);
		assert(p <= n && n < exps[size-1] && 0 != p);
		size_t k = size - 1;
		for(;p < exps[k];--k);
		x = p - exps[k];

		unsigned long long a = n%exps[k] + 1;
		unsigned long long b = exps[k] - a;

		unsigned long long ans = 0;
		if(x < a) ans = n/exps[k];
		else ans = n/exps[k] - 1;

		unsigned long long minans = 0,maxns = 0;
		if(ans&1) minans = ans/2,maxns = ans/2;
		else minans = ans/2 - 1,maxns = ans/2;

		printf("Case #%u: %I64u %I64u\n",iCases,maxns,minans);
	}
	return 0;
}