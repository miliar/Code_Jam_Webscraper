#define LL long long
#define PLL pair<LL,LL>
#include <bits/stdc++.h>

using namespace std;

LL n,k,s;
int T,cas;
vector<PLL> v;

int main()
{
	for(cin>>T;T--;)
	{
		cin>>n>>k,v.clear();
		v.push_back(PLL(n,1));

		for(s=0;s<k;)
		{
			vector<PLL> t;
			for(int i=0;i<v.size();i++)
			{
				LL x=v[i].first,y=v[i].second;
				LL l=x>>1,r=(x-1)>>1;

				if((s+=y)>=k)
				{
					printf("Case #%d: %lld %lld\n",++cas,l,r);
					break;
				}
				t.push_back(PLL(l,y));
				t.push_back(PLL(r,y));
			}

			v.clear();
			for(int i=0;i<t.size();i++)
			{
				if(i>0 && t[i].first==t[i-1].first) t[i].second+=t[i-1].second;
				if((i==t.size()-1 || t[i+1].first!=t[i].first) && t[i].first) v.push_back(t[i]);
			}
		}
	}
}