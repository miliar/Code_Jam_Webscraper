#include <cassert>
#include <cstdio>
#include <algorithm>
#include <vector>
typedef unsigned int uint;

struct range
{
	range(int _k=0, int _b=0, int _e=0): k(_k), b(_b), e(_e) {}
	friend bool operator< (range const &lhs, range const &rhs)
	{
		return lhs.b<rhs.b;
	}
	int k;
	int b,e;
};

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		uint N=0,M=0;
		scanf("%u%u",&N,&M);
		std::vector<range> A(N+M);
		for(uint i=0; i<N+M; ++i)
		{
			A[i].k=N<=i;
			scanf("%d%d",&A[i].b,&A[i].e);
		}
		std::sort(A.begin(),A.end());

		uint r=0;
		int sa[2]={};
		int s1=0;
		std::vector<int> s2[2];
		{
			int lk=A.back().k;
			int tl=A.back().e-1440;
			for(auto &a: A)
			{
				int dt=a.e-a.b;
				sa[a.k]+=dt;
				int g=a.b-tl;
				if(a.k!=lk)
				{
					s1+=g;
					++r;
				}
				else
				{
					sa[a.k]+=g;
					s2[a.k].push_back(g);
				}
				lk=a.k;
				tl=a.e;
			}
		}
		int k=sa[0]+s1<sa[1]+s1?0:1;
		std::sort(s2[1-k].begin(),s2[1-k].end());
		while(sa[k]+s1<720)
		{
			assert(!s2[1-k].empty());
			sa[k]+=s2[1-k].back();
			s2[1-k].pop_back();
			r+=2;
		}
		printf("Case #%u: %u\n",t,r);
	}
}
