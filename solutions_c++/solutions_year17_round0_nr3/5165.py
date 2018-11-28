#include<bits/stdc++.h>

using namespace std;

int main()
{
	int t,cs=0;
	long long int n,k,mini,maxi;
	scanf("%d",&t);
	while(t--)
	{	
		cs++;
		printf("Case #%d: ",cs);
		priority_queue<long long int > pq;
		scanf("%lld %lld",&n,&k);
		pq.push(n);
		long long int top;
		while(k--)
		{
			top = pq.top();
			pq.pop();
			pq.push(top/2);
			pq.push((top-1)/2);
		}
		maxi = top/2;
		mini = (top-1)/2;
		printf("%lld %lld\n",maxi,mini);
	}

	return 0;
}