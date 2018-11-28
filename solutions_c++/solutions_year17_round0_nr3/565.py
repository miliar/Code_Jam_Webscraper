#include <cstdio>
#include <map>
typedef unsigned int uint;
typedef unsigned long long int ull;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		ull N=0,K=0;
		scanf("%llu%llu",&N,&K);
		std::map<ull,ull> s;
		s[N]=1;
		ull min=0,max=0;
		while(1)
		{
			auto l=s.end();
			--l;
			ull n=(*l).first;
			min=(n-1)/2;
			max=n-1-min;
			ull k=(*l).second;
			s.erase(l);
			if(k<K)
			{
				K-=k;
				if(0<min)
					s[min]+=k;
				if(0<max)
					s[max]+=k;
			}
			else break;
		}
		printf("Case #%u: %llu %llu\n",t,max,min);
	}
}
