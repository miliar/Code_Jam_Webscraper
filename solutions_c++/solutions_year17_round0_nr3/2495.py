#include <bits/stdc++.h>
using namespace std;

typedef long long LL;

LL k,n;
map<LL,LL> m;
LL ans1,ans2;

int main()
{
	int T,tc=0;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lld%lld",&n,&k);
		m.clear();
		m[n]=1;
		while(k)
		{
			auto it=m.end();
			it--;
			if (it->second<k) {
				k-=it->second;
				m[it->first/2]+=it->second;
				m[(it->first-1)/2]+=it->second;
				m.erase(it);
			}
			else {
				k=0;
				ans1=it->first/2;
				ans2=(it->first-1)/2;
			}
		}
		printf("Case #%d: %lld %lld\n",++tc,ans1,ans2);
	}
}
