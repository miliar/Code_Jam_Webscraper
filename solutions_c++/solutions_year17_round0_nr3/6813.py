#include <iostream>
#include <cstring>
#include <vector>
#include <cstring>
#include <queue>
#include <utility>
using namespace std;
int T;
long long k,n;
int ca=1;
int main()
{
	scanf("%d",&T);
	while(T--)
	{
		cin>>n>>k;
		long long l;
		long long r;
		priority_queue<long long> q;
		q.push(n);
		while(k--)
		{
			long long t=q.top();
			q.pop();

			if(t%2==0)
			{
				l=t/2-1;
				if(l<0) l=0;
				r=t/2;
			}
			else
			{
				l=t/2;
				if(l<0) l=0;
				r=t/2;
			}
			// if(l)				
				q.push(l);
			// if(r)
				q.push(r);	
		}
		printf("Case #%d: %lld %lld\n",ca++,r,l);
	}
	return 0;
}