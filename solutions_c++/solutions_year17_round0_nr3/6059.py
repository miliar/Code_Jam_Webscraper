#include <bits/stdc++.h>
#define D(x...) fprintf(stderr, x)
using namespace std;
int T;
int main()
{
	scanf("%d ", &T);
	for(int t=1; t<=T; t++)
	{
		int N, K;
		multiset<int> S;
		scanf("%d %d", &N, &K);
		if(K>N) continue;
		S.insert(N);
		for(int k=0; k<K-1; k++)
		{
			auto i = S.end();
			i--;
			int x = (*i);
			S.erase(i);
			if(x%2==0)
			{
				if(x/2>0)S.insert(x/2);
				if((x/2-1)>0)S.insert(x/2-1);
			}
			else
			{
				if(x/2>0)
				{
					S.insert(x/2);
					S.insert(x/2);
				}
			}
		}
		auto i = S.end();
		i--;
		int x = (*i);
		if(x%2==0)
		{
			printf("Case #%d: %d %d\n", t, x/2, x/2-1);
		}
		else
		{
			printf("Case #%d: %d %d\n", t, x/2, x/2);
		}
	}
}