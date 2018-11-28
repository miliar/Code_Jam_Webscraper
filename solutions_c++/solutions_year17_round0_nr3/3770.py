#include <bits/stdc++.h>
using namespace std;
multiset <int> s;
multiset <int> ::iterator it;
int main()
{
	int t,p=1;
	scanf("%d",&t);
	while(t--)
	{
		int n,k,x;
		scanf("%d%d",&n,&k);
		s.insert(n);
		printf("Case #%d: ",p);
		for(int i=0;i<k-1;i++)
		{
			it=s.end();
			--it;
			x=*it;
			if(x%2==0)
			{
				s.erase(it);
				s.insert((x-1)/2);
				s.insert(x/2);
			}
			else
			{
				s.erase(it);
				s.insert(x/2);
				s.insert(x/2);
			}
		}
		it=s.end();
		--it;
		x=*it;
		if(x%2==0)
		{
			printf("%d %d\n",x/2,(x-1)/2);
		}
		else
		{
			printf("%d %d\n",x/2,x/2);
		}
		s.clear();
		p++;
	}
}