#include <cstdio>
#include <algorithm>
#include <vector>
typedef unsigned int uint;
typedef unsigned long long int ll;

struct pancake
{
	pancake(int _r, int _h): r(_r), h(_h), as(2ll*r*h)
	{}
	friend bool operator< (pancake const &lhs, pancake const &rhs)
	{
		return lhs.as<rhs.as;
	}
	int r,h;
	ll as;
};

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,K=0;
		scanf("%u%u",&N,&K);
		std::vector<pancake> P;
		for(uint i=0; i<N; ++i)
		{
			int r=0,h=0;
			scanf("%d%d",&r,&h);
			P.push_back({r,h});
		}
		std::sort(P.begin(),P.end());
		ll ma=0;
		for(uint n=0; n<N; ++n)
		{
			ll a=ll(P[n].r)*P[n].r+P[n].as;
			uint k=1;
			for(uint i=N; k<K && i--;)
			{
				if(i==n)
					continue;
				++k;
				a+=P[i].as;
			}
			if(ma<a)
				ma=a;
		}
		double r=ma*M_PI;
		printf("Case #%u: %.7f\n",t,r);
	}
}
