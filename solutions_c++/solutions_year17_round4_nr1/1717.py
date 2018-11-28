#include <cstdio>
#include <algorithm>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,P=0;
		scanf("%u%u",&N,&P);
		uint n[4]={};
		for(uint i=0; i<N; ++i)
		{
			uint g=0;
			scanf("%u",&g);
			++n[g%P];
		}
		uint r=n[0];
		if(P==2)
			r+=(n[1]+1)/2;
		else if(P==3)
		{
			uint k=std::min(n[1],n[2]);
			r+=k;
			n[1]-=k;
			n[2]-=k;
			r+=(n[1]+2)/3;
			r+=(n[2]+2)/3;
		}
		printf("Case #%u: %u\n",t,r);
	}
}
