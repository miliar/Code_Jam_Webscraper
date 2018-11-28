#include <cstdio>
#include <cstring>
typedef unsigned int uint;

main()
{
	uint T=0;
	scanf("%u",&T);
	for(uint t=1; t<=T; ++t)
	{
		char S[1024];
		uint K=0;
		scanf("%s%u",S,&K);
		uint N=strlen(S);
		uint r=0;
		for(uint n=0; n+K<=N; ++n)
			if(S[n]=='-')
			{
				++r;
				for(uint i=0; i<K; ++i)
					S[n+i]= S[n+i]=='-'?'+':'-';
			}
		bool ok=1;
		for(uint n=0; ok && n<N; ++n)
			ok=S[n]=='+';
		if(ok)
			printf("Case #%u: %u\n",t,r);
		else printf("Case #%u: IMPOSSIBLE\n",t);
	}
}
