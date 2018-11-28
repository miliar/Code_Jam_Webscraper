#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("C-small-2-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t;	scanf("%d",&t);
	int f1=t;
	while(t--)
	{
		long long int n,k,p=0,a,b;
		cin>>n>>k;
		//cout<<n <<" "<<k<<" ";
		priority_queue<int> pq;
		pq.push(n);
		while(k>1)
		{
			int f=pq.top();
			if(f%2)
			{
				pq.pop();
				pq.push(f/2);
				pq.push(f/2);
			}
			else
			{
				pq.pop();
				pq.push(f/2);
				pq.push(f/2 -1);
			}
			k--;
		}
		int f=pq.top();
		if(f%2)
			printf("Case #%d: %lld %lld\n",f1-t,f/2,f/2);
		else
			printf("Case #%d: %lld %lld\n",f1-t,f/2,f/2-1);
	}
}

	
