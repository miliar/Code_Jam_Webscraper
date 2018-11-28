#include <stdio.h>
#include <string.h>
#include <vector>
#include <string>
#include <assert.h>
#include <map>

using std::vector;
using std::map;
using std::string;

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0,q = 0;scanf("%d%d",&n,&q);
		vector<unsigned int> he(n,0),hs(n,0);
		for(unsigned int i = 0;i < n;++i) scanf("%d%d",&he[i],&hs[i]);
		vector< vector<int> > dis(n,vector<int>(n,0));
		for(unsigned int i = 0;i < n;++i)
		{
			for(unsigned int j = 0;j < n;++j) scanf("%d",&dis[i][j]);
		}

		printf("Case #%d:",iCases);
		for(unsigned int iq = 0;iq < q;++iq)
		{
			unsigned int u = 0,v = 0;scanf("%d%d",&u,&v);
			-- u;-- v;
			vector<unsigned long long> sumdis(n,0);
			for(unsigned int i = n - 2;i != (unsigned int)(-1);--i) sumdis[i] += sumdis[i+1] + dis[i][i+1];
			vector<long double> dps(n,-100);
			dps[n - 1] = 0;
			for(unsigned int i = n - 2;i != (unsigned int)(-1);--i)
			{
				for(unsigned int j = i + 1;j < n;++j)
				{
					if(sumdis[i] - sumdis[j] > he[i]) break;
					long double t = (sumdis[i] - sumdis[j])*1.0/hs[i];
					assert(dps[j] >= 0);
					if(dps[i] < 0) dps[i] = dps[j] + t;
					else if(dps[j] + t < dps[i]) dps[i] = dps[j] + t;
				}
			}

			printf(" %.9f",dps[0]);
		}
		printf("\n");
	}
	return 0;
}