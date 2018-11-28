#include<bits/stdc++.h>

using namespace std;

long long n, k;
map<long long, long long> m;

int main()
{
	int tcc;
	scanf("%d", &tcc);
	for(int tc = 1; tc <= tcc; tc++)
	{
		printf("Case #%d: ", tc);

		scanf("%lld %lld", &n, &k);
		m.clear();

		m[n]++;
		while(1)
		{
			auto it = --m.end();
			if(it->second >= k)
			{
				printf("%lld %lld\n", ((it->first-1)/2)+((it->first-1)%2), (it->first-1)/2);
				break;
			}
			
			k -= it->second;
			m[(it->first-1)/2] += it->second;
			m[((it->first-1)/2)+((it->first-1)%2)] += it->second;
			m.erase(it);
		}
	}
	return 0;
}
