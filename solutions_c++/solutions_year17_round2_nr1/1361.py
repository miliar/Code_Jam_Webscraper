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
	static const size_t size = 1000;
	char buff[size+1] = { 0 };
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int d = 0,n = 0;scanf("%d%d",&d,&n);
		vector<unsigned int> ks(n,0),ss(n,0);
		for(unsigned int i = 0;i < n;++i) scanf("%d%d",&ks[i],&ss[i]);
		long double ans = 0;
		for(unsigned int i = 0;i < n;++i)
		{
			unsigned long long v = (unsigned long long)(d)*ss[i];
			long double t = (long double)(v)/(d-ks[i]);
			if(0 == ans) ans = t;
			else if(t < ans) ans = t;
		}
		printf("Case #%d: %.9f\n",iCases,(double)(ans));
	}
	return 0;
}