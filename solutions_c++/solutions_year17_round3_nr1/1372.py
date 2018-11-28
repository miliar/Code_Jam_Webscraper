#include <stdio.h>
#include <vector>
#include <algorithm>
#include <iostream>
#include<iomanip>

using std::vector;

int main()
{
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		unsigned int n = 0,k = 0;scanf("%d%d",&n,&k);
		vector<unsigned int> rs(n,0),hs(n,0);
		for(unsigned int i = 0;i < n;++i) scanf("%d%d",&rs[i],&hs[i]);
		unsigned long long ans = 0;
		for(unsigned int i = 0;i < n;++i)
		{
			unsigned int r0 = rs[i];
			vector<unsigned long long> data;
			for(unsigned int j = 0;j < n;++j)
			{
				if(rs[j] > r0) continue;
				if(j == i) continue;
				data.push_back((unsigned long long)(rs[j])*hs[j]*2);
			}
			if(data.size() + 1 < k) continue;
			std::sort(data.begin(),data.end());
			unsigned long long result = (unsigned long long)(r0)*r0 + 2*(unsigned long long)(r0)*hs[i];
			for(size_t j = 0,size = data.size();j + 1 < k;++j)
			{
				result += data[size-1-j];
			}
			if(result > ans) ans = result;
		}
		long double output = 3.141592653589793;
		output *= ans;
		std::cout << "Case #" << iCases << ": " << std::setprecision(28) << output << std::endl;
	}
	return 0;
}