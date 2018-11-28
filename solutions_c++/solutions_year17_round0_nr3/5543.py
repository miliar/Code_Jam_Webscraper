#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int l=1;l<=t;l++)
	{
		long long n,k;
		scanf("%lld %lld",&n,&k);
		printf("Case #%d: ",l);
		priority_queue<long long> pq;
		pq.push(n);
		while(k--)
		{
			long long a;
			a=pq.top();
			pq.pop();
			long long p1,p2;
			a--;
			p1=a/2;
			p2=a-p1;
			if(k==0)
			{
				printf("%lld %lld\n",max(p1,p2),min(p1,p2));
			}
			pq.push(p1);
			pq.push(p2);
		}
	}
}

