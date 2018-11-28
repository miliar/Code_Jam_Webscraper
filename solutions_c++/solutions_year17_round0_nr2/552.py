#include <cstdio>
typedef unsigned int uint;
typedef unsigned long long int ull;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		ull N=0;
		scanf("%llu",&N);
		uint d[32]={};
		uint k=0;
		for(ull q=N; q; q/=10)
			d[k++]=q%10;
		d[k]=0;
		for(uint i=0; i+1<k; ++i)
		{
			if(d[i]<d[i+1])
			{
				uint j=0;
				while(j<=i)
					d[j++]=9;
				while(d[j]==0)
					d[j++]=9;
				--d[j];
			}
		}
		ull r=0;
		for(uint i=k; i--;)
			r=r*10+d[i];
		printf("Case #%u: %llu\n",t,r);
	}
}
