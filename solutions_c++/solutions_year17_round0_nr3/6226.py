#include<bits/stdc++.h>
using namespace std;
int main()
{
	int T,c=1;
	priority_queue<long long> pq;
	long long N,K,mx,mn;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%lld%lld",&N,&K);
		while(!pq.empty())pq.pop();
	
		long long i=0,tmp;
		pq.push(N);
		
		
		while(i<K)
		{
			tmp=pq.top();
			//cout<<tmp<<endl;
			pq.pop();
			mx=tmp/2;
			if(tmp%2==0)mn=mx-1;
			else mn=mx;
			pq.push(mn);
			pq.push(mx);
			i++;
		}
		printf("Case #%d: %lld %lld\n",c,mx,mn);
		c++;
	}
	return 0;
}