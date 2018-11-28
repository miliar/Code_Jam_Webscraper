#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define mp(a,b) make_pair(a,b)
priority_queue< pair<ll,ll> > s;
int main()
{
	int t,i,j,l;
	ll n,k,curmax,curmin;
	scanf("%d",&t);
	l=t;
	while(t--)
	{
		scanf("%lld%lld",&n,&k);
		s.push(mp(n,1));
		while(k>0)
		{
			pair<ll,ll>  temp=s.top();
			s.pop();
			k-=temp.second;
			if ((temp.first)%2==1)
			{
				curmin=temp.first/2;
				curmax=temp.first/2;
				s.push(mp(curmin,2*(temp.second)));
				
			}
			else
			{
				curmin=temp.first/2-1;
				
				curmax=temp.first/2;
				s.push(mp(curmin,temp.second));
				s.push(mp(curmax,temp.second));
			}
		}
		printf("Case #%d: %lld %lld\n",l-t,curmax,curmin);
		while(!s.empty())
			s.pop();
	}
	return 0;
}
		
			
			
		
	
