#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <stdio.h>
#include <string>

void solve()
{
	std::string d;
	int k;
	std::cin >> d >> k;
	int t =0;
	for(unsigned int i =0; i < d.size();++i)
	{
		if(d[i] =='-')
		{
			if((d.size() -i) < k)
			{
				printf("IMPOSSIBLE\n");
				return;
			}
			else
			{
				t+=1;
				for(int j = 0; j < k;++j)
				{
					d[i+j] = (d[i+j] =='-') ? '+' : '-';
				}
			}
		}
	}
	printf("%d\n", t);
}


int main()
{
	int t;
	std::cin >> t;
	for(int i =1; i <=t;++i)
	{
		printf("Case #%d: " , i);
		solve();
	}
	return 0;
}

