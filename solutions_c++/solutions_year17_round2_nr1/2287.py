#include <cstdio>
#include <algorithm>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint D=0,N=0;
		scanf("%u%u",&D,&N);
		double mdt=0;
		for(uint i=0; i<N; ++i)
		{
			uint k=0,s=0;
			scanf("%u%u",&k,&s);
			double dt=double(D-k)/s;
			mdt=std::max(dt,mdt);
		}
		printf("Case #%u: %.9f\n",t,D/mdt);
	}
}
