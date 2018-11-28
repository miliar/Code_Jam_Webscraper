#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
typedef unsigned int uint;
double eps=1e-9;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,K=0;
		scanf("%u%u",&N,&K);
		assert(N==K);
		double U=0;
		scanf("%lf",&U);
		std::vector<double> P(N);
		for(uint i=0; i<N; ++i)
			scanf("%lf",&P[i]);
		while(eps<U)
		{
			std::sort(P.begin(),P.end());
			double p0=P[0];
			uint k=1;
			while(k<P.size() && std::abs(P[k]-p0)<eps)
				++k;
			double p1=k<P.size()?P[k]:1.0;
			double du=std::min((p1-p0)*k,U);
			U-=du;
			for(uint i=0; i<k; ++i)
				P[i]+=du/k;
		}
		double r=1;
		for(auto p: P)
			r*=p;
		printf("Case #%u: %.7f\n",t,r);
	}
}
